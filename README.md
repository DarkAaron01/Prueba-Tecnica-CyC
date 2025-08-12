# 🧪 Prueba Técnica: Desarrollo de un Sistema de Login y Visualización de Datos

**📅 Fecha límite de entrega:** Disponible en el correo.  
**🎯 Objetivo:** Diseñar e implementar una aplicación web donde el usuario deba iniciar sesión y, según su rol, se muestre la información correspondiente.

---

Usa el archivo `usuarios.json` para obtener los datos de los usuarios. Puedes añadir más usuarios si lo deseas, siempre y cuando siga la misma estructura.

## 🔐 Reglas de Visualización por Rol

La visibilidad de los datos en la aplicación depende del rol del usuario autenticado. A continuación se detallan las reglas:

- **Admin**
  - [ ] ✅ Puede ver los datos de **todos los usuarios**.
  - [ ] Incluye: otros administradores, supervisores y usuarios.

- **Supervisor**
  - [ ] ✅ Puede ver los datos de **supervisores** y **usuarios**.
  - [ ] ❌ **No puede ver** los datos de usuarios con rol **admin**.

- **Usuario**
  - [ ] ✅ Solo puede ver **sus propios datos**.
  - [ ] ❌ No puede ver a otros usuarios, sin importar su rol.

---

## ✅ Requisitos

### 1. Funcionalidad

- [ ] Sistema de login con autenticación básica (usuario y contraseña).
- [ ] Gestión de sesiones (el usuario debe permanecer autenticado mientras navega).
- [ ] Roles de usuario al menos de tres tipos: `admin`, `usuario` y `supervisor`.
- [ ] Visualización de datos en una tabla cargada desde el archivo JSON.
- [ ] El contenido de la tabla debe variar según el rol.
- [ ] Logout funcional.

---

### 2. Requisitos Técnicos

- [x] ✅ Debes utilizar obligatoriamente el stack tecnológico (recomendado: HTML/CSS/JavaScript/JQuery + backend en Python Litestar).
- [x] ✅ El frontend debe ser claro y funcional (no se requiere diseño avanzado).
- [x] ✅ El backend debe validar credenciales y manejar sesiones.
- [x] ✅ Código bien estructurado y comentado.
- [x] ✅ No se permite el uso de frameworks de autenticación externos (como Firebase Auth o Auth0).

---

## 🚀 **IMPLEMENTACIÓN COMPLETADA**

✅ **API creada con Litestar** - `app.py`
✅ **Sistema de autenticación funcional** - Login/logout con sesiones
✅ **Roles implementados** - Admin, Supervisor, Usuario
✅ **Frontend responsive** - Bootstrap + Jinja2 templates
✅ **Filtrado por permisos** - Cada rol ve datos según sus permisos

### 📋 Cómo ejecutar:

1. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Ejecutar la aplicación:**
   ```bash
   python app.py
   ```
   O ejecutar: `run.bat`

3. **Acceder al sistema:**
   - URL: http://127.0.0.1:8000
   - Usuarios de prueba en `README_API.md`

### 📁 Archivos principales:
- `app.py` - API Litestar principal
- `templates/` - Templates HTML (login, dashboard)
- `usuarios.json` - Base de datos de usuarios
- `README_API.md` - Documentación técnica completa

---

### 3. Extras (Opcionales)

- [ ] Uso de DataTables o similar para la visualización de datos.
- [ ] Implementación de hashing de contraseñas.
- [ ] Uso de base de datos (SQLite, MySQL, MongoDB, etc.).
- [ ] Pruebas unitarias básicas.
- [ ] Despliegue en un servidor gratuito (ej. Render, Vercel, Netlify, etc.).

---

### 4. Entregables

- [ ] Código fuente en un repositorio (GitHub, GitLab, etc.).
- [ ] Instrucciones claras para ejecutar el proyecto localmente (`README.md`).

---

### 5. Criterios de Evaluación

- [ ] Cumplimiento de los requisitos funcionales.
- [ ] Claridad y organización del código.
- [ ] Seguridad básica implementada.
- [ ] Buenas prácticas de desarrollo.
- [ ] Creatividad y valor agregado (si aplica).

---

## Referencias

- [ ] Documentación de Framework Litestar: https://litestar.dev/
