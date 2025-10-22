# Guía de Instalación

Esta guía te va a ayudar a configurar el entorno de desarrollo necesario para trabajar con este repositorio de Sistemas Distribuidos.

## Instalación de Dependencias

### 1. Rust (Requerido para mdBook)

#### En Linux/macOS:
```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source ~/.cargo/env
```

#### En Windows (PowerShell):
```powershell
Invoke-WebRequest -Uri https://win.rustup.rs/x86_64 -OutFile rustup-init.exe
.\rustup-init.exe
```

#### Verificar instalación:
```bash
rustc --version
cargo --version
```

### 2. mdBook

```bash
cargo install mdbook
```

#### Verificar instalación:
```bash
mdbook --version
```

### 3. mdbook-katex (Plugin para fórmulas matemáticas)

```bash
cargo install mdbook-katex
```

#### Verificar instalación:
```bash
mdbook-katex --version
```

## Configuración del Proyecto

### 1. Clonar el repositorio
```bash
git clone <url-del-repositorio>
cd distributed-systems
```

### 2. Configurar template de commit
```bash
git config commit.template .gitmessage
```

### 3. Verificar configuración
```bash
# Verificar que mdBook funciona
mdbook build

# Verificar que el plugin katex funciona
mdbook-katex --help
```

## Comandos Útiles

### Desarrollo
```bash
# Servir el libro en modo desarrollo (con hot-reload)
mdbook serve

# Construir el libro
mdbook build

# Limpiar archivos generados
mdbook clean
```

### Estructura de archivos generados
```
book/                    # Archivos HTML generados
├── index.html          # Página principal
├── assets/             # Recursos estáticos
└── ...
```

## Solución de Problemas

### Error: "mdbook: command not found"
- Asegurate de que Rust esté instalado correctamente
- Verificá que `~/.cargo/bin` esté en tu PATH
- Reiniciá tu terminal después de la instalación

### Error: "mdbook-katex: command not found"
- Instalá mdbook-katex: `cargo install mdbook-katex`
- Verificá que esté en el PATH: `which mdbook-katex`

### Error de permisos en Linux/macOS
```bash
# Dar permisos de ejecución si es necesario
chmod +x ~/.cargo/bin/mdbook
chmod +x ~/.cargo/bin/mdbook-katex
```

### Problemas con fórmulas matemáticas
- Asegurate de que mdbook-katex esté instalado
- Verificá que las fórmulas estén en formato LaTeX correcto
- Revisá la configuración en `book.toml`

## Configuración Avanzada

### Variables de entorno (opcional)
```bash
# Agregar al ~/.bashrc o ~/.zshrc
export PATH="$HOME/.cargo/bin:$PATH"
```

### Configuración de mdBook
El archivo `book.toml` contiene la configuración del libro. Las opciones principales incluyen:

```toml
[book]
title = "Sistemas Distribuidos"
authors = ["Francisco Calveyra"]
language = "es"

[output.html]
default-theme = "light"
preferred-dark-theme = "navy"

[preprocessor.katex]
```

## Verificación Final

Para verificar que todo está funcionando correctamente:

1. **Construir el libro**:
   ```bash
   mdbook build
   ```

2. **Servir en modo desarrollo**:
   ```bash
   mdbook serve
   ```

3. **Abrir en el navegador**: http://localhost:3000

4. **Verificar fórmulas matemáticas**: Buscá páginas con ecuaciones LaTeX

## Recursos Adicionales

- [Documentación oficial de mdBook](https://rust-lang.github.io/mdBook/)
- [mdbook-katex plugin](https://github.com/lzanini/mdbook-katex)
- [Rust installation guide](https://doc.rust-lang.org/book/ch01-01-installation.html)

---

Si encontrás problemas durante la instalación, no dudes en crear un issue en el repositorio.
