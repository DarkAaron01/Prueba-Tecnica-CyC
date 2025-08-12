import json
import hashlib
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Any
from uuid import uuid4

from litestar import Litestar, get, post, Request, Response
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.exceptions import NotAuthorizedException, ValidationException
from litestar.response import Template, Redirect
from litestar.static_files import StaticFilesConfig
from litestar.template.config import TemplateConfig
from litestar.datastructures import State


# Configuración de sesiones
SESSIONS: Dict[str, Dict[str, Any]] = {}
SESSION_TIMEOUT = timedelta(hours=2)

# Cargar datos de usuarios
def load_users() -> List[Dict[str, Any]]:
    """Carga los usuarios desde el archivo JSON"""
    try:
        with open("usuarios.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Funciones de utilidad para autenticación
def create_session(user_data: Dict[str, Any]) -> str:
    """Crea una nueva sesión para el usuario"""
    session_id = str(uuid4())
    SESSIONS[session_id] = {
        "user": user_data,
        "created_at": datetime.now(),
        "expires_at": datetime.now() + SESSION_TIMEOUT
    }
    return session_id

def validate_session(session_id: str) -> Optional[Dict[str, Any]]:
    """Valida una sesión existente"""
    if not session_id or session_id not in SESSIONS:
        return None
    
    session = SESSIONS[session_id]
    if datetime.now() > session["expires_at"]:
        del SESSIONS[session_id]
        return None
    
    return session["user"]

def get_current_user(request: Request) -> Optional[Dict[str, Any]]:
    """Obtiene el usuario actual desde la sesión"""
    session_id = request.cookies.get("session_id")
    return validate_session(session_id) if session_id else None

def hash_password(password: str) -> str:
    """Hash simple para la contraseña (en producción usar bcrypt)"""
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate_user(username: str, password: str) -> Optional[Dict[str, Any]]:
    """Autentica un usuario con username y password"""
    users = load_users()
    
    # Para este ejemplo, usamos el nombre como username y un password simple
    # En un sistema real, tendrías campos separados para username/email y password
    for user in users:
        # Usamos el nombre como username y una contraseña por defecto basada en el rol
        default_passwords = {
            "admin": "admin123",
            "supervisor": "super123", 
            "usuario": "user123"
        }
        
        expected_password = default_passwords.get(user["rol"], "default123")
        
        if user["nombre"].lower() == username.lower() and password == expected_password:
            # En producción, agregar aquí hash de password y validaciones adicionales
            return user
    
    return None

def filter_users_by_role(current_user: Dict[str, Any], all_users: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Filtra usuarios según el rol del usuario actual"""
    user_role = current_user["rol"]
    
    if user_role == "admin":
        # Admin puede ver todos los usuarios
        return all_users
    elif user_role == "supervisor":
        # Supervisor puede ver supervisores y usuarios, pero no admins
        return [user for user in all_users if user["rol"] in ["supervisor", "usuario"]]
    else:  # usuario
        # Usuario solo puede ver sus propios datos
        return [user for user in all_users if user["id"] == current_user["id"]]

# Rutas de la aplicación
@get("/")
async def home(request: Request) -> Template:
    """Página principal - redirige según estado de autenticación"""
    user = get_current_user(request)
    if user:
        return Template(template_name="dashboard.html", context={"user": user})
    return Template(template_name="login.html")

@get("/login")
async def login_page() -> Template:
    """Página de login"""
    return Template(template_name="login.html")

@post("/login")
async def login(request: Request) -> Response:
    """Procesa el login del usuario"""
    try:
        form_data = await request.form()
        username = form_data.get("username", "").strip()
        password = form_data.get("password", "").strip()
        
        if not username or not password:
            return Template(
                template_name="login.html", 
                context={"error": "Username y password son requeridos"}
            )
        
        user = authenticate_user(username, password)
        if not user:
            return Template(
                template_name="login.html",
                context={"error": "Credenciales inválidas"}
            )
        
        session_id = create_session(user)
        response = Redirect(path="/dashboard")
        response.set_cookie("session_id", session_id, httponly=True)
        return response
        
    except Exception as e:
        return Template(
            template_name="login.html",
            context={"error": "Error interno del servidor"}
        )

@get("/dashboard")
async def dashboard(request: Request) -> Template:
    """Dashboard principal con datos filtrados por rol"""
    user = get_current_user(request)
    if not user:
        return Redirect(path="/login")
    
    all_users = load_users()
    filtered_users = filter_users_by_role(user, all_users)
    
    return Template(
        template_name="dashboard.html",
        context={
            "user": user,
            "users": filtered_users,
            "total_users": len(filtered_users)
        }
    )

@post("/logout")
async def logout(request: Request) -> Response:
    """Cierra la sesión del usuario"""
    session_id = request.cookies.get("session_id")
    if session_id and session_id in SESSIONS:
        del SESSIONS[session_id]
    
    response = Redirect(path="/login")
    response.delete_cookie("session_id")
    return response

@get("/api/users")
async def api_get_users(request: Request) -> Dict[str, Any]:
    """API endpoint para obtener usuarios (requiere autenticación)"""
    user = get_current_user(request)
    if not user:
        raise NotAuthorizedException("No autorizado")
    
    all_users = load_users()
    filtered_users = filter_users_by_role(user, all_users)
    
    return {
        "users": filtered_users,
        "current_user": user,
        "total": len(filtered_users)
    }

# Configuración de la aplicación
def create_app() -> Litestar:
    """Crea y configura la aplicación Litestar"""
    
    return Litestar(
        route_handlers=[
            home,
            login_page,
            login,
            dashboard,
            logout,
            api_get_users
        ],
        template_config=TemplateConfig(
            engine=JinjaTemplateEngine,
            directory=Path("templates")
        ),
        static_files_config=[
            StaticFilesConfig(
                path="/static",
                directories=[Path("static")]
            )
        ],
        debug=True
    )

app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
