/*
 * EJEMPLO 3: Composite en C++
 * (Ejemplo del PDF - Semana 6)
 */

#include <iostream>
#include <vector>

using namespace std;

class Figura {
public:
    virtual void dibujar() = 0;
};

class Circulo : public Figura {
public:
    void dibujar() override { 
        cout << "Circulo\n"; 
    }
};

class Grupo : public Figura {
    vector<Figura*> figuras;
public:
    void add(Figura* f) { 
        figuras.push_back(f); 
    }
    
    void dibujar() override {
        for (auto f : figuras) 
            f->dibujar();
    }
};

int main() {
    Circulo c1, c2;
    Grupo g;
    g.add(&c1);
    g.add(&c2);
    g.dibujar();
}
