# 🚀 Sistema Web Integral - Módulo de Gestión y Autenticación

> **Subproyecto:** Desarrollo de Aplicaciones  
> **Estudiante:** Luigi Henri Arismendi Toro  
> **Institución:** Universidad Nacional Experimental de los Llanos Occidentales "Ezequiel Zamora" (UNELLEZ)  

---

## 📌 Contexto y Propósito del Sistema
Este repositorio contiene la arquitectura base y el despliegue inicial de un sistema web escalable. El desarrollo se rige bajo los estándares de la **Metodología en V**, garantizando la trazabilidad estricta entre el diseño conceptual, la arquitectura técnica y la codificación modular.

---

## 📊 Arquitectura Global: Modelo en V (Diseño y Validación)

```mermaid
graph TD
    %% Estructura Principal en V
    subgraph Rama_Descendente ["Rama Descendente: Diseño y Verificación"]
        A[1. Análisis de Requisitos] --> B[2. Análisis del Sistema]
        B --> C[3. Diseño de Arquitectura MVT]
        C --> D[4. Diseño de Módulos]
        D --> E[5. Punto de Inflexión: Codificación Base]
    end

    subgraph Rama_Ascendente ["Rama Ascendente: Pruebas y Validación"]
        E --> F[6. Pruebas Unitarias - Módulos]
        F --> G[7. Pruebas de Integración - Django/DB]
        G --> H[8. Pruebas de Sistema - Flujos y Roles]
        H --> I[9. Pruebas de Aceptación - Validación Final]
    end

    %% Estilos Profesionales
    style A fill:#1f77b4,stroke:#fff,stroke-width:2px,color:#fff
    style B fill:#2ca02c,stroke:#fff,stroke-width:2px,color:#fff
    style C fill:#ff7f0e,stroke:#fff,stroke-width:2px,color:#fff
    style D fill:#9467bd,stroke:#fff,stroke-width:2px,color:#fff
    style E fill:#d62728,stroke:#fff,stroke-width:2px,color:#fff
    style F fill:#17becf,stroke:#fff,stroke-width:2px,color:#fff
    style G fill:#bcbd22,stroke:#fff,stroke-width:2px,color:#fff
    style H fill:#e377c2,stroke:#fff,stroke-width:2px,color:#fff
    style I fill:#8c564b,stroke:#fff,stroke-width:2px,color:#fff
