/*
 * DESARROLLO 2: Strategy para algoritmos de ordenamiento
 * (EJERCICIO NUEVO - NO es el ejemplo del PDF)
 */

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Ordenamiento {
public:
    virtual vector<int> ordenar(vector<int> lista) = 0;
};

class Burbuja : public Ordenamiento {
public:
    vector<int> ordenar(vector<int> lista) override {
        int n = lista.size();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n-i-1; j++) {
                if (lista[j] > lista[j+1]) {
                    swap(lista[j], lista[j+1]);
                }
            }
        }
        return lista;
    }
};

class QuickSort : public Ordenamiento {
public:
    vector<int> ordenar(vector<int> lista) override {
        if (lista.size() <= 1) return lista;
        
        int pivote = lista[lista.size() / 2];
        vector<int> izq, medio, der;
        
        for (int x : lista) {
            if (x < pivote) izq.push_back(x);
            else if (x == pivote) medio.push_back(x);
            else der.push_back(x);
        }
        
        vector<int> resultado = ordenar(izq);
        resultado.insert(resultado.end(), medio.begin(), medio.end());
        vector<int> derOrdenado = ordenar(der);
        resultado.insert(resultado.end(), derOrdenado.begin(), derOrdenado.end());
        
        return resultado;
    }
};

class Ordenador {
private:
    Ordenamiento* estrategia;
    
public:
    Ordenador(Ordenamiento* e) : estrategia(e) {}
    
    vector<int> ordenar(vector<int> lista) {
        return estrategia->ordenar(lista);
    }
};

void imprimir(const string& titulo, const vector<int>& v) {
    cout << titulo;
    for (int x : v) cout << x << " ";
    cout << endl;
}

int main() {
    vector<int> numeros = {64, 34, 25, 12, 22, 11, 90};
    
    imprimir("Original: ", numeros);
    
    Burbuja burbuja;
    Ordenador ord1(&burbuja);
    imprimir("Burbuja: ", ord1.ordenar(numeros));
    
    QuickSort quicksort;
    Ordenador ord2(&quicksort);
    imprimir("QuickSort: ", ord2.ordenar(numeros));
    
    return 0;
}
