# Sistemas Distribuidos - Universidad Austral

> Apuntes completos de la materia Sistemas Distribuidos, Universidad Austral, año 2025

## Sobre este repositorio

Este repositorio contiene mis apuntes y material de estudio de la materia **Sistemas Distribuidos** de la Universidad Austral, cursada durante el año 2025. El contenido está organizado de manera estructurada para facilitar el estudio y la comprensión de los conceptos fundamentales de los sistemas distribuidos.

## Contenido

### Teoría
- **Introducción**: Conceptos básicos y fundamentos
- **Comunicación**: Protocolos, middleware y comunicación entre procesos
- **Coordinación**: Algoritmos de consenso, relojes lógicos y sincronización
- **Naming**: Sistemas de nombres, DNS y resolución de direcciones
- **Consistencia y Replicación**: Modelos de consistencia y estrategias de replicación
- **Tolerancia a Fallos**: Redundancia, recuperación y sistemas resilientes
- **Seguridad**: Autenticación, autorización y protocolos de seguridad

### Práctica
- **Guías de ejercicios** organizadas por tema
- **Trabajos Prácticos** con implementaciones prácticas
- **Exámenes anteriores** para práctica adicional

### Estructura del repositorio

```
src/
├── introduccion.md          # Conceptos básicos
├── clase_2.md              # Fundamentos teóricos
├── clase_3.md              # Comunicación
├── coordinacion.md         # Algoritmos de coordinación
├── naming.md              # Sistemas de nombres
├── replicacion.md         # Consistencia y replicación
├── tolerancia.md          # Tolerancia a fallos
├── seguridad.md           # Seguridad en sistemas distribuidos
├── Práctica/             # Guías de ejercicios
│   ├── guia_intro.md
│   ├── guia_comunicacion.md
│   ├── guia_coordinacion.md
│   ├── guia_naming.md
│   ├── guia_consistencia_replicacion.md
│   ├── guia_tolerancia.md
│   └── guia_seguridad.md
└── tps/                   # Trabajos prácticos
    └── tp_1.md
```

## Cómo usar este repositorio

### Para estudiar
1. **Teoría**: Comienza con `introduccion.md` y sigue el orden lógico de los temas
2. **Práctica**: Utiliza las guías en `Práctica/` para ejercitar cada tema
3. **Evaluación**: Revisa los exámenes anteriores en `Práctica/parciales_viejos/`

### Para contribuir
- Si encontrás errores o mejoras, no dudes en crear un issue/pull request
- Las correcciones y mejoras son bienvenidas
- **Configuración de commit template**: Configurá `.gitmessage` como template de commit:
  ```bash
  git config commit.template .gitmessage
  ```
- **Requisitos de desarrollo**: Ver [docs/INSTALL.md](docs/INSTALL.md) para los requisitos de instalación (mdBook, mdbook-katex, Rust)

## Temas principales

### Comunicación
- Middleware y message brokers
- Protocolos de comunicación
- RPC y gRPC
- Multicasting

### Coordinación
- Algoritmos de consenso (Paxos, Raft)
- Relojes lógicos (Lamport, Vector)
- Sincronización de procesos

### Naming
- Sistemas de nombres planos vs estructurados
- DNS y resolución de nombres
- Servicios de directorio

### Consistencia y Replicación
- Modelos de consistencia (CAP Theorem)
- Estrategias de replicación
- Consistencia eventual

### Tolerancia a Fallos
- Redundancia y recuperación
- Checkpointing y logging
- Sistemas resilientes

### Seguridad
- Autenticación y autorización
- Criptografía y protocolos seguros
- Políticas de acceso

## Notas importantes

- Este material está en constante actualización
- Los apuntes reflejan el contenido de las clases del 2025
- Incluye ejemplos prácticos y ejercicios resueltos
- Compatible con mdBook para generación de documentación

---

**Autor**: Francisco Calveyra  
**Materia**: Sistemas Distribuidos  
**Universidad**: Universidad Austral  
**Año**: 2025
