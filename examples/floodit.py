from guizero import App, Waffle, Text, PushButton, info
import random

# Set up the game - colours, width and height of board and no of moves allowed
colours = ["red", "blue", "green", "yellow", "fuchsia", "purple"]
b_width = 14
b_height = 14
moves_limit = 25


# Set up the palette
def init_palette():
    [palette.set_pixel(colours.index(c), 0, c) for c in colours]

# Fill the board with coloured regions
def fill_board():
    [board.set_pixel(x, y, random.choice(colours)) for y in range(b_height) for x in range(b_width)]

# Find and flood any squares next to this
def begin_flood(x, y):
    replacement = palette.get_pixel(x,y)
    target = board.get_pixel(0,0)
    flood(0, 0, target, replacement)
    win_check()

# Recursively floods adjacent squares
def flood(x, y, target, replacement):
    # Algorithm from https://en.wikipedia.org/wiki/Flood_fill
    if target == replacement:
        return False
    if board.get_pixel(x, y) != target:
        return False
    board.set_pixel(x, y, replacement)
    if y+1 <= b_height-1:   # South
        flood(x, y+1, target, replacement)
    if y-1 >= 0:            # North
        flood(x, y-1, target, replacement)
    if x+1 <= b_width-1:    # East
        flood(x+1, y, target, replacement)
    if x-1 >= 0:            # West
        flood(x-1, y, target, replacement)

# Check if there are any moves left or if they won
def win_check():
    moves_left = int(moves_text.value)-1
    moves_text.value = moves_left   # Update moves left
    if moves_left > 0:
        squares = board.get_all()
        if all(colour == squares[0] for colour in squares):
            win_text.value = "Winner!"
            reset.visible = True
            palette.disable()
    else:
        win_text.value = "No more moves left!"
        reset.visible = True
        palette.disable()

# Reset the board and remove the win text/reset button
def reset_board():
    reset.visible = False
    win_text.value = ""
    moves_text.value = moves_limit
    init_palette()
    fill_board()
    palette.enable()



# Set up the game board
app = App("Flood it")

board = Waffle(app, width=b_width, height=b_width, pad=0)
palette = Waffle(app, width=len(colours), height=1, command=begin_flood, dotty=True)
moves_left = Text(app, text="Moves left:")
moves_text = Text(app, text=moves_limit)

# Win text and reset button (initially invisible)
win_text = Text(app)
reset = PushButton(app, text="Start again", command=reset_board)
reset.visible = False

# Initialise the palette and the random board pattern
init_palette()
fill_board()

# Instructions
instructions = PushButton(app, command=info, args=["Instructions", "Click a dot to flood the grid with that colour, beginning from the top left square. You have 25 moves to flood all squares on the grid with the same colour."], text="Instructions")

app.display()
