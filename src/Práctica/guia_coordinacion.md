# Guía Coordinación
## Relojes lógicos
### Ejercicio 1
Explicar por qué los relojes de distintos procesos se desincronizan en un sistema distribuido.

#### Respuesta
De por sí, cada máquina tiene su propio reloj de hardware con un cuarzo que oscila a una cierta frecuencia, pero tiene su propio sesgo. Esto implica que, por más que 2 relojes iguales arranquen al mismo tiempo, se van a desfasar eventualmente.

Sumado a eso, al querer sincronizarlos con un protocolo como NTP, tenes latencia para comunicarte con el "servidor central que tiene la hora real", por lo que tenés que calcular un cierto offset y, nuevamente, podés caer en otro desfasaje.

### Ejercicio 2
Describir los problemas que puede generar esta desincronización en:
- **Orden de eventos**
- **Registro de logs**
- **Coordinación de acceso a recursos**

#### Respuesta
- **Orden de eventos**: justamente se puede desencadenar en perder el orden de los eventos entre los procesos que participan en un sistema distribuido, generando inconsistencias en los resultados obtenidos.
- **Registro de logs**: se puede perder la trazabilidad de los eventos, asegurando que 2 eventos que deberían precederse sucedieron a la misma hora, lo cual debería ser imposible.
- **Coordinación de acceso a recursos**: pueden haber condiciones de carrera en lo que a los accesos a recursos refiere.

### Ejercicio 3
Comparar Lamport clocks y vector clocks ¿Qué problema resuelven cada uno?

#### Respuesta
Lamport arregla el desfasaje y coordina los distintos relojes de todos los procesos que interactúan en un sistema. Se aseguran que el **tiempo en todos los relojes sea correcto**.

Los relojes de vectores ignoran por completo el tiempo y se concentran en **la precedencia de los diferentes eventos**, para poder determinar la causalidad de los eventos.

## Exclusión Mutua
### Ejercicio 1
Comparar los tres algoritmos de exclusión mutua vistos en clase:
- Centralizado
- Basado en token
- Ricart-Agrawala

Para cada algoritmo, analizar:
- Número de mensajes requeridos
- Tolerancia a fallas
- Latencia

#### Respuesta
- Centralizado
  - Se basa en que todos los nodos que quieren un recurso le piden acceso al nodo dueño del mismo
  - En principio, el **número de mensajes** es:
    - 1 de solicitud de acceso por parte del solicitante
    - 1 de respuesta por parte del dueño
      - En caso de ser positiva, le manda un OK/ACK y le da el acceso al recurso al solicitante
      - En caso de ser negativa, le dice "No bro, bancame" <img src="../assets/luigi_wait.png" height="40" width="40"/>
    - Depende cómo se piense/implemente, también puede estar el mensaje en el que el dueño le pregunta a quien tiene el acceso al recurso **si ya terminó de usarlo**.
      - Otra variante de este es que quien tiene el acceso **lo devuelva apenas termina**.
    - Entonces, decimos que es $O(1)$
  - En lo que a **tolerancia a fallas** refiere, es baja, dado que se genera un SPoF
  - La **latencia** debería ser baja porque la conexión es directa, es 1-1. Solicitante sólo se comunica con el dueño.
- Token-based
  - Hay un token dando vueltas y se va pasando de mano para determinar quién puede operar.
    - El **número de mensajes** es $ N $, siendo N la cantidad de nodos.
      - Si tengo 10 nodos (del 0 al 9 y suponiendo que los punteros son $0 \rightarrow 1 \rightarrow 2...$), el nodo 0 quiere un recurso y lo tiene el nodo 9 (peor caso), el token tiene que dar toda la vuelta.
      - 0 pide el token, le pregunta a 1, no lo tiene; 1 le pregunta a 2, no lo tiene... así hasta llegar al 9, que lo tiene, e inmediatamente se lo pasa al 0.
      - Contando, llegamos 
    - La **tolerancia a fallas** es baja, puesto que si se pierde el token hay que regenerarlo, y es difícil tanto de regenerar como de determinar quién lo tiene que tener al regenerarse.
    - La **latencia** es alta, puesto que potencialmente se tiene que pasar por todos los nodos.
