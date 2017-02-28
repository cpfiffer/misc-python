import hlt
from hlt import NORTH, EAST, SOUTH, WEST, STILL, Move, Square
import random


myID, game_map = hlt.get_init()
hlt.send_init("MyPythonBot")

def assign_move(square):
    if square.strength == 0:
        return Move(square, STILL)
    for direction, neighbor in enumerate(game_map.neighbors(square)):
        if neighbor.owner != myID and neighbor.strength < square.strength and neighbor.production > square.production:
            return Move(square, direction)
        if neighbor.owner != myID and neighbor.strength < square.strength and neighbor.production != 0:
            return Move(square, direction)
    if neighbor.owner == myID and neighbor.strength != 0 and square.strength <= 100 and neighbor.strength <= square.strength:
        return Move(square, random.choice((STILL, direction)))
    if square.strength >= 100:
        direction = NORTH
        max_distance = min(game_map.width, game_map.height) / 2
        for d in (NORTH, EAST, SOUTH, WEST):
            distance = 0
            current = square
            while current.owner == myID and distance < max_distance:
                distance += 1
                current = game_map.get_target(current, d)
            if distance < max_distance:
                direction = d
                max_distance = distance
        return Move(square,direction)


    if square.strength < 3 * square.production:
        return Move(square, STILL)
    for direction, neighbor in enumerate(game_map.neighbors(square)):
        if neighbor.owner == myID and square.strength + square.production < neighbor.strength:
            return Move(square, direction)
        else:
            return Move(square, random.choice((STILL, NORTH)))

while True:
    game_map.get_frame()
    moves = [assign_move(square) for square in game_map if square.owner == myID]
    hlt.send_frame(moves)
