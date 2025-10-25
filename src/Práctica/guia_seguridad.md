# Guía Seguridad

## Protocolos y Herramientas de Seguridad

### Ejercicio 1
¿Qué protocolos o herramientas de seguridad se pueden utilizar para superar los siguientes desafíos?

a. Garantizar la integridad del mensaje.  
b. Autenticación mutua.  
c. Suplantación de identidad.  
d. Ataques de replicación.  
e. Gestionar eficientemente las claves secretas compartidas en sistemas grandes.  
f. Autenticidad de las claves públicas.  
g. No revelar información sensible antes de la autenticación de las partes.

### Respuesta
**a. Garantizar la integridad del mensaje**: comparar hashes

**b. Autenticación mutua**: challenge-response, KDC, criptografía de clave pública

**c. Suplantación de identidad**: MFA/2FA; tenés que tener alguna manera de asegurarle al sistema que sos vos.

**d. Ataques de replicación**: números de secuencia/nonce. Evito que el mensaje se pueda volver a enviar, o le doy una validez al mensaje. También se pueden usar claves de sesión, porque duran un tiempo limitado.

**e. Gestionar eficientemente las claves secretas compartidas en sistemas grandes**: KDC

**f. Autenticidad de las claves públicas**: se utiliza una infraestructura de clave pública (PKI) donde las claves públicas son firmadas por una autoridad certificadora (CA) confiable mediante certificados digitales. Así, los usuarios pueden verificar que una clave pública realmente pertenece a quien dice ser su dueño.

**g. No revelar información sensible antes de la autenticación de las partes**: autenticar primero, o también usar criptografía de clave pública.
- En esta última no te tenés que asegurar de que estas hablando con X, sino que directamente cifrás con su clave pública; lo va a poder descifrar esa persona y nadie más.
  - Es débil ante ataques de suplantación de identidad

## Claves de Sesión

### Ejercicio 2
¿Por qué se usan claves de sesión? ¿Qué beneficios tiene?

### Respuesta
Se usan solo durante el tiempo de vida del canal; cuando termina, se destruyen. Se usan en casos donde se quiere dar acceso durante un tiempo limitado a un recurso, tiempo después del cual es necesario volver a autenticarse.

## Políticas de Acceso

### Ejercicio 3
Identifique la política de acceso que aplica a cada escenario:

a. Un alumno crea un nuevo archivo con el informe de Física III. Por defecto, solo él puede leer y modificar el archivo. Decide otorgar permisos de lectura y escritura a todo su equipo y, además, da permiso de comentar a los profesores.

b. En un hospital, el acceso a los sistemas de información está estrictamente organizado. Un usuario con el perfil de "Médico" puede acceder a los historiales clínicos de los pacientes que tiene asignados, solicitar pruebas y ver sus resultados. Un usuario con el perfil de "Administrativo" puede acceder a la información de facturación de los pacientes y gestionar las citas, pero no puede ver los detalles clínicos del historial. Por último, un usuario con el perfil de "Director de Hospital" puede ver reportes estadísticos y de gestión, pero no tiene acceso a los historiales individuales de los pacientes.

c. En una agencia de seguridad nacional, todos los documentos y usuarios están clasificados con etiquetas de seguridad como "Público", "Confidencial", "Secreto" y "Top Secret". Un usuario con autorización "Secreto" puede acceder libremente a documentos clasificados como "Público" y "Confidencial", pero el sistema le denegará automáticamente el acceso a cualquier documento etiquetado como "Top Secret". Estas reglas son configuradas por un administrador central de seguridad y no pueden ser modificadas por los usuarios.

d. Una aplicación bancaria moderna implementa políticas de seguridad muy dinámicas. Por ejemplo, un cliente puede realizar transferencias de hasta 1.000 € desde su propia red Wi-Fi registrada y durante el horario diurno (9:00 a 20:00). Sin embargo, si el mismo cliente intenta realizar una transferencia de más de 500 € mientras está conectado a una red Wi-Fi pública en otro país, el sistema bloquea la operación y solicita una segunda forma de autenticación (ej. una llamada de confirmación). La política evalúa el rol del usuario (cliente), la ubicación, la seguridad de la red, la cantidad de la transacción y la hora del día antes de permitir o denegar la operación.

