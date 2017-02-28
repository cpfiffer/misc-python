import hlt
from hlt import NORTH, EAST, SOUTH, WEST, STILL, Move, Square
import random


myID, game_map = hlt.get_init()
hlt.send_init("Stronghold")

def assign_move(square):
    if square.strength == 0:
        return Move(square, STILL)
    for direction, neighbor in enumerate(game_map.neighbors(square)):
        if square.strength >= 150 and neighbor.strength < square.strength:
            return Move(square, direction)

while True:
    game_map.get_frame()
    moves = [assign_move(square) for square in game_map if square.owner == myID]
    hlt.send_frame(moves)
