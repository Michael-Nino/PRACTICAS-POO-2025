/*
 * DESARROLLO 1: Adaptador de pagos (dolares a soles)
 * (EJERCICIO NUEVO - NO es el ejemplo del PDF)
 */

#include <iostream>
#include <string>

using namespace std;

class PasarelaDolares {
public:
    string pagarUSD(double monto) {
        return "Pago: $" + to_string(monto) + " USD";
    }
};

class AdaptadorSoles {
private:
    PasarelaDolares* pasarela;
    double tipoCambio = 3.75;
    
public:
    AdaptadorSoles(PasarelaDolares* p) : pasarela(p) {}
    
    string pagarSoles(double monto) {
        double montoUSD = monto / tipoCambio;
        return "Convertido: S/" + to_string(monto) + " -> " + pasarela->pagarUSD(montoUSD);
    }
};

int main() {
    PasarelaDolares pasarela;
    AdaptadorSoles adaptador(&pasarela);
    cout << adaptador.pagarSoles(375) << endl;
    return 0;
}
