import pywhatkit
from datetime import datetime, timedelta
import time

# Obtén el tiempo actual y añade un minuto para el envío
current_time = datetime.now()
future_time = current_time + timedelta(minutes=1)  # Añade 1 minuto

# Imprime la hora y los minutos futuros para verificar
print(f"Hora futura: {future_time.hour}, Minuto futuro: {future_time.minute}")

# Configuración del mensaje
receiver = '+5354700189'
msg = 'Hola princesa este mensaje no lo escribi con el movil'

# Envía el mensaje
pywhatkit.sendwhatmsg(receiver, msg, future_time.hour, future_time.minute)
time.sleep(10)
print("Se envio correctamente el mensaje")


# Obtén el tiempo actual y añade un minuto para el envío
current_time = datetime.now()
future_time = current_time + timedelta(minutes=1)  # Añade 1 minuto
pywhatkit.sendwhatmsg_to_group(group_id='EfEN7MgUZdU3wX2a850j4p',
                               message='mensaje de prueba de automatizacion de whatsapp',
                               time_hour=future_time.hour,
                               time_min=future_time.minute)

'''
edge_options = Options()
driver = webdriver.Edge(options=edge_options)
chat = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p')
chat.send_keys(Keys.ENTER)
'''