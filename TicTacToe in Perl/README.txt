There are two codes. One is TicTacToe.pl which is the one to be played with the computer.
The other one is TicTacToe_Multiplayer.pl which is a two player game.

The file is to be executed as perl TicTacToe.pl or perl TicTacToe_Multiplayer.pl

1) The TicTacToe_Multiplayer.pl contains a class Player.pm which gives us two objects i.e. the players. The code runs for any numerical inputs and will ask again in case of an invalid input. The code runs till there is a winner or a tie.

2) The TicTacToe.pl contains two classes. One is Player.pm which creates the object of the user and the other is a derived class from this called Comp.pm. This class generates a non-repeating ramdom number between 0 to 9 (Implemented by storing these numbers in a list and splicing whenever number is used) and marks a 'O' over there. The code runs for any numerical inputs and will ask again in case of an invalid input. The game continues till there is a winner or it ends in a tie.
