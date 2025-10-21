# Trabajo de Investigacion: Patrones Estructurales en Frameworks

## Semana 6: Adapter, Decorator, Composite

### 1. Composite en Qt y Java Swing

#### Qt (C++)
- **Uso**: Jerarquia de widgets (QWidget, QLayout)
- **Implementacion**: Todos los widgets pueden contener otros widgets
- **Ejemplo**: QVBoxLayout puede contener QLabel, QPushButton, etc.
- **Codigo**:
```cpp
QWidget *window = new QWidget();
QVBoxLayout *layout = new QVBoxLayout();
layout->addWidget(new QPushButton("Boton 1"));
layout->addWidget(new QPushButton("Boton 2"));
window->setLayout(layout);
```

#### Java Swing
- **Uso**: Componentes graficos (JPanel, JFrame)
- **Implementacion**: Container puede contener otros Component
- **Ejemplo**: JPanel contiene JButton, JLabel
- **Codigo**:
```java
JFrame frame = new JFrame();
JPanel panel = new JPanel();
panel.add(new JButton("Boton 1"));
panel.add(new JButton("Boton 2"));
frame.add(panel);
```

### 2. Decorator en Flask (Python)

#### Flask - Manejo de Rutas
- **Uso**: Decoradores para definir rutas y middleware
- **Implementacion**: `@app.route()` es un decorator
- **Ejemplo**:
```python
@app.route('/usuarios')
@login_required
@admin_required
def lista_usuarios():
    return render_template('usuarios.html')
```

#### Decoradores Comunes en Flask
- `@app.route()`: Define ruta HTTP
- `@login_required`: Requiere autenticacion
- `@cache.cached()`: Cachea respuesta
- `@app.before_request`: Ejecuta antes de cada request

### 3. Adapter en Frameworks

#### Django - Database Adapters
- **Uso**: Adaptadores para diferentes bases de datos
- **Implementacion**: DatabaseWrapper adapta cada motor de BD
- **Soporta**: PostgreSQL, MySQL, SQLite, Oracle
- **Ventaja**: Mismo codigo ORM funciona con cualquier BD

### 4. Comparacion

| Patron | Framework | Uso Principal |
|--------|-----------|---------------|
| Composite | Qt | Jerarquia de widgets |
| Composite | Swing | Contenedores de componentes |
| Decorator | Flask | Rutas y middleware |
| Decorator | Django | Permisos y cache |
| Adapter | Django | Motores de base de datos |
| Adapter | JDBC | Drivers de BD en Java |

### 5. Conclusiones

1. **Composite**: Esencial para interfaces graficas jerarquicas
2. **Decorator**: Muy util en frameworks web para funcionalidad cruzada
3. **Adapter**: Permite integrar sistemas heterogeneos
4. Estos patrones facilitan la extension sin modificar codigo existente
5. Flask usa decoradores extensivamente, es su caracteristica principal
