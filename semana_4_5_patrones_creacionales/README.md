# Semana 4-5: Patrones de Diseño Creacionales

## 📚 Patrones Estudiados
- **Singleton**
- **Factory**
- **Builder**

## 📄 Informe LaTeX
**Ver informe completo:** [Overleaf - Semana 4-5](https://es.overleaf.com/read/szkscdncvspj#c0ab70)

---

## 📂 Estructura de Carpetas

```
semana_4_5_patrones_creacionales/
├── codigo_ejemplos/
├── desarrollo/
├── trabajo_investigacion/
└── resultados/
```

---

## 💡 Código de Ejemplos

Ejemplos extraídos directamente del material del curso (PDF).

### Singleton
- **`ejemplo1_singleton.cpp`** - Implementación en C++ de patrón Singleton con clase Config
- **`ejemplo1_singleton.py`** - Implementación en Python usando módulo para instancia única

**Características:**
- Constructor privado
- Instancia estática única
- Método `getInstance()` para acceso global
- Thread-safe en versión avanzada

**Uso:**
```cpp
Config* config = Config::getInstance();
config->set("database", "localhost");
```

### Factory
- **`ejemplo2_factory.cpp`** - Factory Method para crear objetos de transporte
- **`ejemplo2_factory.py`** - Factory con creación de Camión, Barco y Avión

**Características:**
- Interfaz común `Transporte`
- Clases concretas: `Camion`, `Barco`, `Avion`
- Método factory estático `crear(tipo)`
- Desacoplamiento entre creación y uso

**Uso:**
```cpp
Transporte* t = TransporteFactory::crear("camion");
t->entregar();
```

### Builder
- **`ejemplo3_builder.cpp`** - Constructor de objetos Computadora complejos
- **`ejemplo3_builder.py`** - Pattern Builder con interfaz fluida

**Características:**
- Construcción paso a paso
- Interfaz fluida (method chaining)
- Director opcional para construcciones predefinidas
- Separación de construcción y representación

**Uso:**
```cpp
Computadora* pc = ComputadoraBuilder()
    .setCPU("Intel i7")
    .setRAM(16)
    .build();
```

---

## 🔨 Desarrollo (Ejercicios Prácticos)

Ejercicios completamente diferentes a los ejemplos del PDF.

### Desarrollo 1: Sistema de Logger (Singleton)
- **`desarrollo1_singleton_logger.cpp`**
- **`desarrollo1_singleton_logger.py`**

**Descripción:**
Sistema de logging centralizado que garantiza una única instancia del logger en toda la aplicación.

**Funcionalidades:**
- Método `log(mensaje)` para registrar eventos
- Niveles: INFO, WARNING, ERROR
- Instancia única compartida
- Thread-safe con mutex (C++)

**Ejemplo de salida:**
```
[INFO] Aplicacion iniciada
[WARNING] Memoria baja
[ERROR] Fallo en conexion
```

### Desarrollo 2: Factory de Notificaciones
- **`desarrollo2_factory_notificaciones.cpp`**
- **`desarrollo2_factory_notificaciones.py`**

**Descripción:**
Sistema que crea diferentes tipos de notificaciones (Email, SMS, Push) según el canal requerido.

**Funcionalidades:**
- Interfaz `Notificacion` con método `enviar()`
- Implementaciones: `Email`, `SMS`, `Push`
- Factory para seleccionar tipo de notificación
- Envío polimórfico de mensajes

**Ejemplo de uso:**
```cpp
Notificacion* n = NotificacionFactory::crear("email");
n->enviar("Hola mundo");
// Salida: [Email] Enviando: Hola mundo
```

### Desarrollo 3: Builder de Documentos PDF
- **`desarrollo3_builder_pdf.cpp`**
- **`desarrollo3_builder_pdf.py`**

**Descripción:**
Constructor de documentos PDF complejos con múltiples secciones y configuraciones.

**Funcionalidades:**
- Método `setTitulo()`, `setAutor()`, `agregarCapitulo()`
- Configuración de márgenes y estilos
- Method chaining para construcción fluida
- Validación de documento completo

**Ejemplo:**
```python
pdf = PDFBuilder()
    .setTitulo("Mi Documento")
    .setAutor("Juan Perez")
    .agregarCapitulo("Introduccion")
    .build()
```

---

## 🔍 Trabajo de Investigación

**Archivo:** `investigacion_frameworks.md`

**Contenido:**
- **Django (Python)**: Uso de Singleton en settings.py
- **Spring Boot (Java)**: Beans singleton por defecto
- **Qt (C++)**: QApplication como Singleton
- **Factory en frameworks**: Creación de objetos en Spring IoC
- **Builder en bibliotecas**: StringBuilder en Java, Builders en Retrofit

**Frameworks analizados:**
1. Django (Python)
2. Spring Boot (Java)
3. Qt (C++)
4. Tkinter (Python)

---

## 📊 Resultados

### Informe LaTeX
**Archivo:** `informe_patrones_creacionales.tex`

**Contenido:**
- Marco teórico de patrones creacionales
- Implementaciones en C++ y Python
- Análisis comparativo de lenguajes
- Ejemplos ejecutados
- Aplicaciones en frameworks reales
- Ventajas y desventajas
- Conclusiones

### Diagramas UML
**Carpeta:** `resultados/diagramas_UML/`

**Archivos:**
- `singleton.puml` - Diagrama UML del patrón Singleton
- `factory.puml` - Diagrama UML del patrón Factory
- `builder.puml` - Diagrama UML del patrón Builder
- `README.md` - Guía para visualizar diagramas

**Visualización:**
Los diagramas se pueden ver directamente en GitHub o usando PlantUML.

**Ver diagramas:** [README de Diagramas UML](./resultados/diagramas_UML/README.md)

---

## 🚀 Cómo Ejecutar

### C++
```bash
# Compilar
g++ -std=c++11 codigo_ejemplos/ejemplo1_singleton.cpp -o singleton
g++ -std=c++11 desarrollo/desarrollo1_singleton_logger.cpp -o logger

# Ejecutar
./singleton
./logger
```

### Python
```bash
# Ejecutar directamente
python3 codigo_ejemplos/ejemplo1_singleton.py
python3 desarrollo/desarrollo1_singleton_logger.py
```

---

## 📈 Comparación C++ vs Python

| Aspecto | C++ | Python |
|---------|-----|--------|
| **Singleton** | Constructor privado, instancia estática | `__new__` o módulo |
| **Factory** | Métodos estáticos, punteros | Funciones o clases |
| **Builder** | Method chaining con punteros | Method chaining directo |
| **Rendimiento** | Alto (compilado) | Moderado (interpretado) |
| **Código** | Más verboso | Más conciso |
| **Seguridad de tipos** | Fuerte (en compilación) | Dinámica (en ejecución) |

---

## 🎯 Aprendizajes Clave

1. **Singleton** garantiza una única instancia, útil para configuraciones globales
2. **Factory** desacopla la creación de objetos del código cliente
3. **Builder** facilita la construcción de objetos complejos paso a paso
4. Los patrones son independientes del lenguaje pero su implementación varía
5. C++ requiere gestión manual de memoria, Python usa garbage collection

---

## 📚 Referencias

- Gamma, E. et al. (1994). Design Patterns: Elements of Reusable Object-Oriented Software
- [Refactoring Guru - Creational Patterns](https://refactoring.guru/design-patterns/creational-patterns)
- Documentación C++: https://cppreference.com
- Documentación Python: https://docs.python.org

---

**Universidad Nacional del Altiplano - 2025**
