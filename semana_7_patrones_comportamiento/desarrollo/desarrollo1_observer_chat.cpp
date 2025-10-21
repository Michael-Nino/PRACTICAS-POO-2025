/*
 * DESARROLLO 1: Observer para sistema de chat
 * (EJERCICIO NUEVO - NO es el ejemplo del PDF)
 */

#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Usuario {
private:
    string nombre;
    
public:
    Usuario(const string& n) : nombre(n) {}
    
    void recibir_mensaje(const string& mensaje) {
        cout << nombre << " recibio: " << mensaje << endl;
    }
    
    string get_nombre() { return nombre; }
};

class Chat {
private:
    vector<Usuario*> usuarios;
    
public:
    void unirse(Usuario* usuario) {
        usuarios.push_back(usuario);
        cout << usuario->get_nombre() << " se unio al chat" << endl;
    }
    
    void enviar_mensaje(const string& mensaje) {
        for (auto u : usuarios) {
            u->recibir_mensaje(mensaje);
        }
    }
};

int main() {
    Chat chat;
    Usuario u1("Juan");
    Usuario u2("Maria");
    
    chat.unirse(&u1);
    chat.unirse(&u2);
    chat.enviar_mensaje("Hola a todos!");
    
    return 0;
}
