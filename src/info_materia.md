# Información de la materia

Docentes:
- Mariano Benitez
- Rodolfo Sumoza
- Tomás Najún
- Rodrigo Pazos
- David Túa

Hay parte práctica y parte teórica. La idea es llevar la práctica al día (?).

## ¿De qué vamos a hablar?
### Programas interconectados en la red
**Para qué se comunican?**
**Es necesario?**
- Por disponibilidad
- Por escalabilidad
  - Si un programa se vuelve muy pesado y consume muchos recursos, va a ser necesario volverlo distribuido.
- Por ubicación geográfica
## ¿Para qué armar una red?
Si es más fácil hacer todo en la misma compu, ¿para qué me voy a gastar en hacer una red?

Esencialmente, por 2 motivos:
- Por diseño/definición es distribuido
  - Red de bancos
  - Sensores / elementos de IoT
  - Aplicaciones móviles
Básicamente, cuando el problema es inherentemente distribuido, **no hay chance de juntarlo**.
Este motivo se llamará "Descentralizado", el cual es **necesario**.

- Porque no alcanza una sola computadora
  - No me alcanza la memoria, CPU, etc.
  - No se puede apagar nunca
  - Tiene que ser muy rápido
Básicamente, cuando tengo requerimientos que me obligan a usar más de una computadora.
A esto le vamos a decir "Distribuido", el cual es un motivo **suficiente**.

## ¡Los sistemas distribuidos son complejos!
Cuando hay más cosas que se pueden romper, se agrega muchísima complejidad. Uno tiene que estar preparado para que las cosas se rompan.

Justamente, en un sistema distribuido es mucho más complejo porque tiene muchos componentes.

### Te pueden pasar mil cosas
- Se rompe la computadora
- No se sabe con quién se tiene que comunicar
- No se ponen de acuerdo
- Se corta la comunicación
- Se pierden los bits
- Pueden venir intrusos
  - Atacantes, por ejemplo
- Obvio, hay bugs en el código
Entre otras cosas...

Si no se controlan estas cosas: ¿La gente podría confiar en el sistema?
Si no se confía en el sistema, no sirve para nada.

El principal desafío de los sistemas distribuidos es hacerlos **confiables**.

## Cómo sabemos todo esto?
- Del libro de **Tanenbaum**.
  - Es un bodrio de leer, en la materia se tratan de bajar las ideas principales del mismo.

## ¿Qué pasa en un sistema distribuido?
-  Hay procesos.
-  Que se comunican.
-  Que se coordinan entre sí.
-  Que necesitan encontrarse.
-  Que comparten información.
-  Que se prenden, apagan y rompen.
-  Que se defienden ante amenazas.

## Enfoque de la materia
**La realidad**:
- Son una banda de temas y muy complejos y amplios
- Se puede ir en mucho detalle en cada punto (profundidad)
- Los problemas y las soluciones cambian todo el tiempo
- Pero las bases siguen siendo las mismas
- Se usa en el trabajo de todo ingeniero de software

Entonces como ingenieros, **¿qué es lo importante?**
- Tener un conocimiento de las bases que forman un sistema distribuido
- Analizar un sistema y reconocer sus capacidades y limitaciones
- Proponer soluciones en forma objetiva y clara

Un buen diseño de un sistema distribuido (qué pasa cuando se rompe, cómo encaro temas de escalabilidad, etc.) logra que no tengas que hacer cambios de arquitectura grandes en caso de la necesidad de un cambio.

**¿Qué se llevan al final de la materia?**
- Conocimientos de los aspectos de los sistemas distribuidos
- Entendimiento de las características y el impacto de cada aspecto
- Habilidades básicas para analizar y evaluar problemas y soluciones

**¿Qué no se llevan?**
- Conocimiento profundo de alguna solución (ej: Kubernetes)

**¿Qué capacidades necesitan traer?**
- Analizar información y situaciones complejas
- Presentar alternativas de forma objetiva
- Tener pensamiento crítico, en resumen.

**Teoría (70% de la cursada)**
- Foco en los conceptos
- Problemas y características
- Bajada a tierra del libro

**Práctica (30% de la cursada)**
- Foco en las habilidades
- Analizar situaciones
- Presentación de propuestas

**De parte de que aprenden**
- Lean los capítulos después de la clase
- Consultas en la siguiente

## Evaluaciones
2 parciales, 11 de septiembre y 30 de octubre
Recus: 6 y 11 de noviembre

**2 TPs**
- _Entrega TP1_: 18 de septiembre
- _Entrega TP2_: 6 de noviembre