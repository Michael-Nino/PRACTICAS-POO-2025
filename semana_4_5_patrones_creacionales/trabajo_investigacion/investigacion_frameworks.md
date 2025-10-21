# Trabajo de Investigacion: Patrones Creacionales en Frameworks

## Semana 4-5: Singleton, Factory, Builder

### 1. Patron Singleton en Frameworks

#### Django (Python)
- **Uso**: Settings y configuracion global
- **Implementacion**: El objeto `settings` es un Singleton que contiene toda la configuracion
- **Ejemplo**: `django.conf.settings` se carga una sola vez y se reutiliza en toda la aplicacion
- **Ventaja**: Garantiza configuracion consistente en toda la aplicacion

#### Spring Boot (Java)
- **Uso**: Beans por defecto son Singleton
- **Implementacion**: `@Component`, `@Service`, `@Repository` crean Singletons
- **Ejemplo**: Una clase anotada con `@Service` tendra una unica instancia en el contenedor
- **Ventaja**: Ahorro de memoria y rendimiento mejorado

### 2. Patron Factory en Frameworks

#### Django ORM (Python)
- **Uso**: Creacion de instancias de modelos
- **Implementacion**: `Model.objects.create()` actua como Factory
- **Ejemplo**:
```python
User.objects.create(username='juan', email='juan@mail.com')
```
- **Ventaja**: Abstrae la creacion y validacion de objetos de BD

#### Spring Framework (Java)
- **Uso**: BeanFactory para crear objetos
- **Implementacion**: `ApplicationContext` es una Factory avanzada
- **Ejemplo**: `context.getBean("miServicio")` retorna instancia creada
- **Ventaja**: Inversion de control y gestion automatica de dependencias

### 3. Patron Builder en Frameworks

#### Tkinter vs Qt (Python/C++)

**Tkinter (Python)**
- **Uso**: Construccion de interfaces graficas
- **Implementacion**: Widgets se construyen paso a paso
- **Ejemplo**:
```python
ventana = tk.Tk()
ventana.title("Mi App")
ventana.geometry("800x600")
boton = tk.Button(ventana, text="Click")
```

**Qt (C++/Python)**
- **Uso**: Construccion de objetos complejos de UI
- **Implementacion**: Clases Builder para dialogos y ventanas
- **Ejemplo**:
```cpp
QMessageBox msgBox;
msgBox.setText("Mensaje");
msgBox.setIcon(QMessageBox::Information);
msgBox.setStandardButtons(QMessageBox::Ok);
```
- **Ventaja**: Construccion flexible de componentes complejos

### 4. Comparacion de Implementaciones

| Framework | Singleton | Factory | Builder |
|-----------|-----------|---------|---------|
| Django | Settings global | ORM objects | Form builders |
| Spring Boot | Bean scope | BeanFactory | RequestBuilder |
| Qt | QApplication | QObject | QMessageBox |
| Tkinter | Root window | Widget creation | Window builder |

### 5. Conclusiones

1. **Singleton**: Esencial para configuraciones y recursos compartidos
2. **Factory**: Simplifica creacion de objetos complejos
3. **Builder**: Ideal para objetos con muchas configuraciones opcionales
4. Todos los frameworks modernos usan estos patrones internamente
5. Comprender estos patrones ayuda a usar mejor los frameworks
