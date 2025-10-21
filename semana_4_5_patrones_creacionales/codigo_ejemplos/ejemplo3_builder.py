# Ejemplo 3: Builder en Python (EXACTO DEL PDF)

class Computadora:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.gpu = None

class Builder:
    def __init__(self):
        self.computadora = Computadora()
    
    def add_cpu(self, cpu):
        self.computadora.cpu = cpu
        return self
    
    def add_ram(self, ram):
        self.computadora.ram = ram
        return self
    
    def add_gpu(self, gpu):
        self.computadora.gpu = gpu
        return self
    
    def build(self):
        return self.computadora

pc = Builder().add_cpu("Intel i9").add_ram("32GB").add_gpu("RTX 4090").build()
print(vars(pc))
