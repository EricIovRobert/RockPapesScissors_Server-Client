# RockPapesScissors_Server-Client

Rock, Paper, Scissors is a classic game that I've also implemented in Python! It can be played by 2 players using a server and 2 clients.

Here's a brief overview of how the game works:

Server: The server manages the game logic and communication between the two clients. It waits for both clients to connect before starting the game.
Clients: Each client represents one player. They connect to the server and then take turns making their move by selecting either rock, paper, or scissors.
Game Logic: After both players make their moves, the server determines the winner based on the rules of the game. It then sends the result back to both clients, informing them of the winner or if it's a tie.
Continuation: The game continues with each player making new moves until one player wins a round or the players decide to quit.
This setup allows for an interactive multiplayer experience where players can compete against each other remotely. It's a fun project to implement and play with friends
