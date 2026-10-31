# 🚀 Proyecto Web: Sistema de Gestión Base (Módulo I)

> **Subproyecto:** Desarrollo de Aplicaciones I  
> **Estudiante:** Luigi Henri Arismendi Toro  
> **Institución:** Universidad Nacional Experimental de los Llanos Occidentales "Ezequiel Zamora" (UNELLEZ)  

---

## 📌 Descripción del Proyecto
Este repositorio constituye la estructura inicial y los fundamentos técnicos de la aplicación web desarrollada para el subproyecto Desarrollo de Aplicaciones I. El proyecto integra el stack tecnológico compuesto por **Python, Django, Vite.js y Docker**, siguiendo estrictamente los principios de la **Metodología de Desarrollo en V**.

---

## ⚙️ Metodología de Desarrollo en V: Rama Descendente (Fase de Verificación)

Esta metodología garantiza calidad, mantenibilidad y coherencia en el desarrollo de software. Esta fase se enfoca en la verificación conceptual y técnica antes de la construcción avanzada de los módulos finales.

### 1. Análisis de Requisitos (*Requirement Gathering*)
En esta etapa inicial se identifican las necesidades del usuario final y los objetivos del sistema.
- **Objetivo General:** Proveer una plataforma web escalable, segura y multi-rol para la gestión de usuarios y procesos clave.
- **Definición de Roles de Usuario:**
  * **Administrador:** Control total sobre la base de datos, administración de usuarios y configuración global del sistema.
  * **Gestor:** Permisos avanzados para la gestión operativa y moderación de contenido/datos.
  * **Usuario Registrado:** Acceso a su perfil personal y funcionalidades principales de la plataforma.
  * **Visitante (Público):** Acceso restringido únicamente a páginas públicas, inicio de sesión y registro.

### 2. Análisis del Sistema (*System Analysis*)
Especifica el comportamiento general del software y la interacción entre sus componentes funcionales.
- **Casos de Uso Principales:**
  * Autenticación de usuario $\rightarrow$ Verificación de credenciales $\rightarrow$ Asignación de sesión con rol específico.
  * Navegación por la plataforma $\rightarrow$ Filtrado de plantillas/vistas (*Templates*) acorde a los privilegios del usuario.
- **Flujo de Navegación:**
  * Los usuarios no autenticados (Visitantes) son redirigidos automáticamente al portal de inicio o autenticación.
  * Una vez autenticado, Django evalúa el rol del usuario y renderiza la interfaz correspondiente.

### 3. Diseño de Software / Arquitectura (*Software Design*)
Define los componentes principales, las interfaces y la selección del Stack Tecnológico.
- **Stack de Desarrollo:**
  * **Backend:** Python 3.11 + Django Framework.
  * **Frontend / Build Tool:** Vite.js + HTML5 / CSS3 / JavaScript.
  * **Contenerización:** Docker & Docker Compose para aislamiento del entorno de desarrollo.
  * **Base de Datos:** SQLite (Desarrollo local) / PostgreSQL (Preparado para producción).
- **Arquitectura de Software:**
  * Patrón **MVT (Model-View-Template)** propio de Django, desacoplando la lógica de datos, la lógica de negocio y la presentación visual.

### 4. Diseño de Módulos (*Module Design*)
Detalla la lógica interna, modelos de datos y componentes individuales de cada aplicación.
- **Módulo de Autenticación (`usuarios` / `authentication`):**
  * **Modelos (`models.py`):** Extensión del modelo `User` de Django para almacenar información de roles y perfil.
  * **Vistas (`views.py`):** Lógica para formularios de registro, inicio de sesión y redirección basada en roles (`@login_required`, decoradores de permisos).
  * **Rutas (`urls.py`):** Mapeo limpio de endpoints de autenticación y navegación por rol.
- **Configuración del Panel de Administración (`admin.py`):**
  * Personalización del panel Django Admin para gestionar tablas, usuarios y roles de manera visual.

### 5. Punto de Inflexión: Codificación (*Coding*)
El momento de transición donde las especificaciones teóricas se convierten en código fuente ejecutable.
- **Acciones Realizadas:**
  * Configuración de contenedores en Docker (`Dockerfile` y `docker-compose.yml`).
  * Inicialización del repositorio de Git y subida a GitHub.
  * Instalación de Django y librerías base (`requirements.txt`).
  * Creación del proyecto Django y la app `usuarios`.
  * Configuración de plantillas base (*Templates*) con soporte para roles.
