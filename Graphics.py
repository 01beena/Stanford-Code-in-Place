from graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
BOX_SIZE = 80  # Size of each box
from graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
BOX_SIZE = 80  # Size of each box

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Draw a line of boxes
    for i in range(5):
        left_x = i * BOX_SIZE
        top_y = CANVAS_HEIGHT - BOX_SIZE  # Align boxes at the bottom of the canvas
        right_x = left_x + BOX_SIZE
        bottom_y = CANVAS_HEIGHT
        
        canvas.create_rectangle(left_x, top_y, right_x, bottom_y, "white", "black")
    
    # No need to call canvas.display() if not displaying interactively

if __name__ == '__main__':
    main()

