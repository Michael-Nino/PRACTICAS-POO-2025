/*
 * DESARROLLO 2: Decorator para validacion en funciones matematicas
 * (EJERCICIO NUEVO - NO es el ejemplo del PDF)
 */

#include <iostream>
#include <string>
#include <cmath>
#include <functional>

using namespace std;

function<string(double)> validar_positivo(function<double(double)> func, const string& nombre) {
    return [func, nombre](double n) -> string {
        if (n < 0) {
            return "Error: numero negativo";
        }
        double resultado = func(n);
        return nombre + " de " + to_string((int)n) + " = " + to_string(resultado);
    };
}

double raiz_cuadrada(double n) {
    return sqrt(n);
}

int main() {
    auto raiz_con_validacion = validar_positivo(raiz_cuadrada, "Raiz");
    
    cout << raiz_con_validacion(16) << endl;
    cout << raiz_con_validacion(-4) << endl;
    
    return 0;
}
