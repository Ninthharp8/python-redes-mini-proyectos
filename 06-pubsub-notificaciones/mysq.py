import zmq
import mysql.connector

def server():
    # Verificar la conexión a la base de datos MySQL
    try:
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="mensajes"
        )
        cursor = db_connection.cursor()
        print("Conexión a la base de datos exitosa.")
        
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        return

    print("Servidor escuchando")
    
    # Insertar un nuevo mensaje
    topic = input("Topic: ")
    message = input("Message: ")
    cursor.execute("INSERT INTO mensajes (tema, mensaje) VALUES (%s, %s)", (topic, message))
    print("Nuevo mensaje insertado.")

    # Hacer commit para guardar los cambios en la base de datos
    db_connection.commit()

if __name__ == "__main__":
    server()
