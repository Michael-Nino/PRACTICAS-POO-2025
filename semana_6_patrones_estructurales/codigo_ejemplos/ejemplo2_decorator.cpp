/*
 * EJEMPLO 2: Decorator en C++
 * (Version cruzada del ejemplo Python del PDF - Semana 6)
 */

#include <iostream>
#include <string>
#include <functional>

using namespace std;

// Funcion base
string saludar(const string& nombre) {
    return "Hola " + nombre;
}

// Decorator que agrega log
function<string(const string&)> log(function<string(const string&)> func, const string& nombre_func) {
    return [func, nombre_func](const string& arg) {
        cout << "Ejecutando funcion: " << nombre_func << endl;
        return func(arg);
    };
}

int main() {
    auto saludar_con_log = log(saludar, "saludar");
    cout << saludar_con_log("Aldo") << endl;
    return 0;
}
