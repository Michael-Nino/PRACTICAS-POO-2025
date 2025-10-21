# Semana 6: Patrones de Diseño Estructurales

## 📚 Patrones Estudiados
- **Adapter**
- **Decorator**
- **Composite**

## 📄 Informe LaTeX
**Ver informe completo:** [Overleaf - Semana 6](https://es.overleaf.com/read/bvzzgtrkxwcb#26f16c)

---

## 📂 Estructura de Carpetas

```
semana_6_patrones_estructurales/
├── codigo_ejemplos/
├── desarrollo/
├── trabajo_investigacion/
└── resultados/
```

---

## 💡 Código de Ejemplos

Ejemplos extraídos directamente del material del curso (PDF).

### Adapter
- **`ejemplo1_adapter.cpp`** - Adaptador de enchufe europeo a americano
- **`ejemplo1_adapter.py`** - Adapter para interfaces incompatibles

**Características:**
- Clase `EnchufeEuropeo` con método `conectarTipoC()`
- Clase `Adaptador` que implementa interfaz americana
- Conversión de interfaz incompatible
- Permite usar objetos existentes con nueva interfaz

**Uso:**
```cpp
EnchufeEuropeo* europeo = new EnchufeEuropeo();
EnchufeAmericano* adaptado = new Adaptador(europeo);
adaptado->conectar(); // Usa el enchufe europeo
```

### Decorator
- **`ejemplo2_decorator.cpp`** - Decoradores para sistema de logging
- **`ejemplo2_decorator.py`** - Añade funcionalidad de timestamp y nivel

**Características:**
- Clase base `Logger` con método `log()`
- Decoradores: `TimestampDecorator`, `LevelDecorator`
- Composición en lugar de herencia
- Añade funcionalidad dinámicamente

**Uso:**
```cpp
Logger* logger = new TimestampDecorator(
    new LevelDecorator(new SimpleLogger())
);
logger->log("Mensaje");
// Salida: [2025-01-15 10:30:45] [INFO] Mensaje
```

### Composite
- **`ejemplo3_composite.cpp`** - Jerarquía de formas geométricas
- **`ejemplo3_composite.py`** - Círculos y grupos de formas

**Características:**
- Interfaz `Forma` con método `dibujar()`
- Clase `Circulo` como hoja
- Clase `Grupo` como composición
- Tratamiento uniforme de objetos individuales y compuestos

**Uso:**
```cpp
Grupo* grupo = new Grupo();
grupo->agregar(new Circulo(5));
grupo->agregar(new Circulo(10));
grupo->dibujar(); // Dibuja todos los círculos
```

---

## 🔨 Desarrollo (Ejercicios Prácticos)

Ejercicios completamente diferentes a los ejemplos del PDF.

### Desarrollo 1: Adaptador de Sistemas de Pago
- **`desarrollo1_adapter_pagos.cpp`**
- **`desarrollo1_adapter_pagos.py`**

**Descripción:**
Sistema que adapta diferentes APIs de pago (PayPal, Stripe, MercadoPago) a una interfaz común.

**Funcionalidades:**
- Interfaz `ProcesadorPago` con método `procesarPago()`
- Adaptadores para cada servicio externo
- API legada adaptada a nueva interfaz
- Cambio transparente entre proveedores

**Ejemplo de uso:**
```cpp
ProcesadorPago* paypal = new AdaptadorPayPal();
paypal->procesarPago(100.50);
// Salida: [PayPal] Procesando $100.50
```

**Clases:**
- `ProcesadorPago` (interfaz objetivo)
- `PayPalAPI`, `StripeAPI` (APIs externas)
- `AdaptadorPayPal`, `AdaptadorStripe` (adaptadores)

### Desarrollo 2: Decorador de Validación de Formularios
- **`desarrollo2_decorator_validacion.cpp`**
- **`desarrollo2_decorator_validacion.py`**

**Descripción:**
Sistema de validación de formularios con decoradores que añaden diferentes validaciones dinámicamente.

**Funcionalidades:**
- Clase base `Formulario` con método `enviar()`
- Decoradores: `ValidadorEmail`, `ValidadorLongitud`, `ValidadorSQL`
- Composición de múltiples validaciones
- Prevención de inyección SQL

**Ejemplo:**
```python
form = ValidadorEmail(
    ValidadorLongitud(
        ValidadorSQL(FormularioBase())
    )
)
form.enviar("usuario@email.com", "contraseña123")
```

**Validaciones:**
- Email: Verifica formato válido
- Longitud: Verifica mínimo/máximo de caracteres
- SQL: Detecta intentos de inyección SQL

### Desarrollo 3: Sistema de Archivos (Composite)
- **`desarrollo3_composite_archivos.cpp`**
- **`desarrollo3_composite_archivos.py`**

**Descripción:**
Representación de sistema de archivos con archivos y carpetas usando patrón Composite.

**Funcionalidades:**
- Interfaz `ElementoSistema` con métodos `mostrar()` y `tamanio()`
- Clase `Archivo` como elemento hoja
- Clase `Carpeta` como composición
- Cálculo recursivo de tamaños

**Ejemplo:**
```cpp
Carpeta* documentos = new Carpeta("Documentos");
documentos->agregar(new Archivo("informe.pdf", 1024));
documentos->agregar(new Archivo("foto.jpg", 2048));

Carpeta* raiz = new Carpeta("C:");
raiz->agregar(documentos);
raiz->mostrar(); // Muestra estructura jerárquica
```

**Estructura:**
```
C:/
  Documentos/
    informe.pdf (1024 KB)
    foto.jpg (2048 KB)
  Descargas/
    archivo.zip (5120 KB)
```

---

## 🔍 Trabajo de Investigación

**Archivo:** `investigacion_frameworks.md`

**Contenido:**
- **Qt (C++)**: QLayout como Composite para widgets
- **Java Swing**: Component/Container como Composite
- **Flask (Python)**: Decoradores para rutas y autenticación
- **Django**: Middleware como cadena de decoradores
- **Adapter en ORMs**: Adaptación de diferentes bases de datos

**Frameworks analizados:**
1. Qt (C++)
2. Java Swing (Java)
3. Flask (Python)
4. Django (Python)

**Casos de uso:**
- Layouts anidados en interfaces gráficas
- Decoradores @app.route en Flask
- Sistema de middleware en Django
- Componentes UI jerárquicos

---

## 📊 Resultados

### Informe LaTeX
**Archivo:** `informe_patrones_estructurales.tex`

**Contenido:**
- Marco teórico de patrones estructurales
- Implementaciones detalladas en C++ y Python
- Análisis comparativo de lenguajes
- Ejemplos ejecutados del desarrollo
- Aplicaciones en frameworks reales
- Ventajas y desventajas de cada patrón
- Resultados y conclusiones

### Diagramas UML
**Carpeta:** `resultados/diagramas_UML/`

**Archivos:**
- `adapter.puml` - Diagrama UML del patrón Adapter
- `decorator.puml` - Diagrama UML del patrón Decorator
- `composite.puml` - Diagrama UML del patrón Composite
- `README.md` - Guía para visualizar diagramas

**Características de los diagramas:**
- Notación UML profesional
- Relaciones claramente identificadas
- Notas explicativas
- Ejemplos de uso incluidos

**Ver diagramas:** [README de Diagramas UML](./resultados/diagramas_UML/README.md)

---

## 🚀 Cómo Ejecutar

### C++
```bash
# Compilar ejemplos
g++ -std=c++11 codigo_ejemplos/ejemplo1_adapter.cpp -o adapter
g++ -std=c++11 codigo_ejemplos/ejemplo2_decorator.cpp -o decorator
g++ -std=c++11 codigo_ejemplos/ejemplo3_composite.cpp -o composite

# Compilar desarrollos
g++ -std=c++11 desarrollo/desarrollo1_adapter_pagos.cpp -o pagos
g++ -std=c++11 desarrollo/desarrollo2_decorator_validacion.cpp -o validacion
g++ -std=c++11 desarrollo/desarrollo3_composite_archivos.cpp -o archivos

# Ejecutar
./adapter
./pagos
```

### Python
```bash
# Ejecutar ejemplos
python3 codigo_ejemplos/ejemplo1_adapter.py
python3 codigo_ejemplos/ejemplo2_decorator.py
python3 codigo_ejemplos/ejemplo3_composite.py

# Ejecutar desarrollos
python3 desarrollo/desarrollo1_adapter_pagos.py
python3 desarrollo/desarrollo2_decorator_validacion.py
python3 desarrollo/desarrollo3_composite_archivos.py
```

---

## 📈 Comparación C++ vs Python

| Aspecto | C++ | Python |
|---------|-----|--------|
| **Adapter** | Herencia múltiple o composición | Duck typing o herencia |
| **Decorator** | Punteros y composición | Decoradores nativos (@) |
| **Composite** | Vectores de punteros | Listas dinámicas |
| **Interfaces** | Clases abstractas puras | ABC o duck typing |
| **Memoria** | Gestión manual | Garbage collection |
| **Flexibilidad** | Fuertemente tipado | Tipado dinámico |

---

## 🎯 Aprendizajes Clave

1. **Adapter** permite reutilizar código existente con interfaces incompatibles
2. **Decorator** añade responsabilidades a objetos sin modificar su código
3. **Composite** trata objetos individuales y composiciones uniformemente
4. Los patrones estructurales mejoran la flexibilidad del diseño
5. Composición sobre herencia es un principio fundamental
6. Python tiene soporte nativo para decoradores (@decorator)
7. C++ requiere más código pero ofrece mayor control

---

## 🌟 Casos de Uso Reales

### Adapter
- Integración de APIs de terceros
- Migración de sistemas legacy
- Compatibilidad entre versiones

### Decorator
- Autenticación y autorización
- Logging y monitoreo
- Compresión y encriptación
- Validación de datos

### Composite
- Interfaces gráficas (widgets anidados)
- Sistemas de archivos
- Estructuras organizacionales
- Menús jerárquicos

---

## 📚 Referencias

- Gamma, E. et al. (1994). Design Patterns: Elements of Reusable Object-Oriented Software
- [Refactoring Guru - Structural Patterns](https://refactoring.guru/design-patterns/structural-patterns)
- Qt Documentation: https://doc.qt.io
- Flask Documentation: https://flask.palletsprojects.com
- Python Decorators Guide: https://realpython.com/primer-on-python-decorators/

---

**Universidad Nacional del Altiplano - 2025**
