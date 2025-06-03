import socket
import threading
import mysql.connector

# Configuración de la base de datos MySQL
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mensajes"
)

db_cursor = db_connection.cursor()
# Lista para almacenar las conexiones de los suscriptores
subscribers = []

# Función para manejar las conexiones de los clientes
def handle_subscriber(subscriber_socket):
        print("se ejecuta suscripcion")
        try:
            topic = subscriber_socket[1]
            if topic.lower() =="exit": 
                return exit()
            sql = "SELECT * FROM mensajes WHERE tema = %s"
            db_cursor.execute(sql, (topic,))
            messages = db_cursor.fetchall()
            for message in messages:
                client.send(f"Tema: {message[0]}, Mensaje: {message[1]}".encode())
        except Exception as e:
            print(f"Error en el manejo del suscriptor: {e}")
            
    # Al suscribirse, enviar todos los mensajes almacenados en la base de datos
        for message in messages:
            print("mensaje almacenado: ")
            client.send(f"Tema: {message[0]}, Mensaje: {message[1]}".encode())
        subscribers.remove(client)
        client.close()
        print("Se ejecuto subscriber")


# Función para manejar las conexiones de los publicadores
def handle_publisher(publisher_socket):
        try:
            topic, message =publisher_socket[1],publisher_socket[2]
            if topic.lower() =="exit": 
                return exit()
            # Guardar en la base de datos
            sql = "INSERT INTO mensajes (tema, mensaje) VALUES (%s, %s)"
            values = (topic, message)
            db_cursor.execute(sql, values)
            db_connection.commit()
            print(f"[Nuevo mensaje recibido] Tema: {topic}, Mensaje: {message}")
            # Envía el mensaje a los suscriptores activos
            for subscriber in subscribers:
                try:
                    subscriber.send(f"Tema: {topic}, Mensaje: {message}".encode())
                except:
                    subscribers.remove(subscriber)
        except Exception as e:
            print(f"Error en el manejo del publicador: {e}")


# Configuración del servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 9999))
server.listen(5)
print("[Servidor iniciado] Esperando conexiones...")
# Aceptar conexiones entrantes
while True:
    client, addr = server.accept()
    print(f"[Nueva conexión] {addr[0]}:{addr[1]}")
    data = client.recv(1024).decode().split('|')
    if data[0] == f"subscriber":
        subscribers.append(client)
        threading.Thread(target=handle_subscriber, args=(data,)).start()
    elif data[0] == "publisher":
        threading.Thread(target=handle_publisher, args=(data,)).start()
        
