/*
 * DESARROLLO 3: Builder en C++ - Generador de Documentos PDF
 * (EJERCICIO NUEVO - NO es el ejemplo del PDF de computadoras)
 */

#include <iostream>
#include <string>
#include <vector>

using namespace std;

class DocumentoPDF {
public:
    string titulo;
    string autor;
    vector<string> capitulos;
    
    void mostrar() const {
        cout << "Titulo: " << titulo << endl;
        cout << "Autor: " << autor << endl;
        cout << "\nCapitulos:" << endl;
        for (const auto& cap : capitulos) {
            cout << "  - " << cap << endl;
        }
    }
};

class PDFBuilder {
private:
    DocumentoPDF documento;
    
public:
    PDFBuilder& setTitulo(const string& titulo) {
        documento.titulo = titulo;
        return *this;
    }
    
    PDFBuilder& setAutor(const string& autor) {
        documento.autor = autor;
        return *this;
    }
    
    PDFBuilder& agregarCapitulo(const string& capitulo) {
        documento.capitulos.push_back(capitulo);
        return *this;
    }
    
    DocumentoPDF build() {
        return documento;
    }
};

int main() {
    cout << "=== DESARROLLO 3: BUILDER - PDF ===" << endl << endl;
    
    // Construir documento
    PDFBuilder builder;
    DocumentoPDF documento = builder
        .setTitulo("Manual de C++")
        .setAutor("Pedro Lopez")
        .agregarCapitulo("Capitulo 1: Introduccion")
        .agregarCapitulo("Capitulo 2: Punteros")
        .agregarCapitulo("Capitulo 3: Clases")
        .build();
    
    documento.mostrar();
    
    return 0;
}

/*
 * COMPILAR: g++ -std=c++14 desarrollo3_builder_pdf.cpp -o desarrollo3_builder
 * EJECUTAR: ./desarrollo3_builder
 */
