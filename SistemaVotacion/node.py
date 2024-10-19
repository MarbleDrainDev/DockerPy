import socket

def iniciar_nodo():
    nodo = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    nodo.bind(('0.0.0.0', 5000))  # Todos los nodos escuchan en el puerto 5000
    nodo.listen(5)

    print("Nodo iniciado y escuchando en el puerto 5000")

    while True:
        cliente, direccion = nodo.accept()
        print(f'Conexión recibida de {direccion}')
        datos = cliente.recv(1024).decode()
        print(f'Datos recibidos: {datos}')
        cliente.sendall(f'Confirmación recibida'.encode())
        cliente.close()

if __name__ == "__main__":
    iniciar_nodo()
