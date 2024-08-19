import pywhatkit
from datetime import datetime, timedelta
import time
import logging

# Configuración del log
logging.basicConfig(filename='whatsapp_sender.log', level=logging.INFO, format='%(asctime)s - %(message)s')

class WhatsAppSender:
    def __init__(self):
        self.current_time = datetime.now()

    def get_future_time(self, minutes=1):
        return datetime.now() + timedelta(minutes=minutes)

    def log_message(self, receiver, message, success):
        status = 'Success' if success else 'Failure'
        logging.info(f"Receiver: {receiver}, Message: {message}, Status: {status}")

    def send_message(self, receiver, message, future_time, image_path=None):
        try:
            print(f"Enviando mensaje a {receiver} a las {future_time.hour}:{future_time.minute}")
            if image_path:
                pywhatkit.sendwhats_image(receiver, image_path, message, future_time.hour, future_time.minute)
            else:
                pywhatkit.sendwhatmsg(receiver, message, future_time.hour, future_time.minute)
            time.sleep(10)  # Espera para asegurar que el mensaje se envíe
            print("Se envió correctamente el mensaje")
            self.log_message(receiver, message, True)
        except Exception as e:
            print(f"Error al enviar el mensaje a {receiver}: {e}")
            self.log_message(receiver, message, False)

    def send_group_message(self, group_id, message, future_time, image_path=None):
        try:
            print(f"Enviando mensaje al grupo {group_id} a las {future_time.hour}:{future_time.minute}")
            if image_path:
                pywhatkit.sendwhats_image(group_id, image_path, message, future_time.hour, future_time.minute, is_group=True)
            else:
                pywhatkit.sendwhatmsg_to_group(group_id, message, future_time.hour, future_time.minute)
            time.sleep(10)  # Espera para asegurar que el mensaje se envíe
            print("Se envió correctamente el mensaje al grupo")
            self.log_message(group_id, message, True)
        except Exception as e:
            print(f"Error al enviar el mensaje al grupo {group_id}: {e}")
            self.log_message(group_id, message, False)

    def send_messages_to_list(self, receivers, message, image_path=None):
        for i, receiver in enumerate(receivers):
            future_time = self.get_future_time(minutes=i+1)  # Añade 1 minuto entre cada mensaje
            self.send_message(receiver, message, future_time, image_path)

    def send_group_messages_to_list(self, group_ids, message, image_path=None):
        for i, group_id in enumerate(group_ids):
            future_time = self.get_future_time(minutes=i+1)  # Añade 1 minuto entre cada mensaje
            self.send_group_message(group_id, message, future_time, image_path)


# Uso de la clase WhatsAppSender
sender = WhatsAppSender()


# Enviar mensaje a una lista de números individuales
phone_numbers = ['+5356068764', '+5354700189']
sender.send_messages_to_list(phone_numbers, 'Hola princesa este mensaje no lo escribi con el movil')

# Enviar mensaje a una lista de grupos
group_ids = ['EfEN7MgUZdU3wX2a850j4p', 'I9ieIGTxCkD9wKEpfM9cr6']
sender.send_group_messages_to_list(group_ids, 'mensaje de prueba de automatizacion de whatsapp')

print("Se envio correctamente el mensaje")
