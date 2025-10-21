# Trabajo de Investigacion: Patrones de Comportamiento en Frameworks

## Semana 7: Observer, Strategy, Command

### 1. Observer en Android LiveData

#### Android LiveData - Patron Observer
- **Uso**: Observar cambios en datos de la UI
- **Implementacion**: LiveData es un observable, Activities/Fragments son observers
- **Ejemplo**:
```java
// ViewModel con LiveData
public class UserViewModel extends ViewModel {
    private MutableLiveData<User> user = new MutableLiveData<>();
    
    public LiveData<User> getUser() {
        return user;
    }
}

// Activity observando
userViewModel.getUser().observe(this, user -> {
    // Se ejecuta automaticamente cuando user cambia
    textView.setText(user.getName());
});
```

#### Ventajas de LiveData
- **Lifecycle-aware**: Solo notifica cuando la UI esta activa
- **Previene memory leaks**: Se desuscribe automaticamente
- **Actualizacion automatica**: UI siempre sincronizada con datos
- **No mas crashes**: No actualiza UI cuando Activity esta detenida

### 2. Observer en Otros Frameworks

#### RxJava (Java/Android)
- **Uso**: Programacion reactiva
- **Ejemplo**:
```java
Observable<String> observable = Observable.just("Hola");
observable.subscribe(data -> System.out.println(data));
```

#### Vue.js (JavaScript)
- **Uso**: Reactividad en componentes web
- **Implementacion**: Propiedades data son observables
- **Ejemplo**:
```javascript
new Vue({
  data: { mensaje: 'Hola' },
  watch: {
    mensaje(nuevo, viejo) {
      console.log('Cambio de', viejo, 'a', nuevo);
    }
  }
});
```

### 3. Strategy en Frameworks

#### Spring Security (Java)
- **Uso**: Diferentes estrategias de autenticacion
- **Implementacion**: AuthenticationProvider como Strategy
- **Soporta**: LDAP, Database, OAuth, JWT
- **Ventaja**: Cambiar metodo de auth sin cambiar codigo

#### Collections.sort() en Java
- **Uso**: Diferentes algoritmos de comparacion
- **Ejemplo**:
```java
Collections.sort(lista, (a, b) -> a.compareTo(b));
Collections.sort(lista, Comparator.reverseOrder());
```

### 4. Command en Frameworks

#### Spring @Transactional
- **Uso**: Encapsula operaciones de base de datos
- **Implementacion**: Cada transaccion es un Command
- **Permite**: Rollback automatico en errores

### 5. Comparacion

| Patron | Framework | Uso Principal |
|--------|-----------|---------------|
| Observer | Android LiveData | Sincronizacion UI-Datos |
| Observer | RxJava | Streams reactivos |
| Observer | Vue.js | Reactividad web |
| Strategy | Spring Security | Metodos de autenticacion |
| Strategy | Collections.sort | Algoritmos de ordenamiento |
| Command | Spring | Transacciones BD |

### 6. Conclusiones

1. **Observer**: Fundamental en arquitecturas reactivas modernas
2. **LiveData**: Implementacion inteligente que respeta el ciclo de vida Android
3. **Strategy**: Permite flexibilidad en algoritmos sin modificar cliente
4. **Command**: Esencial para operaciones reversibles (undo/redo)
5. Estos patrones son la base de la programacion reactiva
6. Android usa Observer extensivamente en su arquitectura MVVM
