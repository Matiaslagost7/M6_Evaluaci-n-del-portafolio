# 🚗 Sistema de Concesionaria - Django

Sistema web completo para la gestión de una concesionaria de automóviles, desarrollado con Django 5.2.6 y Python 3.12. Incluye catálogo público, sistema de contacto, panel administrativo y gestión de inventario.

## 📋 Tabla de Contenidos

- [Características](#características)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Requisitos Previos](#requisitos-previos)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Uso](#uso)
- [Funcionalidades](#funcionalidades)
- [Modelos de Datos](#modelos-de-datos)
- [Sistema de Permisos](#sistema-de-permisos)
- [Estructura de URLs](#estructura-de-urls)

## ✨ Características

### Área Pública
- ✅ Catálogo de vehículos con sistema de búsqueda
- ✅ Vista detallada de cada automóvil
- ✅ Formulario de contacto
- ✅ Indicadores de disponibilidad en tiempo real (basado en stock)
- ✅ Diseño responsive con Bootstrap 5

### Panel Administrativo
- ✅ Sistema de autenticación personalizado
- ✅ Gestión completa de inventario (CRUD)
- ✅ Control de stock automático
- ✅ Gestión de usuarios con diferentes permisos
- ✅ Dashboard con estadísticas
- ✅ Carga y gestión de imágenes

## 📁 Estructura del Proyecto

```
concesionaria/
│
├── concesionaria/          # Configuración principal del proyecto
│   ├── settings.py         # Configuración de Django
│   ├── urls.py             # URLs principales
│   ├── wsgi.py             # Configuración WSGI
│   └── asgi.py             # Configuración ASGI
│
├── autos/                  # Aplicación pública (catálogo)
│   ├── models.py           # Modelo Automovil
│   ├── views.py            # Vistas públicas
│   ├── forms.py            # Formularios (AutomovilForm, ContactoForm)
│   ├── urls.py             # URLs con namespace 'public'
│   ├── admin.py            # Configuración del admin de Django
│   ├── static/             # Archivos estáticos públicos
│   │   ├── css/            # Estilos del catálogo
│   │   ├── js/             # Scripts del catálogo
│   │   └── image/          # Imágenes públicas
│   └── templates/          # Templates públicos
│       ├── base.html       # Template base
│       ├── index.html      # Página principal
│       ├── catalogo.html   # Listado de vehículos
│       ├── detalle_auto.html
│       ├── contacto.html
│       └── buscar_automovil.html
│
├── login/                  # Aplicación de administración
│   ├── models.py           # Modelo CustomUser
│   ├── views.py            # Vistas administrativas
│   ├── forms.py            # Formularios de usuario
│   ├── mixins.py           # Decoradores y mixins
│   ├── urls.py             # URLs con namespace 'panel'
│   ├── static/             # Archivos estáticos del panel
│   │   ├── css/            # Estilos del panel admin
│   │   └── js/             # Scripts del panel admin
│   └── templates/          # Templates administrativos
│       ├── login.html
│       ├── register.html
│       ├── panel_admin.html
│       ├── inventario.html
│       ├── crear_automovil.html
│       ├── editar_automovil.html
│       └── eliminar_automovil.html
│
├── media/                  # Archivos cargados por usuarios
│   └── autos/              # Imágenes de automóviles
│
├── db.sqlite3              # Base de datos SQLite
├── manage.py               # Script de gestión de Django
└── README.md               # Este archivo
```

## 🛠️ Tecnologías Utilizadas

### Backend
- **Django 5.2.6** - Framework web principal
- **Python 3.12** - Lenguaje de programación
- **SQLite** - Base de datos
- **Pillow 12.0.0** - Procesamiento de imágenes

### Frontend
- **Bootstrap 5.3.3** - Framework CSS
- **Font Awesome 6.0.0** - Iconos
- **JavaScript vanilla** - Interactividad del cliente

### Dependencias Adicionales
- **asgiref 3.10.0** - Soporte ASGI
- **sqlparse 0.5.3** - Formateo SQL
- **tzdata 2025.2** - Datos de zonas horarias

## 📦 Requisitos Previos

- Python 3.12 o superior
- pip (gestor de paquetes de Python)
- Entorno virtual (recomendado)

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd "M6_Evaluación del portafolio"
```

### 2. Crear y activar entorno virtual

**Windows (PowerShell):**
```powershell
python -m venv env
.\env\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
python -m venv env
env\Scripts\activate.bat
```

**Linux/Mac:**
```bash
python -m venv env
source env/bin/activate
```

### 3. Instalar dependencias

```bash
pip install django==5.2.6
pip install pillow==12.0.0
pip install asgiref==3.10.0
pip install sqlparse==0.5.3
pip install tzdata==2025.2
```

O usar requirements.txt (si está disponible):
```bash
pip install -r requirements.txt
```

### 4. Aplicar migraciones

```bash
cd concesionaria
python manage.py migrate
```

### 5. Crear superusuario

```bash
python manage.py createsuperuser
```

Sigue las instrucciones en pantalla para crear tu cuenta de administrador.

### 6. Ejecutar el servidor

```bash
python manage.py runserver
```

La aplicación estará disponible en: `http://127.0.0.1:8000/`

## 👥 Usuarios de Prueba

El sistema incluye los siguientes usuarios pre-configurados para pruebas:

### Superusuario (Acceso Total)
- **Usuario**: `Mati1`
- **Contraseña**: `Mati2000`
- **Permisos**: 
  - ✅ Acceso completo al sistema
  - ✅ Gestión de inventario (crear, editar, eliminar)
  - ✅ Gestión de usuarios y permisos
  - ✅ Acceso al admin de Django
  - ✅ Panel administrativo completo

### Administrador de Inventario
- **Usuario**: `Mati2`
- **Contraseña**: `Trabajo2000`
- **Permisos**:
  - ✅ Gestión completa de inventario
  - ✅ Puede eliminar automóviles
  - ✅ Crear y editar vehículos
  - ✅ Acceso al panel administrativo
  - ❌ No puede gestionar usuarios

### Editor de Inventario
- **Usuario**: `Mati3`
- **Contraseña**: `Trabajo2000`
- **Permisos**:
  - ✅ Crear nuevos automóviles
  - ✅ Editar automóviles existentes
  - ✅ Ver inventario completo
  - ✅ Acceso al panel administrativo
  - ❌ No puede eliminar automóviles
  - ❌ No puede gestionar usuarios

### Gestor de Permisos y Roles
- **Usuario**: `Mati4`
- **Contraseña**: `Trabajo2000`
- **Permisos**:
  - ✅ Gestionar usuarios del sistema
  - ✅ Asignar permisos y roles
  - ✅ Crear y editar usuarios
  - ✅ Acceso al panel administrativo
  - ⚠️ Acceso limitado al inventario (solo lectura)

### Usuario Común
- **Usuario**: `Mati5`
- **Contraseña**: `Trabajo2000`
- **Permisos**:
  - ✅ Acceso al catálogo público
  - ✅ Ver detalles de vehículos
  - ✅ Usar formulario de contacto
  - ❌ Sin acceso al panel administrativo
  - ❌ Sin acceso al inventario
  - ❌ Sin permisos de gestión

### Resumen de Permisos por Usuario

| Usuario | Superuser | Ver Inventario | Crear Auto | Editar Auto | Eliminar Auto | Gestionar Usuarios | Admin Django |
|---------|-----------|----------------|------------|-------------|---------------|-------------------|--------------|
| Mati1   | ✅        | ✅             | ✅         | ✅          | ✅            | ✅                | ✅           |
| Mati2   | ❌        | ✅             | ✅         | ✅          | ✅            | ❌                | ❌           |
| Mati3   | ❌        | ✅             | ✅         | ✅          | ❌            | ❌                | ❌           |
| Mati4   | ❌        | ⚠️             | ❌         | ❌          | ❌            | ✅                | ❌           |
| Mati5   | ❌        | ❌             | ❌         | ❌          | ❌            | ❌                | ❌           |

> **Nota**: Estos usuarios están configurados para pruebas y demostración del sistema de permisos. En un entorno de producción, se recomienda cambiar todas las contraseñas y crear usuarios con credenciales seguras.

## ⚙️ Configuración

### Variables importantes en `settings.py`

```python
# Modelo de usuario personalizado
AUTH_USER_MODEL = 'login.CustomUser'

# URL de login
LOGIN_URL = '/login/'

# Archivos media
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Archivos estáticos
STATIC_URL = 'static/'
```

### Base de datos

Por defecto, el proyecto usa SQLite. Para cambiar a PostgreSQL o MySQL, modifica la configuración en `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nombre_base_datos',
        'USER': 'usuario',
        'PASSWORD': 'contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 📖 Uso

### Inicio de Sesión Rápido

Para probar las diferentes funcionalidades del sistema, puedes usar estos usuarios:

```
Acceso completo:    Mati1 / Mati2000
Admin inventario:   Mati2 / Trabajo2000
Editor inventario:  Mati3 / Trabajo2000
Gestor usuarios:    Mati4 / Trabajo2000
Usuario común:      Mati5 / Trabajo2000
```

### Acceso Público

1. **Página Principal**: `http://127.0.0.1:8000/`
   - Muestra vehículos destacados y acceso al catálogo

2. **Catálogo**: `http://127.0.0.1:8000/catalogo/`
   - Lista todos los vehículos disponibles
   - Sistema de búsqueda por marca y modelo
   - Indicadores de stock

3. **Detalle de Vehículo**: `http://127.0.0.1:8000/detalle/<id>/`
   - Información completa del vehículo
   - Imágenes
   - Estado de disponibilidad

4. **Contacto**: `http://127.0.0.1:8000/contacto/`
   - Formulario para consultas

### Panel Administrativo

1. **Login**: `http://127.0.0.1:8000/login/`
   - Acceso para usuarios registrados

2. **Panel Admin**: `http://127.0.0.1:8000/panel/`
   - Dashboard con estadísticas
   - Acceso rápido a funciones

3. **Inventario**: `http://127.0.0.1:8000/panel/inventario/`
   - Lista completa de vehículos
   - Filtros por disponibilidad
   - Contadores de stock

4. **Gestión de Vehículos**:
   - Crear: `http://127.0.0.1:8000/panel/crear/`
   - Editar: `http://127.0.0.1:8000/panel/editar/<id>/`
   - Eliminar: `http://127.0.0.1:8000/panel/eliminar/<id>/`

5. **Gestión de Usuarios**: `http://127.0.0.1:8000/panel/usuarios/`
   - Solo para superusuarios
   - Crear, editar y eliminar usuarios

## 🎯 Funcionalidades

### Sistema de Stock Automático

El sistema utiliza el campo `stock` para determinar automáticamente la disponibilidad:

- **Stock > 0**: Vehículo disponible (muestra badge verde)
- **Stock = 0**: Vehículo no disponible (muestra badge rojo)

```python
# En templates:
{% if auto.stock > 0 %}
    <span class="badge bg-success">Disponible ({{ auto.stock }} unidades)</span>
{% else %}
    <span class="badge bg-danger">Sin Stock</span>
{% endif %}
```

### Sistema de Búsqueda

Búsqueda inteligente que filtra por:
- Marca del vehículo
- Modelo del vehículo
- Solo vehículos con stock disponible

### Formularios con Validación

Todos los formularios incluyen:
- Validación del lado del servidor
- Validación del lado del cliente (HTML5)
- Mensajes de error claros
- Ayudas contextuales (help_text)
- Estilos Bootstrap

## 🗄️ Modelos de Datos

### Modelo Automovil

```python
class Automovil(models.Model):
    marca = models.CharField(max_length=100, verbose_name='Marca')
    modelo = models.CharField(max_length=100, verbose_name='Modelo')
    anio = models.IntegerField(verbose_name='Año')
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')
    stock = models.IntegerField(default=1, verbose_name='Stock disponible')
    descripcion = models.TextField(blank=True, null=True, verbose_name='Descripción')
    imagen = models.ImageField(upload_to='autos/', blank=True, null=True, verbose_name='Imagen')
```

**Campos:**
- `marca`: Marca del vehículo (obligatorio)
- `modelo`: Modelo del vehículo (obligatorio)
- `anio`: Año de fabricación (obligatorio)
- `precio`: Precio en formato decimal (obligatorio)
- `stock`: Cantidad disponible (default: 1)
- `descripcion`: Descripción detallada (opcional)
- `imagen`: Imagen del vehículo (opcional)

### Modelo CustomUser

```python
class CustomUser(AbstractUser):
    # Hereda todos los campos de AbstractUser
    # + configuración de permisos personalizados
    
    class Meta:
        permissions = [
            ('puede_gestionar_usuarios', 'Puede gestionar usuarios del sistema'),
        ]
```

**Permisos especiales:**
- `puede_gestionar_usuarios`: Permite administrar otros usuarios

## 🔐 Sistema de Permisos

### Decoradores Personalizados

**`@solo_login_requerido`**
- Requiere que el usuario esté autenticado
- Redirige a login si no está autenticado

**`verificar_login_y_permisos()`**
- Verifica autenticación
- Verifica permisos específicos
- Maneja redirecciones y mensajes de error

### Niveles de Acceso

1. **Público** (sin autenticación):
   - Página principal
   - Catálogo
   - Detalle de vehículos
   - Contacto
   - Búsqueda

2. **Usuario Común** (ej: Mati5):
   - Acceso solo al área pública
   - Sin permisos administrativos

3. **Editor de Inventario** (ej: Mati3):
   - Panel administrativo
   - Crear y editar automóviles
   - Ver inventario completo
   - No puede eliminar vehículos

4. **Administrador de Inventario** (ej: Mati2):
   - Todo lo anterior +
   - Eliminar automóviles
   - Gestión completa del inventario

5. **Gestor de Permisos** (ej: Mati4):
   - Panel administrativo
   - Gestión de usuarios y roles
   - Asignación de permisos
   - Acceso limitado al inventario

6. **Superusuario** (ej: Mati1):
   - Acceso total al sistema
   - Todas las funcionalidades anteriores
   - Acceso al admin de Django
   - Control total de usuarios y permisos

## 🌐 Estructura de URLs

### URLs Públicas (namespace: 'public')

```python
'' → index
'catalogo/' → catalogo
'detalle/<int:id>/' → detalle_automovil
'contacto/' → contacto
'buscar/' → buscar_automovil
```

### URLs del Panel (namespace: 'panel')

```python
'' → panel_admin
'inventario/' → inventario
'crear/' → crear_automovil
'editar/<int:pk>/' → editar_automovil
'eliminar/<int:pk>/' → eliminar_automovil
'usuarios/' → gestionar_usuarios
'usuarios/editar/<int:pk>/' → editar_usuario
'usuarios/eliminar/<int:pk>/' → eliminar_usuario
```

### URLs de Autenticación

```python
'login/' → login_view
'logout/' → logout_view
'register/' → register_view
```

## 📊 Características del Admin de Django

Acceso: `http://127.0.0.1:8000/admin/`

**Configuración personalizada para Automovil:**
```python
class AutomovilAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'anio', 'precio', 'stock', 'disponible_display')
    list_filter = ('marca', 'anio')
    search_fields = ('marca', 'modelo')
    ordering = ('-anio',)
```

## 🎨 Estilos y Diseño

### Sistema de Colores

- **Primary**: Azul (`#0d6efd`) - Acciones principales
- **Success**: Verde (`#198754`) - Disponible, confirmaciones
- **Danger**: Rojo (`#dc3545`) - Eliminar, sin stock
- **Warning**: Amarillo (`#ffc107`) - Editar, advertencias
- **Secondary**: Gris (`#6c757d`) - Acciones secundarias

### Componentes Personalizados

- Cards con sombras y hover effects
- Badges de estado dinámicos
- Formularios con validación visual
- Alertas con iconos Font Awesome
- Tablas responsivas
- Modales para confirmaciones

## 🔧 Comandos Útiles

### Gestión del Proyecto

```bash
# Ejecutar servidor de desarrollo
python manage.py runserver

# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Recopilar archivos estáticos
python manage.py collectstatic

# Abrir shell de Django
python manage.py shell
```

### Gestión de la Base de Datos

```bash
# Ver SQL de una migración
python manage.py sqlmigrate autos 0001

# Verificar problemas en el proyecto
python manage.py check

# Limpiar sesiones expiradas
python manage.py clearsessions
```

## 🐛 Solución de Problemas

### El servidor no inicia

**Error**: `Port already in use`
```bash
# Windows: Matar proceso en puerto 8000
netstat -ano | findstr :8000
taskkill /PID <número_de_proceso> /F
```

### Errores de migración

```bash
# Reiniciar migraciones (¡CUIDADO! Elimina datos)
python manage.py migrate autos zero
python manage.py migrate autos

# O eliminar db.sqlite3 y volver a migrar
python manage.py migrate
```

### Imágenes no se muestran

Verifica en `settings.py`:
```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

Y en `urls.py` principal:
```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... tus urls
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### CSS no se aplica

```bash
# Limpiar caché del navegador: Ctrl + Shift + R
# Verificar ruta en template:
{% load static %}
<link href="{% static 'css/styles.css' %}" rel="stylesheet">
```

## 📝 Notas de Desarrollo

### Migraciones Aplicadas

1. **0001_initial**: Creación inicial del modelo Automovil
2. **0002**: Agregado campo `estado` (obsoleto, removido)
3. **0003**: Sistema de stock implementado, campos `disponible` y `estado` eliminados

### Cambios Importantes

- **Sistema de disponibilidad**: Cambió de campo booleano `disponible` a sistema basado en `stock`
- **Permisos**: Sistema de permisos personalizados para gestión de usuarios
- **Templates**: Uso de herencia de templates con `base.html` compartido

## 🤝 Contribuciones

Este proyecto fue desarrollado como parte del Módulo 6 - Evaluación del Portafolio del Bootcamp.

## 📄 Licencia

Este proyecto es de uso educativo.

## 👨‍💻 Autor

Desarrollado como proyecto de evaluación del Bootcamp de Desarrollo Full Stack.

---

**Versión**: 1.0.0  
**Última actualización**: Octubre 2025  
**Django**: 5.2.6  
**Python**: 3.12