### Respuesta
a. DAC
b. RBAC
c. MAC
d. ABAC

## Firewalls y Gateways

### Ejercicio 4
¿Cuál es la principal diferencia entre un firewall de filtrado de paquetes y un gateway a nivel de aplicación? De un ejemplo de ambos.

### Respuesta
La diferencia principal es el criterio de elección:
- El de filtrado de paquetes elige según el contenido de los headers o del paquete en sí mismo
  - Ejemplo: un router que permite el tráfico HTTP por el puerto 80 para navegación web, pero bloquea el tráfico FTP por el puerto 21 para prevenir transferencias de archivos.
- El gateway a nivel de aplicación elige según el contenido del mensaje
  - Ejemplo: Un proxy HTTP como Squid actúa como gateway a nivel de aplicación, inspeccionando el contenido de las solicitudes y respuestas HTTP. Por ejemplo, puede bloquear descargas de archivos ejecutables o filtrar contenido web específico según el texto presente en la página.

## Sistemas de Detección de Intrusos

### Ejercicio 5
Busque ejemplos reales de mecanismos de Detection Intrusion Para signature-based Intrusion Detection Systems y Anomaly-based Intrusion Detection Systems

### Respuesta:

#### Signature-based Intrusion Detection Systems (IDS)

Los sistemas de detección basados en firmas identifican ataques conocidos comparando el tráfico de red o eventos del sistema con patrones predefinidos (firmas) de ataques conocidos.

**Ejemplos reales:**

1. **Snort** - Sistema de detección de intrusiones de código abierto más popular:
   - Detecta ataques como SQL injection, buffer overflows, y malware
   - Ejemplo de regla: `alert tcp any any -> any 80 (content:"GET /admin"; msg:"Admin access attempt";)`
   - Usado por empresas como Cisco, Sourcefire

2. **Suricata** - Motor de detección de intrusiones de alto rendimiento:
   - Detecta ataques DDoS, exploits, y malware
   - Utilizado por organizaciones gubernamentales y empresas
   - Soporte para protocolos como HTTP, DNS, TLS

3. **OSSEC** - Sistema de detección de intrusiones basado en host:
   - Monitorea logs del sistema, integridad de archivos
   - Detecta cambios no autorizados en archivos críticos
   - Usado en servidores web y sistemas críticos

4. **Cisco FirePOWER** - Solución empresarial:
   - Detecta malware, exploits, y ataques dirigidos
   - Integración con firewalls Cisco
   - Usado en redes corporativas grandes

#### Anomaly-based Intrusion Detection Systems (IDS)

Los sistemas de detección basados en anomalías identifican comportamientos inusuales comparando la actividad actual con un modelo de comportamiento "normal" establecido.

**Ejemplos reales:**

1. **IBM QRadar** - Plataforma de seguridad empresarial:
   - Utiliza machine learning para detectar anomalías
   - Detecta comportamientos inusuales en usuarios y sistemas
   - Usado por bancos y organizaciones financieras

2. **Splunk Enterprise Security** - Plataforma SIEM:
   - Análisis de comportamiento de usuarios (UEBA)
   - Detecta accesos anómalos, transferencias de datos inusuales
   - Usado por empresas Fortune 500

3. **Darktrace** - Inteligencia artificial para ciberseguridad:
   - Utiliza machine learning para detectar amenazas internas
   - Detecta comportamientos anómalos en tiempo real
   - Usado por organizaciones gubernamentales y empresas

4. **Vectra AI** - Detección de amenazas en tiempo real:
   - Análisis de comportamiento de red
   - Detecta ataques avanzados persistentes (APT)
   - Usado en infraestructuras críticas

5. **Microsoft Defender for Identity** - Protección de identidades:
   - Detecta movimientos laterales y escalación de privilegios
   - Análisis de comportamiento de usuarios
   - Integrado en ecosistemas Microsoft

**Diferencias clave:**
- **Signature-based**: Efectivo contra ataques conocidos, bajo falso positivo, requiere actualizaciones constantes
- **Anomaly-based**: Detecta ataques desconocidos, puede generar falsos positivos, requiere entrenamiento inicial
