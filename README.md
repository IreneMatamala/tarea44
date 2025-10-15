# Práctica DevSecOps - tarea44

Este repositorio implementa prácticas de DevSecOps integrando seguridad en el pipeline CI/CD.

## Herramientas implementadas

1. **Gitleaks**: Detección de secretos en el código
2. **Trivy**: Escaneo de vulnerabilidades en imágenes Docker
3. **Azure Key Vault**: Gestión segura de secretos
4. **Docker Security**: Mejores prácticas de seguridad en contenedores

## Estructura

- `.github/workflows/devsecops.yml`: Pipeline de CI/CD con seguridad
- `.gitleaks.toml`: Configuración de detección de secrets
- `Dockerfile`: Contenedor seguro con usuario no-root
- `app/`: Aplicación Python con integración Azure Key Vault

## Cómo usar

1. Clonar el repositorio
2. Configurar Azure Key Vault
3. Ejecutar el pipeline mediante push a main
