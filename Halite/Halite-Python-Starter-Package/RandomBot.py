import hlt
from hlt import NORTH, EAST, SOUTH, WEST, STILL, Move, Square
import random


myID, game_map = hlt.get_init()
hlt.send_init("Best Bot")

def assign_move(square):
    for direction, neighbor in enumerate(game_map.neighbors(square)):
        if neighbor.owner != myID and neighbor.strength < square.strength and neighbor.production > square.production:
            return Move(square, direction)
        if neighbor.owner != myID and neighbor.strength < square.strength:
            return Move(square, direction)
        if neighbor.owner != myID and neighbor.strength < square.strength + square.production:
            return Move(square, STILL)
    if square.strength < 5 * square.production:
        return Move(square, STILL)
    elif square.strength == 255:
        return Move(square, EAST)
    else:
        return Move(square, random.choice((NORTH, STILL)))

while True:
    game_map.get_frame()
    moves = [assign_move(square) for square in game_map if square.owner == myID]
    hlt.send_frame(moves)
