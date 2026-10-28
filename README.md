# 🚀 Sistema Web Integral - Módulo de Gestión y Autenticación

> **Subproyecto:** Desarrollo de Aplicaciones  
> **Estudiante:** Luigi Henri Arismendi Toro  
> **Institución:** Universidad Nacional Experimental de los Llanos Occidentales "Ezequiel Zamora" (UNELLEZ)  

---

## 📌 Contexto y Propósito del Sistema
Este repositorio contiene la arquitectura base y el despliegue inicial de un sistema web escalable. El desarrollo se rige bajo los estándares de la **Metodología en V**, garantizando la trazabilidad estricta entre el diseño conceptual, la arquitectura técnica y la codificación modular.

---

## 📊 Material Visual: Metodología de Desarrollo en V

A continuación se presenta la infografía oficial que resume el flujo completo de la metodología, conectando la rama descendente de verificación con la rama ascendente de validación:

![Infografía Metodología en V](1.jpg)

---

## 🔍 Desglose Técnico de las Fases del Proyecto

### 1. Análisis de Requisitos (*Requirement Gathering*)
En esta etapa inicial se identifican las necesidades del usuario final y los objetivos del sistema.
* **Objetivo General:** Proveer una plataforma web escalable, segura y multi-rol para la gestión de usuarios y procesos clave.
* **Definición de Roles de Usuario:**
  * **Administrador:** Control total sobre la base de datos, administración de usuarios y configuración del sistema.
  * **Gestor:** Permisos avanzados para la gestión operativa y moderación de contenido/datos.
  * **Usuario Registrado:** Acceso a su perfil personal y funcionalidades principales de la plataforma.
  * **Visitante (Público):** Acceso restringido únicamente a páginas públicas, login y registro.

### 2. Análisis del Sistema (*System Analysis*)
Define el comportamiento general del software y la interacción entre sus componentes funcionales.
* **Casos de Uso Principales:**
  * Autenticación de usuario $\rightarrow$ Verificación de credenciales $\rightarrow$ Asignación de sesión con rol específico.
  * Navegación por la plataforma $\rightarrow$ Filtrado de plantillas/vistas (*Templates*) acorde a los privilegios del usuario.
* **Flujo de Navegación:**
  * Los usuarios no autenticados (Visitantes) son redirigidos automáticamente al portal de inicio o autenticación.
  * Una vez autenticado, Django evalúa el rol del usuario y renderiza la interfaz correspondiente.

### 3. Diseño de Software / Arquitectura (*Software Design*)
Especifica la estructura global del software, los componentes principales y la selección del Stack Tecnológico.
* **Stack de Desarrollo:**
  * **Backend:** Python 3.11 + Django Framework.
  * **Frontend / Build Tool:** Vite.js + HTML5 / CSS3 / JavaScript.
  * **Contenerización:** Docker & Docker Compose para un entorno virtual.
  * **Base de Datos:** SQLite (Entorno de desarrollo local) / PostgreSQL (Preparado para producción).
* **Arquitectura de Software:**
  * Patrón MVT (*Model-View-Template*) propio de Django, desacoplando la lógica de datos, la lógica de negocio y la presentación visual.

### 4. Diseño de Módulos (*Module Design*)
Detalla la lógica interna, modelos de datos y componentes individuales de cada aplicación.
* **Módulo de Autenticación (`usuarios`):**
  * **Modelos:** Extensión del modelo `User` de Django para almacenar información de roles y perfil.
  * **Vistas (`views.py`):** Manejo de formularios de registro, inicio de sesión y redirección basada en roles (`@login_required`, decoradores de permisos).
  * **Rutas (`urls.py`):** Mapeo limpio de endpoints de autenticación y navegación.
* **Configuración del Panel de Administración (`admin.py`):**
  * Personalización del panel Django Admin para gestionar tablas, usuarios y roles de manera visual.

### 5. Punto de Inflexión: Codificación (*Coding*)
El momento de transición donde las especificaciones teóricas se convierten en código fuente ejecutable.
* **Acciones Realizadas:**
  1. Configuración de contenedores en Docker (`Dockerfile` y `docker-compose.yml`).
  2. Inicialización del repositorio de Git y subida a GitHub.
  3. Instalación de Django y librerías base (`requirements.txt`).
  4. Creación del proyecto Django y la app `usuarios`.
  5. Configuración de plantillas base (*Templates*) con soporte para roles.

---

## 🧪 Correlación con la Rama Ascendente (Fases de Pruebas)
Aunque se trabaje con la rama descendente (fase de diseño y codificación) es de suma importancia destacar que la fortaleza de la Metodología en V radica en su correlación directa con la rama ascendente (fase de pruebas y validación):

1. **Pruebas Unitarias (*Unit Testing*):** Corresponden al *Diseño de Módulos*. Verifican que cada función, vista o algoritmo individual funcione correctamente.
2. **Pruebas de Integración (*Integration Testing*):** Corresponden al *Diseño de Arquitectura*. Aseguran que la comunicación entre Django, la base de datos y Vite.js sea estable.
3. **Pruebas del Sistema (*System Testing*):** Corresponden al *Análisis del Sistema*. Validan que la aplicación cumpla con los flujos de trabajo globales y el control de roles.
4. **Pruebas de Aceptación y Validación (*Acceptance Testing & Validation*):** Corresponden al *Análisis de Requisitos*. Es el punto crucial donde se valida con el usuario/profesor que el producto final cumple con las necesidades reales planteadas al inicio del proyecto.
