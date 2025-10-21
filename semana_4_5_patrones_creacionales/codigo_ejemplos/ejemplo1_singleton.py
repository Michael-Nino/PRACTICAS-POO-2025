# Ejemplo 1: Singleton en Python (VERSIÓN CRUZADA del ejemplo C++)

class Config:
    """Versión Python del Singleton del PDF"""
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def show_message(self):
        print("Configuración global cargada.")

# Prueba
obj1 = Config()
obj2 = Config()
obj1.show_message()
print(f"¿Son iguales? {obj1 is obj2}")
