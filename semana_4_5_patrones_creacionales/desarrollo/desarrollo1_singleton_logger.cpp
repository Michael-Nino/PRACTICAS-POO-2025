/**
 * DESARROLLO 1: Singleton en C++ - Sistema de Logging
 * (EJERCICIO NUEVO - NO es el ejemplo del PDF)
 * 
 * Sistema simple de logging con Singleton
 */

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

class Logger {
private:
    static Logger* instance;
    ofstream logFile;
    
    Logger() {
        logFile.open("aplicacion.log", ios::app);
    }

public:
    static Logger* getInstance() {
        if (instance == nullptr) {
            instance = new Logger();
        }
        return instance;
    }
    
    void log(const string& mensaje) {
        if (logFile.is_open()) {
            logFile << mensaje << endl;
            cout << "[LOG] " << mensaje << endl;
        }
    }
    
    ~Logger() {
        if (logFile.is_open()) {
            logFile.close();
        }
    }
};

Logger* Logger::instance = nullptr;

int main() {
    cout << "=== DESARROLLO 1: SINGLETON - LOGGER ===" << endl;
    
    Logger* logger1 = Logger::getInstance();
    Logger* logger2 = Logger::getInstance();
    
    cout << "Son la misma instancia? " << (logger1 == logger2 ? "SI" : "NO") << endl;
    
    logger1->log("Aplicacion iniciada");
    logger1->log("Usuario admin logueado");
    logger2->log("Consulta ejecutada");
    
    return 0;
}

/**
 * COMPILAR: g++ -std=c++11 desarrollo1_singleton_logger.cpp -o logger
 * EJECUTAR: ./logger
 */
