import echo_util
import threading

HOST = echo_util.HOST
PORT = echo_util.PORT

conect = {}
alegere = {}
player_number = 1

rules = {
"piatra": {"piatra": "castig", "hartie": "pierdere", "foarfeca": "castig"},
"hartie": {"piatra": "castig", "hartie": "egalitate", "foarfeca": "pierdere"},
"foarfeca": {"piatra": "pierdere", "hartie": "castig", "foarfeca": "egalitate"}
}
def castig(p1, p2):
    if p1 == p2:
        return "egalitate"
    elif rules[p1][p2] == "castig":
        return "player1"
    else: 
        return "player2"

def handle_client(sock, addr, player):
    """ Receive data from the client via sock and echo it back """
    echo_util.send_msg(sock,player)
    while True:
        try:
            msg = echo_util.recv_msg(sock) # Blocks until received
            print('{}: {}'.format(addr, msg))
            if not msg or msg == 'q':
                
                for i, j in conect.items():
                    echo_util.send_msg(j,"q")
                    
            else:
                alegere [player] = msg
                if len(alegere) == 2:
                    castigator = castig(alegere["player1"], alegere["player2"])
                    for i, j in conect.items():
                        echo_util.send_msg(j,"Castigator: " + castigator)
                    alegere.clear()
     
        except (ConnectionError, BrokenPipeError):
            print('Closed connection to {}'.format(addr))
            sock.close()
            break
    del conect[player]


if __name__ == '__main__':
    listen_sock = echo_util.create_listen_socket(HOST, PORT)
    addr = listen_sock.getsockname()
    print('Listening on {}'.format(addr))

    while len(conect) < 2:
        client_sock, addr = listen_sock.accept()
        player = f"player{player_number}"
        conect[player] = client_sock
        print(f"{player} Conected")
        
        thread = threading.Thread(target = handle_client, args = [client_sock, addr,player], daemon=True)
        thread.start()
        player_number += 1
    while len(conect) > 0:
        pass
    listen_sock.close()