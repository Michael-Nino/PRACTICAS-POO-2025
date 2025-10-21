"""
DESARROLLO 2: Factory en Python - Sistema de Notificaciones
(EJERCICIO NUEVO - NO es el ejemplo del PDF de transportes)
"""

from abc import ABC, abstractmethod


class Notificacion(ABC):
    @abstractmethod
    def enviar(self, destinatario, mensaje):
        pass


class EmailNotificacion(Notificacion):
    def enviar(self, destinatario, mensaje):
        print(f"Enviando EMAIL a {destinatario}: {mensaje}")
        return True


class SMSNotificacion(Notificacion):
    def enviar(self, destinatario, mensaje):
        print(f"Enviando SMS a {destinatario}: {mensaje[:50]}")
        return True


class PushNotificacion(Notificacion):
    def enviar(self, destinatario, mensaje):
        print(f"Enviando PUSH a {destinatario}: {mensaje}")
        return True


class NotificacionFactory:
    @staticmethod
    def crear_notificacion(tipo):
        if tipo == "email":
            return EmailNotificacion()
        elif tipo == "sms":
            return SMSNotificacion()
        elif tipo == "push":
            return PushNotificacion()
        else:
            raise ValueError(f"Tipo '{tipo}' no soportado")


def main():
    print("=== DESARROLLO 2: FACTORY - NOTIFICACIONES ===\n")
    
    # Crear diferentes notificaciones
    email = NotificacionFactory.crear_notificacion("email")
    sms = NotificacionFactory.crear_notificacion("sms")
    push = NotificacionFactory.crear_notificacion("push")
    
    # Enviar mensajes
    email.enviar("admin@empresa.com", "Alerta de seguridad")
    sms.enviar("987654321", "Codigo de verificacion: 123456")
    push.enviar("device_001", "Nueva notificacion disponible")


if __name__ == "__main__":
    main()

"""
EJECUTAR: python3 desarrollo2_factory_notificaciones.py
"""