- Ricart-Agrawala
  - Acá la movida es que cuando un proceso quiere acceder a un recurso, le manda un mensaje a **todos** los nodos (incluyéndose a sí mismo) diciendo "che, quiero el recurso en tal momento (timestamp)".
  - Cada nodo que recibe el mensaje tiene tres opciones:
    - Si no le interesa el recurso, responde OK de una.
    - Si ya está usando el recurso, encola el pedido y no responde nada hasta que lo libere.
    - Si también quiere el recurso pero todavía no lo tiene, compara timestamps: el que tenga el timestamp más chico (o, en caso de empate, el ID más bajo) gana. Si el mensaje entrante gana, responde OK; si no, lo encola.
  - El proceso recién puede acceder al recurso cuando recibió OK de todos los otros nodos.
  - En cuanto a **número de mensajes**, es bastante hablador: para cada acceso, cada proceso manda $N-1$ mensajes de pedido y recibe $N-1$ OKs, así que son $2(N-1)$ mensajes por acceso (sin contar los reintentos si hay empates o caídas).
  - **Tolerancia a fallas**: es baja, porque si un nodo se cae y no responde, el resto se queda esperando el OK y nadie accede al recurso. O sea, un nodo caído puede trabar todo el sistema.
  - **Latencia**: depende de la velocidad de respuesta de todos los nodos, pero en el mejor caso es baja porque apenas llegan los OKs ya podés entrar. En el peor caso, si hay muchos compitiendo o alguno lento, se puede hacer eterna la espera.

## Algoritmos de elección
### Ejercicio 1
Imagine un sistema de 7 nodos que eligen al coordinador usando un algoritmo bully. El nodo 7 deja de funcionar y tanto el nodo 1 y el 4 detectan en simultáneo esta situación. Listar todos los mensajes necesarios para encontrar al nuevo nodo coordinador.


#### Respuesta
> **Aclaraciones**: 
> - $S_1$ va a ser el proceso que siga los mensajes que se disparan a partir de que 1 detectó que se cayó 7, y $S_4$ va a seguir a 4.
> - $S_1$ y $S_4$ se ejecutarán en paralelo


- $S_1$
  - 1 le manda mensaje a 2 $\Longrightarrow$ 2 le responde OK.
  - 1 le manda mensaje a 3 $\Longrightarrow$ 3 le responde OK.
  - 1 le manda mensaje a 4 $\Longrightarrow$ 4 le responde OK.
  - 1 le manda mensaje a 5 $\Longrightarrow$ 5 le responde OK.
  - 1 le manda mensaje a 6 $\Longrightarrow$ 6 le responde OK.
  - **1 deja de enviar mensajes**.
  - 2 le manda mensaje a 3 $\Longrightarrow$ 3 le responde OK.
  - 2 le manda mensaje a 4 $\Longrightarrow$ 4 le responde OK.
  - 2 le manda mensaje a 5 $\Longrightarrow$ 5 le responde OK.
  - 2 le manda mensaje a 6 $\Longrightarrow$ 6 le responde OK.
  - **2 deja de enviar mensajes**.
  - 3 le manda mensaje a 4 $\Longrightarrow$ 4 le responde OK.
  - 3 le manda mensaje a 5 $\Longrightarrow$ 5 le responde OK.
  - 3 le manda mensaje a 6 $\Longrightarrow$ 6 le responde OK.
  - **3 deja de enviar mensajes**.
  - 4 le manda mensaje a 5 $\Longrightarrow$ 5 le responde OK.
  - 4 le manda mensaje a 6 $\Longrightarrow$ 6 le responde OK.
  - **4 deja de enviar mensajes**.
  - 5 le manda mensaje a 6 $\Longrightarrow$ 6 le responde OK.
  - **5 deja de enviar mensajes**.
  - 6 es el nuevo coordinador $\Longrightarrow$ **finaliza la elección**.
- $S_4$
  - 4 le manda mensaje a 5 $\Longrightarrow$ 5 le responde OK.
  - 4 le manda mensaje a 6 $\Longrightarrow$ 6 le responde OK.
  - **4 deja de enviar mensajes**.
  - 5 le manda mensaje a 6 $\Longrightarrow$ 6 le responde OK.
  - **5 deja de enviar mensajes**.
  - 6 es el nuevo coordinador $\Longrightarrow$ **finaliza la elección**.


### Ejercicio 2
Explicar por qué la detección de fallos (saber si un coordinador realmente cayó o solo está lento) es un problema difícil en sistemas distribuidos. ¿Qué se sacrifica si queremos siempre un coordinador disponible?


#### Respuesta
El querer detectar fallos en un sistema distribuido es difícil por el simple hecho de que, en principio, implicaría que todos los nodos se conozcan entre todos y que se comuniquen entre sí para poder determinar el estado del sistema.

