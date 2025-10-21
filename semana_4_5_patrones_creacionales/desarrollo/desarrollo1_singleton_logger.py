"""
DESARROLLO 1: Singleton en Python - Sistema de Logging
(VERSION CRUZADA del desarrollo C++)
"""

class Logger:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        self.log_file = open("aplicacion.log", "a")
    
    def log(self, mensaje):
        self.log_file.write(mensaje + "\n")
        print(f"[LOG] {mensaje}")
    
    def __del__(self):
        if hasattr(self, 'log_file'):
            self.log_file.close()


def main():
    print("=== DESARROLLO 1: SINGLETON - LOGGER (Python) ===")
    
    logger1 = Logger()
    logger2 = Logger()
    
    print(f"Son la misma instancia? {logger1 is logger2}")
    
    logger1.log("Aplicacion iniciada")
    logger1.log("Usuario admin logueado")
    logger2.log("Consulta ejecutada")


if __name__ == "__main__":
    main()

"""
EJECUTAR: python3 desarrollo1_singleton_logger.py
"""
