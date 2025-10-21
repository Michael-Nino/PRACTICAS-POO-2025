/*
 * DESARROLLO 3: Command para editor de texto con guardar y deshacer
 * (EJERCICIO NUEVO - NO es el ejemplo del PDF)
 */

#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Editor;

class Command {
public:
    virtual void ejecutar() = 0;
    virtual void deshacer() = 0;
};

class Editor {
public:
    string contenido;
    vector<Command*> historial;
    
    Editor() : contenido("") {}
    
    void ejecutar(Command* comando) {
        comando->ejecutar();
        historial.push_back(comando);
    }
    
    void deshacer() {
        if (!historial.empty()) {
            Command* comando = historial.back();
            historial.pop_back();
            comando->deshacer();
        }
    }
};

class EscribirCommand : public Command {
private:
    Editor* editor;
    string texto;
    string backup;
    
public:
    EscribirCommand(Editor* e, const string& t) : editor(e), texto(t) {}
    
    void ejecutar() override {
        backup = editor->contenido;
        editor->contenido += texto;
        cout << "Escrito: " << texto << endl;
    }
    
    void deshacer() override {
        editor->contenido = backup;
        cout << "Deshecho" << endl;
    }
};

int main() {
    Editor editor;
    
    EscribirCommand cmd1(&editor, "Hola ");
    EscribirCommand cmd2(&editor, "Mundo");
    
    editor.ejecutar(&cmd1);
    editor.ejecutar(&cmd2);
    cout << "Contenido: " << editor.contenido << endl;
    
    editor.deshacer();
    cout << "Despues de deshacer: " << editor.contenido << endl;
    
    return 0;
}
