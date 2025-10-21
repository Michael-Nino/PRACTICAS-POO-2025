/*
 * EJEMPLO 1: Observer en C++
 * (Version cruzada del ejemplo Python del PDF - Semana 7)
 */

#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Observador {
public:
    void actualizar(const string& mensaje) {
        cout << "Notificado: " << mensaje << endl;
    }
};

class Sujeto {
private:
    vector<Observador*> obs;
    
public:
    void registrar(Observador* o) {
        obs.push_back(o);
    }
    
    void notificar(const string& mensaje) {
        for (auto o : obs) {
            o->actualizar(mensaje);
        }
    }
};

int main() {
    Sujeto s;
    Observador o1, o2;
    s.registrar(&o1);
    s.registrar(&o2);
    s.notificar("Se actualizo el sistema.");
    return 0;
}
