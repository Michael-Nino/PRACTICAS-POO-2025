/*
 * EJEMPLO 2: Strategy en C++
 * (Ejemplo del PDF - Semana 7)
 */

#include <iostream>

using namespace std;

class Estrategia {
public:
    virtual void ejecutar() = 0;
};

class EstrategiaA : public Estrategia {
public:
    void ejecutar() override { 
        cout << "Algoritmo A\n"; 
    }
};

class EstrategiaB : public Estrategia {
public:
    void ejecutar() override { 
        cout << "Algoritmo B\n"; 
    }
};

class Contexto {
    Estrategia* estrategia;
public:
    Contexto(Estrategia* e) : estrategia(e) {}
    void setEstrategia(Estrategia* e) { estrategia = e; }
    void operar() { estrategia->ejecutar(); }
};

int main() {
    EstrategiaA a;
    EstrategiaB b;
    Contexto ctx(&a);
    ctx.operar();
    ctx.setEstrategia(&b);
    ctx.operar();
}
