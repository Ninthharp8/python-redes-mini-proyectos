import socket

server_address = ('localhost', 9999)

def publish(topic, message):
        # abrimos un socket para mandar la informacion por el.
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect(server_address) 
            # asignamos la informacion junto con el rol
            role="publisher"
            client.send(f"{role}|{topic}|{message}".encode())
            print("[Publicación exitosa]")
            
if __name__ == "__main__":
    while True:
        topic = input("Ingrese el tema ('exit' para terminar): ")
        if topic.lower() == 'exit':
            publish("exit", "")
            break
        message = input("Ingrese el mensaje: ")
        publish(topic, message)
