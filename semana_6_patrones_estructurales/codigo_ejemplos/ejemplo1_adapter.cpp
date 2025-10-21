/*
 * EJEMPLO 1: Adapter en C++
 * (Version cruzada del ejemplo Python del PDF - Semana 6)
 */

#include <iostream>
#include <string>

using namespace std;

class EnchufeEuropeo {
public:
    string conectar() {
        return "220V conectado";
    }
};

class Adaptador {
private:
    EnchufeEuropeo* enchufe;
    
public:
    Adaptador(EnchufeEuropeo* e) : enchufe(e) {}
    
    string conectar() {
        return "Adaptado a 110V -> " + enchufe->conectar();
    }
};

int main() {
    EnchufeEuropeo e;
    Adaptador a(&e);
    cout << a.conectar() << endl;
    return 0;
}
