/*
 * DESARROLLO 3: Composite para carpetas y archivos
 * (EJERCICIO NUEVO - NO es el ejemplo del PDF)
 */

#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Elemento {
public:
    virtual void mostrar(int nivel = 0) = 0;
};

class Archivo : public Elemento {
private:
    string nombre;
    
public:
    Archivo(const string& n) : nombre(n) {}
    
    void mostrar(int nivel = 0) override {
        for (int i = 0; i < nivel; i++) cout << "  ";
        cout << "- " << nombre << endl;
    }
};

class Carpeta : public Elemento {
private:
    string nombre;
    vector<Elemento*> elementos;
    
public:
    Carpeta(const string& n) : nombre(n) {}
    
    void agregar(Elemento* e) {
        elementos.push_back(e);
    }
    
    void mostrar(int nivel = 0) override {
        for (int i = 0; i < nivel; i++) cout << "  ";
        cout << "/ " << nombre << "/" << endl;
        for (auto e : elementos) {
            e->mostrar(nivel + 1);
        }
    }
};

int main() {
    Carpeta raiz("Documentos");
    Archivo informe("informe.pdf");
    raiz.agregar(&informe);
    
    Carpeta carpeta_imagenes("Imagenes");
    Archivo foto1("foto1.jpg");
    Archivo foto2("foto2.jpg");
    carpeta_imagenes.agregar(&foto1);
    carpeta_imagenes.agregar(&foto2);
    
    raiz.agregar(&carpeta_imagenes);
    raiz.mostrar();
    
    return 0;
}
