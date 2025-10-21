"""
DESARROLLO 1: Observer para sistema de chat
(EJERCICIO NUEVO - NO es el ejemplo del PDF)
"""


class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def recibir_mensaje(self, mensaje):
        print(f"{self.nombre} recibio: {mensaje}")


class Chat:
    def __init__(self):
        self.usuarios = []
    
    def unirse(self, usuario):
        self.usuarios.append(usuario)
        print(f"{usuario.nombre} se unio al chat")
    
    def enviar_mensaje(self, mensaje):
        for u in self.usuarios:
            u.recibir_mensaje(mensaje)


chat = Chat()
u1 = Usuario("Juan")
u2 = Usuario("Maria")
chat.unirse(u1)
chat.unirse(u2)
chat.enviar_mensaje("Hola a todos!")
