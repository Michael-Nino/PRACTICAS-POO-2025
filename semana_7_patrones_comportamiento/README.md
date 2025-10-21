# Semana 7: Patrones de Diseño de Comportamiento

## 📚 Patrones Estudiados
- **Observer**
- **Strategy**
- **Command**

## 📄 Informe LaTeX
**Ver informe completo:** [Overleaf - Semana 7](https://es.overleaf.com/read/mtmvdcdmszwv#c2455a)

---

## 📂 Estructura de Carpetas

```
semana_7_patrones_comportamiento/
├── codigo_ejemplos/
├── desarrollo/
├── trabajo_investigacion/
└── resultados/
```

---

## 💡 Código de Ejemplos

Ejemplos extraídos directamente del material del curso (PDF).

### Observer
- **`ejemplo1_observer.cpp`** - Sistema de notificaciones uno-a-muchos
- **`ejemplo1_observer.py`** - Observadores suscritos a cambios de estado

**Características:**
- Interfaz `Observer` con método `actualizar()`
- Clase `Sujeto` que mantiene lista de observadores
- Notificación automática cuando cambia el estado
- Desacoplamiento entre sujeto y observadores

**Uso:**
```cpp
Sujeto* sujeto = new Sujeto();
Observer* obs1 = new ObservadorConcreto("Obs1");
sujeto->agregarObservador(obs1);
sujeto->setEstado("Nuevo estado"); // Notifica a obs1
```

### Strategy
- **`ejemplo2_strategy.cpp`** - Familia de algoritmos intercambiables
- **`ejemplo2_strategy.py`** - Estrategias de cálculo diferentes

**Características:**
- Interfaz `Estrategia` con método `ejecutar()`
- Múltiples implementaciones de algoritmos
- Cambio de estrategia en tiempo de ejecución
- Eliminación de condicionales complejos

**Uso:**
```cpp
Contexto* ctx = new Contexto(new EstrategiaA());
ctx->ejecutarEstrategia(); // Usa EstrategiaA

ctx->setEstrategia(new EstrategiaB());
ctx->ejecutarEstrategia(); // Usa EstrategiaB
```

### Command
- **`ejemplo3_command.cpp`** - Encapsulación de peticiones como objetos
- **`ejemplo3_command.py`** - Comandos con soporte para undo

**Características:**
- Interfaz `Comando` con métodos `ejecutar()` y `deshacer()`
- Clase `Invocador` que ejecuta comandos
- Clase `Receptor` que realiza las operaciones
- Historial de comandos para undo/redo

**Uso:**
```cpp
Receptor* receptor = new Receptor();
Comando* cmd = new ComandoConcreto(receptor);
Invocador* inv = new Invocador();
inv->setComando(cmd);
inv->presionarBoton(); // Ejecuta comando
```

---

## 🔨 Desarrollo (Ejercicios Prácticos)

Ejercicios completamente diferentes a los ejemplos del PDF.

### Desarrollo 1: Sistema de Chat (Observer)
- **`desarrollo1_observer_chat.cpp`**
- **`desarrollo1_observer_chat.py`**

**Descripción:**
Sistema de chat en tiempo real donde múltiples usuarios reciben notificaciones cuando alguien envía un mensaje a la sala.

**Funcionalidades:**
- Clase `SalaChat` como Subject observable
- Clase `Usuario` como Observer
- Métodos: `agregarUsuario()`, `eliminarUsuario()`, `enviarMensaje()`
- Notificación broadcast a todos los usuarios conectados

**Ejemplo de uso:**
```cpp
SalaChat* sala = new SalaChat("General");
Usuario* alice = new Usuario("Alice");
Usuario* bob = new Usuario("Bob");

sala->agregarUsuario(alice);
sala->agregarUsuario(bob);

sala->enviarMensaje("Alice", "Hola a todos!");
// Salida:
// [Bob] recibió: Alice: Hola a todos!
```

**Casos de uso:**
- Aplicaciones de mensajería
- Sistemas de notificaciones
- Actualizaciones en tiempo real
- Broadcasting de eventos

### Desarrollo 2: Algoritmos de Ordenamiento (Strategy)
- **`desarrollo2_strategy_ordenamiento.cpp`**
- **`desarrollo2_strategy_ordenamiento.py`**

**Descripción:**
Sistema que permite cambiar dinámicamente el algoritmo de ordenamiento (Burbuja, Selección, Inserción) según las necesidades.

**Funcionalidades:**
- Interfaz `EstrategiaOrdenamiento` con método `ordenar()`
- Implementaciones: `OrdenamientoBurbuja`, `OrdenamientoSeleccion`, `OrdenamientoInsercion`
- Clase `Ordenador` que usa la estrategia seleccionada
- Medición de tiempo de ejecución

**Ejemplo:**
```python
ordenador = Ordenador()
datos = [64, 34, 25, 12, 22, 11, 90]

ordenador.set_estrategia(OrdenamientoBurbuja())
ordenador.ordenar(datos)  # Usa Burbuja

ordenador.set_estrategia(OrdenamientoSeleccion())
ordenador.ordenar(datos)  # Usa Selección
```

**Algoritmos implementados:**
- **Burbuja**: O(n²) - Simple pero ineficiente
- **Selección**: O(n²) - Menos intercambios que burbuja
- **Inserción**: O(n²) - Eficiente para datos casi ordenados

**Comparación de rendimiento:**
| Algoritmo | Datos pequeños | Datos grandes | Datos ordenados |
|-----------|----------------|---------------|-----------------|
| Burbuja | Aceptable | Lento | Lento |
| Selección | Aceptable | Lento | Lento |
| Inserción | Rápido | Lento | Muy rápido |

### Desarrollo 3: Editor de Texto con Undo (Command)
- **`desarrollo3_command_editor.cpp`**
- **`desarrollo3_command_editor.py`**

**Descripción:**
Editor de texto simple con capacidad de deshacer operaciones usando el patrón Command.

**Funcionalidades:**
- Clase `Editor` como Receiver con contenido de texto
- Comandos: `ComandoEscribir`, `ComandoBorrar`
- Clase `GestorComandos` como Invoker con historial
- Operaciones reversibles (undo)

**Ejemplo:**
```cpp
Editor* editor = new Editor();
GestorComandos* gestor = new GestorComandos();

Comando* cmd1 = new ComandoEscribir(editor, "Hola ");
gestor->ejecutar(cmd1);

Comando* cmd2 = new ComandoEscribir(editor, "mundo");
gestor->ejecutar(cmd2);

cout << editor->getContenido(); // "Hola mundo"

gestor->deshacer(); // Elimina "mundo"
cout << editor->getContenido(); // "Hola "
```

**Operaciones soportadas:**
- `escribir(texto)`: Añade texto al final
- `borrar(n)`: Borra n caracteres del final
- `deshacer()`: Revierte última operación
- `mostrar()`: Muestra contenido actual

**Historial:**
```
Operación 1: Escribir "Hola "
Operación 2: Escribir "mundo"
Operación 3: Borrar 5
[Undo] -> Vuelve a Operación 2
```

---

## 🔍 Trabajo de Investigación

**Archivo:** `investigacion_frameworks.md`

**Contenido:**
- **Android LiveData**: Implementación de Observer para UI reactiva
- **RxJava/RxJS**: Programación reactiva con Observables
- **Vue.js**: Sistema de reactividad basado en Observer
- **Spring Framework**: Estrategias de transacciones y autenticación
- **Redux**: Actions como comandos que modifican estado
- **Git**: Comandos como objetos ejecutables

**Frameworks analizados:**
1. Android (Java/Kotlin)
2. RxJava/RxJS (Reactive Extensions)
3. Vue.js (JavaScript)
4. Spring Framework (Java)
5. Redux (JavaScript)
6. Passport.js (Node.js)

**Casos prácticos:**
- LiveData observa cambios en datos y actualiza UI
- RxJava transforma streams de eventos
- Redux ejecuta actions para cambiar estado
- Spring usa Strategy para diferentes tipos de transacciones

---

## 📊 Resultados

### Informe LaTeX
**Archivo:** `informe_patrones_comportamiento.tex`

**Contenido:**
- Marco teórico de patrones de comportamiento
- Implementaciones detalladas en C++ y Python
- Desarrollo de ejercicios explicado
- Análisis comparativo de lenguajes
- Aplicaciones en frameworks reales
- Ventajas y desventajas de cada patrón
- Resultados y conclusiones

### Diagramas UML
**Carpeta:** `resultados/diagramas_UML/`

**Archivos:**
- `observer.puml` - Diagrama UML del patrón Observer
- `strategy.puml` - Diagrama UML del patrón Strategy
- `command.puml` - Diagrama UML del patrón Command
- `README.md` - Guía para visualizar diagramas

**Ver diagramas:** [README de Diagramas UML](./resultados/diagramas_UML/README.md)

---

## 🚀 Cómo Ejecutar

### C++
```bash
# Compilar ejemplos
g++ -std=c++11 codigo_ejemplos/ejemplo1_observer.cpp -o observer
g++ -std=c++11 codigo_ejemplos/ejemplo2_strategy.cpp -o strategy
g++ -std=c++11 codigo_ejemplos/ejemplo3_command.cpp -o command

# Compilar desarrollos
g++ -std=c++11 desarrollo/desarrollo1_observer_chat.cpp -o chat
g++ -std=c++11 desarrollo/desarrollo2_strategy_ordenamiento.cpp -o sort
g++ -std=c++11 desarrollo/desarrollo3_command_editor.cpp -o editor

# Ejecutar
./observer
./chat
./sort
./editor
```

### Python
```bash
# Ejecutar ejemplos
python3 codigo_ejemplos/ejemplo1_observer.py
python3 codigo_ejemplos/ejemplo2_strategy.py
python3 codigo_ejemplos/ejemplo3_command.py

# Ejecutar desarrollos
python3 desarrollo/desarrollo1_observer_chat.py
python3 desarrollo/desarrollo2_strategy_ordenamiento.py
python3 desarrollo/desarrollo3_command_editor.py
```

---

## 📈 Comparación C++ vs Python

| Aspecto | C++ | Python |
|---------|-----|--------|
| **Observer** | Lista de punteros a observers | Lista dinámica de objetos |
| **Strategy** | Punteros a estrategias | Referencias o duck typing |
| **Command** | Historial con vectores | Historial con listas |
| **Polimorfismo** | Funciones virtuales | Duck typing o ABC |
| **Memoria** | Gestión manual (new/delete) | Garbage collection |
| **Interfaces** | Clases abstractas puras | ABC o protocolos |
| **Rendimiento** | Alto (compilado) | Moderado (interpretado) |

---

## 🎯 Aprendizajes Clave

1. **Observer** establece relación uno-a-muchos para notificaciones automáticas
2. **Strategy** permite cambiar algoritmos en tiempo de ejecución
3. **Command** encapsula peticiones como objetos para undo/redo
4. Los patrones de comportamiento se enfocan en la comunicación entre objetos
5. Desacoplar responsabilidades mejora la flexibilidad del sistema
6. Python ofrece implementaciones más concisas
7. C++ proporciona mayor control sobre rendimiento y memoria

---

## 🌟 Casos de Uso Reales

### Observer
- **UI Frameworks**: Actualización automática de vistas
- **Sistemas de eventos**: Notificaciones push
- **Pub/Sub**: Mensajería entre componentes
- **Reactive Programming**: RxJava, RxJS, Vue.js

### Strategy
- **Algoritmos**: Ordenamiento, búsqueda, compresión
- **Autenticación**: Diferentes métodos de login
- **Pagos**: Múltiples procesadores de pago
- **Validación**: Diferentes reglas de validación

### Command
- **Editores**: Undo/redo de operaciones
- **Transacciones**: Commits y rollbacks
- **Macros**: Secuencias de comandos
- **Queue systems**: Ejecución asíncrona

---

## 💡 Ventajas y Desventajas

### Observer
**Ventajas:**
- Desacoplamiento entre sujeto y observadores
- Soporte para broadcast
- Fácil añadir nuevos observadores

**Desventajas:**
- Orden de notificación no garantizado
- Posibles problemas de rendimiento
- Debugging complejo

### Strategy
**Ventajas:**
- Algoritmos intercambiables
- Elimina condicionales
- Fácil testing

**Desventajas:**
- Cliente debe conocer estrategias
- Más clases en el sistema
- Overhead de comunicación

### Command
**Ventajas:**
- Desacoplamiento invocador-receptor
- Undo/redo fácil de implementar
- Cola de comandos

**Desventajas:**
- Más clases
- Complejidad en sistemas simples
- Consumo de memoria en historial

---

## 📚 Referencias

- Gamma, E. et al. (1994). Design Patterns: Elements of Reusable Object-Oriented Software
- [Refactoring Guru - Behavioral Patterns](https://refactoring.guru/design-patterns/behavioral-patterns)
- Android Developers - LiveData: https://developer.android.com/topic/libraries/architecture/livedata
- RxJava Documentation: https://github.com/ReactiveX/RxJava
- Redux Documentation: https://redux.js.org
- Vue.js Reactivity: https://vuejs.org/guide/essentials/reactivity-fundamentals.html

---

**Universidad Nacional del Altiplano - 2025**
