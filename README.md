# Aplicación Web - Metodología de Desarrollo en V

Proyecto web desarrollado siguiendo las fases iniciales de la metodología en V solicitada.

---

## 📊 Infografía: Rama Descendente (Fase de Verificación)

```mermaid
graph TD
    A[Análisis de Requisitos] --> B[Análisis del Sistema]
    B --> C[Diseño de Software / Arquitectura]
    C --> D[Diseño de Módulos]
    D --> E[Punto de Inflexión: Codificación]

    style A fill:#3498db,stroke:#2980b9,stroke-width:2px,color:#fff
    style B fill:#2ecc71,stroke:#27ae60,stroke-width:2px,color:#fff
    style C fill:#f1c40f,stroke:#f39c12,stroke-width:2px,color:#fff
    style D fill:#9b59b6,stroke:#8e44ad,stroke-width:2px,color:#fff
    style E fill:#e74c3c,stroke:#c0392b,stroke-width:2px,color:#fff
```

---

## 🔽 Fases Descendentes de la Metodología

1. **Análisis de Requisitos (Requirement Gathering):** 
   * Definición de las necesidades del usuario y funcionalidades requeridas en el sistema.
2. **Análisis del Sistema (System Analysis):** 
   * Especificación del comportamiento general del software y la arquitectura funcional.
3. **Diseño de Software / Arquitectura (Software Design):** 
   * Definición de los componentes principales, interfaces y el stack tecnológico (Python, Django, Vite.js, Docker).
4. **Diseño de Módulos (Module Design):** 
   * Detalle de la lógica interna, algoritmos y modelo de datos para cada módulo.
5. **Punto de Inflexión: Codificación (Coding):** 
   * Construcción del código fuente y desarrollo efectivo del proyecto.

---

## 👥 Roles y Niveles de Acceso
- **Administrador:** Gestión total desde el panel Django Admin (`/admin`).
- **Gestor:** Administración de datos operativos y reportes.
- **Usuario:** Acceso a vistas privadas de usuario registrado.
- **Visitante:** Acceso a landing pública, login y registro.
