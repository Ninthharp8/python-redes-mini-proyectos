import socket

server_address = ('localhost', 9999)

def subscribe(topic):
    # iniciamos el socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect(server_address)
        role = "subscriber"
        client.send(f"{role}|{topic}".encode())
        print(f"Topic enviado : {topic}")
        while True:
            message = client.recv(1024).decode()
            if not message:
                break
            print(message)

if __name__ == "__main__":

    while True:
        topic = input("Ingrese el tema al que desea suscribirse ('exit' para terminar): ")
        if topic.lower() == 'exit':
            break
        subscribe(topic)
       
