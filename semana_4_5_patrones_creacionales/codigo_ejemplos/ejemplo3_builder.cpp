// Ejemplo 3: Builder en C++ (VERSIÓN CRUZADA del ejemplo Python)

#include <iostream>
#include <string>
using namespace std;

class Computadora {
public:
    string cpu;
    string ram;
    string gpu;
    
    void mostrar() {
        cout << "CPU: " << cpu << endl;
        cout << "RAM: " << ram << endl;
        cout << "GPU: " << gpu << endl;
    }
};

class Builder {
private:
    Computadora* computadora;
    
public:
    Builder() {
        computadora = new Computadora();
    }
    
    Builder* add_cpu(string cpu) {
        computadora->cpu = cpu;
        return this;
    }
    
    Builder* add_ram(string ram) {
        computadora->ram = ram;
        return this;
    }
    
    Builder* add_gpu(string gpu) {
        computadora->gpu = gpu;
        return this;
    }
    
    Computadora* build() {
        return computadora;
    }
};

int main() {
    Computadora* pc = (new Builder())
        ->add_cpu("Intel i9")
        ->add_ram("32GB")
        ->add_gpu("RTX 4090")
        ->build();
    
    pc->mostrar();
    return 0;
}
