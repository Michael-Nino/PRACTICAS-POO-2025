/*
 * DESARROLLO 2: Factory en C++ - Sistema de Notificaciones
 * (EJERCICIO NUEVO - NO es el ejemplo del PDF de transportes)
 */

#include <iostream>
#include <string>
#include <memory>

using namespace std;

// Interfaz base
class Notificacion {
public:
    virtual ~Notificacion() = default;
    virtual void enviar(const string& destinatario, const string& mensaje) = 0;
};

// Notificacion por Email
class EmailNotificacion : public Notificacion {
public:
    void enviar(const string& destinatario, const string& mensaje) override {
        cout << "Enviando EMAIL a " << destinatario << ": " << mensaje << endl;
    }
};

// Notificacion por SMS
class SMSNotificacion : public Notificacion {
public:
    void enviar(const string& destinatario, const string& mensaje) override {
        string mensajeCorto = mensaje.substr(0, 50);
        cout << "Enviando SMS a " << destinatario << ": " << mensajeCorto << endl;
    }
};

// Notificacion Push
class PushNotificacion : public Notificacion {
public:
    void enviar(const string& destinatario, const string& mensaje) override {
        cout << "Enviando PUSH a " << destinatario << ": " << mensaje << endl;
    }
};

// Factory
class NotificacionFactory {
public:
    static unique_ptr<Notificacion> crearNotificacion(const string& tipo) {
        if (tipo == "email") {
            return make_unique<EmailNotificacion>();
        } else if (tipo == "sms") {
            return make_unique<SMSNotificacion>();
        } else if (tipo == "push") {
            return make_unique<PushNotificacion>();
        } else {
            throw invalid_argument("Tipo '" + tipo + "' no soportado");
        }
    }
};

int main() {
    cout << "=== DESARROLLO 2: FACTORY - NOTIFICACIONES ===" << endl << endl;
    
    // Crear diferentes notificaciones
    auto email = NotificacionFactory::crearNotificacion("email");
    auto sms = NotificacionFactory::crearNotificacion("sms");
    auto push = NotificacionFactory::crearNotificacion("push");
    
    // Enviar mensajes
    email->enviar("admin@empresa.com", "Alerta de seguridad");
    sms->enviar("987654321", "Codigo de verificacion: 123456");
    push->enviar("device_001", "Nueva notificacion disponible");
    
    return 0;
}

/*
 * COMPILAR: g++ -std=c++14 desarrollo2_factory_notificaciones.cpp -o desarrollo2_factory
 * EJECUTAR: ./desarrollo2_factory
 */
