/*
 * EJEMPLO 3: Command en C++
 * (Version cruzada del ejemplo Python del PDF - Semana 7)
 */

#include <iostream>
#include <vector>

using namespace std;

class Command {
public:
    virtual void ejecutar() = 0;
};

class ImprimirCommand : public Command {
public:
    void ejecutar() override {
        cout << "Imprimiendo documento..." << endl;
    }
};

class GuardarCommand : public Command {
public:
    void ejecutar() override {
        cout << "Guardando documento..." << endl;
    }
};

class Invocador {
private:
    vector<Command*> historial;
    
public:
    void ejecutar(Command* comando) {
        comando->ejecutar();
        historial.push_back(comando);
    }
};

int main() {
    Invocador i;
    ImprimirCommand imprimir;
    GuardarCommand guardar;
    
    i.ejecutar(&imprimir);
    i.ejecutar(&guardar);
    
    return 0;
}
