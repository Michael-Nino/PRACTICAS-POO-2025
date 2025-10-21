// Ejemplo 2: Factory en C++ (VERSIÓN CRUZADA del ejemplo Python)

#include <iostream>
#include <string>
using namespace std;

class Transporte {
public:
    virtual string entregar() = 0;
    virtual ~Transporte() {}
};

class Camion : public Transporte {
public:
    string entregar() override {
        return "Entrega por carretera";
    }
};

class Barco : public Transporte {
public:
    string entregar() override {
        return "Entrega por mar";
    }
};

class Factory {
public:
    static Transporte* get_transporte(string tipo) {
        if (tipo == "camion") return new Camion();
        else if (tipo == "barco") return new Barco();
        return nullptr;
    }
};

int main() {
    Transporte* t = Factory::get_transporte("barco");
    cout << t->entregar() << endl;
    delete t;
    return 0;
}
