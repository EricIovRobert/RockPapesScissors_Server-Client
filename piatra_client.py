import sys, socket
import echo_util

HOST = sys.argv[-1] if len(sys.argv) > 1 else '127.0.0.1'
PORT = echo_util.PORT

if __name__ == '__main__':
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))  #connect to server
    except ConnectionError:
        print('Socket error on connection')
        sys.exit(1)
    msg = echo_util.recv_msg(sock)
    print('\nConnected to {}:{}'.format(HOST, PORT))
    print("Type message, enter to send, 'q' to quit")
    print(msg)

    while True:
        print("Alegere: ", end = '')
        msg = input()
        if not msg:
            continue

        if msg == 'q': 
            echo_util.send_msg(sock, msg)
            break

        
        if msg == "piatra" or msg == "hartie" or msg == "foarfeca":
            try:
                echo_util.send_msg(sock, msg) # Blocks until sent
                print('Sent message: {}'.format(msg))
                msg = echo_util.recv_msg(sock)
                if msg == "q":
                    print ("Unul dintre playeri s-a deconectat, vei fi deconectat si tu!")
                    break
                    sock.close()
                
                print(msg)
                
            except ConnectionError:
                print('Socket error during communication')
                sock.close()
                print('Closed connection to server\n')
                break
        
        else:
            print ('Nu ai introdus una dintre optiunile valide: piatra, hartie, foarfeca sau q!')

    print("Closing connection")
    sock.close()