Si se lo quiere pensar como un _grafo_, se requeriría tener un grafo completo no dirigido de conexiones. Si $N$ es la cantidad de nodos, requeriría $\frac{N(N-1)}{2}$ conexiones/vías de comunicación distintas, lo cual resultaría muy costoso.

Dicho eso, podemos decir que, si queremos un coordinador disponible siempre, tenemos que **sacrificar el rendimiento del sistema**, teniendo una latencia alta.

### Ejercicio 3
Comparar el algoritmo de elección de coordinador basado en anillos con el algoritmo bully: ¿qué diferencias hay en número de mensajes y tolerancia a fallas?

- **Basado en anillos**: un nodo detecta que se cayó el coordinador y inicia una votación, pasando un arreglo con su ID. Pega la vuelta con cada uno appendeando su ID al arreglo y, cuando vuelve a quien arrancó la votación, este comparte un mensaje con el ID del coordinador (el más grande). 
  - **Número de mensajes**: El caso normal implica $2N$ mensajes por cada votación.
    - El peor de los casos, en cambio, es en el cual todos los nodos (salvo el que se cayó, claramente) detectan que se cayó el coordinador. Por ende, se requerirían $2N^2$ mensajes.
  - **Tolerancia a fallas**: es alta por el hecho de que si se cae un nodo y no le responde, se le envía el mensaje de elección al próximo proceso que esté funcionando dentro del anillo. Si se cae el nodo que había salido ganador en el último mensaje (caso más borde), **se reinicia la votación**.
- **Bully**: le pregunto siempre a los nodos más grandes. Si no me responden gano la elección.
  - **Número de mensajes**: suponiendo el peor caso en el que tengo N nodos (del 0 a $N-1$) y la votación arranca desde 0, voy a tener:
    - 0 le manda a $1,2,3,...,N-1$ y todos le responden, implicando $2(N-1)$ mensajes
    - 1 le manda a $2,3,4,...,N-1$ y todos le responden, implicando $2(N-2)$ mensajes
    - 2 le manda a $3,4,5,...,N-1$ y todos le responden, implicando $2(N-3)$ mensajes
    - 3 le manda a $4,5,6,...,N-1$ y todos le responden, implicando $2(N-4)$ mensajes
    - ...
    - $N-2$ le manda a $N-1$ y todos le responden, implicando 2 mensajes
    - Con una cierta ecuación de recurrencia obtenida a partir de esta deducción, obtenemos que se define como:
      - $\displaystyle\sum_{i=0}^{N-2} 2 \cdot (N-1-i)$
    - Que, simplificando en una sola fórmula, sería $\boxed{N(N-1)}$
  - **Tolerancia a fallas**: es alta, por lo que dijimos antes. Si se cae un nodo coordinador, arranca una nueva votación y se define otro coordinador.
    - Si entra un nuevo nodo con ID más alto que el coordinador actual, se vota de vuelta.

## Precedencia de eventos
### Ejercicio 1
Dadas las siguientes marcas de tiempo vectorial de tres eventos distintos:
- Evento A: [2,1,0]
- Evento B: [1,2,0]
- Evento C: [2,2,1]

Responder y justificar:
1. ¿A y B son concurrentes, o uno precede al otro?
2. ¿Cuál es la relación entre C y A?
3. ¿Cuál es la relación entre C y B?

#### Respuesta
> Aclaración: las posiciones de los vectores de cada evento se definen como $X_i$, siendo X el nombre del evento e i el índice del mismo (para simplicidad lo vamos a hacer 0-based, siendo las posiciones posibles en este caso 0, 1 y 2)
1. ¿A y B son concurrentes, o uno precede al otro?
   1. A y B son **concurrentes**, porque $A_0 > B_0 \wedge B_1 > A_1$. No hay forma de determinar si uno ocurrió antes que el otro, por lo que decimos que son concurrentes.
2. ¿Cuál es la relación entre C y A?
   1. A **es precedente de** C y **_también puede ser causa_**, puesto que $A_0 = C_0 \wedge A_1 < C_1 \wedge A_2 < C_2$
3. ¿Cuál es la relación entre C y B?
   1. B **es precedente de** C y **_también puede ser causa_**, puesto que $B_0 < C_0 \wedge B_1 = C_1 \wedge B_2 < C_2$

> Si un evento A precede a otro evento B, decimos que **puede ser causa**, pero no asegurarlo porque no tenemos ninguna garantía de ello.\
> Que sea precedente quiere decir que pasa antes, nada más.