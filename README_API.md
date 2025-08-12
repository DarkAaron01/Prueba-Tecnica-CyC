# 🚀 Sistema de Login y Visualización de Datos - API con Litestar

Este proyecto implementa un sistema de autenticación con roles y visualización de datos usando **Litestar** como framework backend y HTML/CSS/JavaScript para el frontend.

## 📋 Características

- ✅ Sistema de login con autenticación básica
- ✅ Gestión de sesiones con cookies HTTP
- ✅ Tres roles de usuario: `admin`, `supervisor`, `usuario`
- ✅ Filtrado de datos según permisos del rol
- ✅ Interfaz web responsive con Bootstrap
- ✅ API REST para acceso programático

## 🏗️ Estructura del Proyecto

```
prueba-tecnica-cyc-main/
├── app.py                 # Aplicación principal Litestar
├── usuarios.json          # Base de datos de usuarios
├── requirements.txt       # Dependencias Python
├── templates/            
│   ├── base.html         # Template base
│   ├── login.html        # Página de login
│   └── dashboard.html    # Dashboard principal
├── static/               # Archivos estáticos (CSS, JS, imágenes)
└── README_API.md         # Esta documentación
```

## 🔐 Reglas de Acceso por Rol

### Admin
- ✅ Puede ver **todos los usuarios** (admins, supervisores y usuarios)
- ✅ Acceso completo al sistema

### Supervisor  
- ✅ Puede ver **supervisores** y **usuarios**
- ❌ **No puede ver** usuarios con rol **admin**

### Usuario
- ✅ Solo puede ver **sus propios datos**
- ❌ No puede ver otros usuarios

## 🔑 Usuarios de Prueba

| Nombre | Rol | Contraseña |
|--------|-----|------------|
| Jhon Doe | admin | admin123 |
| Juan Pérez | admin | admin123 |
| Ana Torres | supervisor | super123 |
| Luis Gómez | supervisor | super123 |
| Valentina Ríos | usuario | user123 |
| Mateo Vargas | usuario | user123 |

*Nota: Para cualquier usuario, usa su nombre completo como username y la contraseña según su rol.*

## 🚀 Instalación y Ejecución

### 1. Configurar el entorno virtual
```bash
python -m venv .venv
.venv\Scripts\activate  # En Windows
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Ejecutar la aplicación
```bash
python app.py
```

### 4. Acceder a la aplicación
Abre tu navegador y ve a: `http://127.0.0.1:8000`

## 🌐 Endpoints de la API

### Web Routes
- `GET /` - Página principal (redirige según autenticación)
- `GET /login` - Página de login
- `POST /login` - Procesar login
- `GET /dashboard` - Dashboard con datos filtrados
- `POST /logout` - Cerrar sesión

### API Routes
- `GET /api/users` - Obtener usuarios (requiere autenticación)

## 💾 Formato de Datos

### Usuario (usuarios.json)
```json
{
  "id": 1,
  "nombre": "Jhon Doe",
  "rol": "admin",
  "renta_mensual": 2523.06
}
```

### Respuesta API (/api/users)
```json
{
  "users": [...],
  "current_user": {...},
  "total": 5
}
```

## 🔒 Seguridad

- **Sesiones**: Gestión de sesiones con timeout de 2 horas
- **Cookies HTTP**: Cookies con flag `httponly` para prevenir XSS
- **Validación**: Validación de entrada en todos los endpoints
- **Autenticación**: Sistema de autenticación personalizado sin dependencias externas

## 🎨 Frontend

- **Bootstrap 5**: Framework CSS para diseño responsive
- **Font Awesome**: Iconos
- **jQuery**: Funcionalidad JavaScript adicional
- **Jinja2**: Motor de templates

## 📝 Notas Técnicas

1. **Passwords**: En este ejemplo se usan contraseñas por defecto según el rol. En producción usar hash seguro (bcrypt).

2. **Base de Datos**: Se usa archivo JSON para simplicidad. En producción usar base de datos real.

3. **Sesiones**: Almacenadas en memoria. En producción usar Redis o base de datos.

4. **HTTPS**: En producción, siempre usar HTTPS para cookies seguras.

## 🐛 Troubleshooting

### Error: "Module not found"
```bash
pip install -r requirements.txt
```

### Error: "Port already in use"
Cambia el puerto en `app.py`:
```python
uvicorn.run("app:app", host="127.0.0.1", port=8001, reload=True)
```

### Error: "Template not found"
Verifica que la carpeta `templates/` esté en el directorio raíz del proyecto.

## 📞 Soporte

Si encuentras algún problema:
1. Verifica que todas las dependencias estén instaladas
2. Confirma que el archivo `usuarios.json` esté presente
3. Revisa que los templates estén en la carpeta correcta
4. Verifica los logs en la consola para errores específicos
