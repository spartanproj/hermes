import socket,sys

from threading import Thread
connected=set()


def on_new_client(client_socket, addr):
    while True:
        data = client_socket.recv(1024).decode('utf-8').split("<~~>")
        lastuser=lastuser if data[0]=="" else data[1]
        try:
            connected.add(data[1])
            if not data[0]:
                connected.remove(data[1])#
            log=open("chat.log","a")
            log.write(f"{addr[0]} >> {data[0]}\n")
            log.close()

            log=open("chat.log","r")
            client_socket.send(log.read().encode())
            log.close()
        except:
            connected.remove(lastuser)
            client_socket.close()
            break
    

def main():
    host = '0.0.0.0'  # allow any incoming connections
    port = 8082

    s = socket.socket()
    s.bind((host, port))  # bind the socket to the port and ip address

    s.listen(5)  # wait for new connections

    while True:
        c, addr = s.accept()  # Establish connection with client.
        # this returns a new socket object and the IP address of the client
        print(f"New connection from: {addr}")
        thread = Thread(target=on_new_client, args=(c, addr))  # create the thread
        thread.start()  # start the thread
    c.close()
    thread.join()

if __name__ == '__main__':
    main()