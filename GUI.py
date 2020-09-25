import pygame
import pyraminx
import time

pygame.init()
pygame.display.set_caption('Master Pyraminx GUI')
SCREEN = pygame.display.set_mode((1200, 700))
DONE = False

# Config for updating moves in real time
VISUALIZE_MOVE = False

# Defines for colors
BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (50,214,49)
BLUE = (63,139,253)
YELLOW = (255,252,2)
RED = (228,44,56)
GREY = (211,211,211)

# Stores height and width
WIDTH, HEIGHT = pygame.display.get_surface().get_size()
HALF_WIDTH = WIDTH//2
CLOCK = pygame.time.Clock()
pyraminx = pyraminx.Pyraminx()

def switcher(color):
    switch = {
        "G": GREEN,
        "R": RED,
        "B": BLUE,
        "Y": YELLOW
    }
    return switch.get(color, "Invalid color")
def greenSide():
    # Defines middle triangle outline
    # Format follow as defining solid triangle then drawing outline
    pygame.draw.polygon(SCREEN, BLACK, [[HALF_WIDTH, 200], [HALF_WIDTH - 200, 400], [HALF_WIDTH + 200, 400]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.greenSide[0][0]), [[HALF_WIDTH, 200], [HALF_WIDTH - 50, 250], [HALF_WIDTH + 50, 250]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[HALF_WIDTH, 200], [HALF_WIDTH - 50, 250], [HALF_WIDTH + 50, 250]], 2)

    # Green side row 2 outline and fills
    pygame.draw.polygon(SCREEN, switcher(pyraminx.greenSide[1][0]), [[HALF_WIDTH - 50, 250], [HALF_WIDTH - 100, 300], [HALF_WIDTH, 300]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[HALF_WIDTH - 50, 250], [HALF_WIDTH - 100, 300], [HALF_WIDTH, 300]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.greenSide[1][1]), [[HALF_WIDTH, 300], [HALF_WIDTH - 50, 250], [HALF_WIDTH + 50, 250]], 0)  # inverted triangle
    pygame.draw.polygon(SCREEN, BLACK, [[HALF_WIDTH, 300], [HALF_WIDTH - 50, 250], [HALF_WIDTH + 50, 250]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.greenSide[1][2]), [[HALF_WIDTH + 50, 250], [HALF_WIDTH, 300], [HALF_WIDTH + 100, 300]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[HALF_WIDTH + 50, 250], [HALF_WIDTH, 300], [HALF_WIDTH + 100, 300]], 2)

    # Green side row 3 outline and fills
    pygame.draw.polygon(SCREEN, switcher(pyraminx.greenSide[2][0]), [[HALF_WIDTH - 100, 300], [HALF_WIDTH - 150, 350], [HALF_WIDTH - 50, 350]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[HALF_WIDTH - 100, 300], [HALF_WIDTH - 150, 350], [HALF_WIDTH - 50, 350]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.greenSide[2][1]), [[HALF_WIDTH - 50, 350], [HALF_WIDTH - 100, 300], [HALF_WIDTH, 300]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[HALF_WIDTH - 50, 350], [HALF_WIDTH - 100, 300], [HALF_WIDTH, 300]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.greenSide[2][2]), [[HALF_WIDTH, 300], [HALF_WIDTH - 50, 350], [HALF_WIDTH + 50, 350]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[HALF_WIDTH, 300], [HALF_WIDTH - 50, 350], [HALF_WIDTH + 50, 350]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.greenSide[2][3]), [[HALF_WIDTH + 50, 350], [HALF_WIDTH, 300], [HALF_WIDTH + 100, 300]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[HALF_WIDTH + 50, 350], [HALF_WIDTH, 300], [HALF_WIDTH + 100, 300]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.greenSide[2][4]), [[HALF_WIDTH + 100, 300], [HALF_WIDTH + 50, 350], [HALF_WIDTH + 150, 350]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[HALF_WIDTH + 100, 300], [HALF_WIDTH + 50, 350], [HALF_WIDTH + 150, 350]], 2)

    # Green side row 4 outline and fills
    pygame.draw.polygon(SCREEN, switcher(pyraminx.greenSide[3][0]), [[HALF_WIDTH - 150, 350], [HALF_WIDTH - 200, 400], [HALF_WIDTH - 100, 400]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[HALF_WIDTH - 150, 350], [HALF_WIDTH - 200, 400], [HALF_WIDTH - 100, 400]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.greenSide[3][1]), [[HALF_WIDTH - 100, 400], [HALF_WIDTH - 150, 350], [HALF_WIDTH - 50, 350]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[HALF_WIDTH - 100, 400], [HALF_WIDTH - 150, 350], [HALF_WIDTH - 50, 350]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.greenSide[3][2]), [[HALF_WIDTH - 50, 350], [HALF_WIDTH - 100, 400], [HALF_WIDTH, 400]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[HALF_WIDTH - 50, 350], [HALF_WIDTH - 100, 400], [HALF_WIDTH, 400]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.greenSide[3][3]), [[HALF_WIDTH, 400], [HALF_WIDTH - 50, 350], [HALF_WIDTH + 50, 350]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[HALF_WIDTH, 400], [HALF_WIDTH - 50, 350], [HALF_WIDTH + 50, 350]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.greenSide[3][4]), [[HALF_WIDTH + 50, 350], [HALF_WIDTH + 100, 400], [HALF_WIDTH, 400]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[HALF_WIDTH + 50, 350], [HALF_WIDTH + 100, 400], [HALF_WIDTH, 400]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.greenSide[3][5]), [[HALF_WIDTH + 100, 400], [HALF_WIDTH + 150, 350], [HALF_WIDTH + 50, 350]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[HALF_WIDTH + 100, 400], [HALF_WIDTH + 150, 350], [HALF_WIDTH + 50, 350]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.greenSide[3][6]), [[HALF_WIDTH + 150, 350], [HALF_WIDTH + 200, 400], [HALF_WIDTH + 100, 400]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[HALF_WIDTH + 150, 350], [HALF_WIDTH + 200, 400], [HALF_WIDTH + 100, 400]], 2)

def blueSide():
    offset = HALF_WIDTH + 400
    # Defines middle triangle outline
    # Format follow as defining solid triangle then drawing outline
    pygame.draw.polygon(SCREEN, BLACK, [[HALF_WIDTH + 400, 200], [HALF_WIDTH + 600, 400], [HALF_WIDTH + 200, 400]], 2)  # Center Triangle

    pygame.draw.polygon(SCREEN, switcher(pyraminx.blueSide[0][0]), [[offset, 200], [offset - 50, 250], [offset + 50, 250]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[offset, 200], [offset - 50, 250], [offset + 50, 250]], 2)

    # Green side row 2 outline and fills
    pygame.draw.polygon(SCREEN, switcher(pyraminx.blueSide[1][0]), [[offset - 50, 250], [offset - 100, 300], [offset, 300]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[offset - 50, 250], [offset - 100, 300], [offset, 300]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.blueSide[1][1]), [[offset, 300], [offset - 50, 250], [offset + 50, 250]], 0)  # inverted triangle
    pygame.draw.polygon(SCREEN, BLACK, [[offset, 300], [offset - 50, 250], [offset + 50, 250]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.blueSide[1][2]), [[offset + 50, 250], [offset, 300], [offset + 100, 300]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[offset + 50, 250], [offset, 300], [offset + 100, 300]], 2)

    # Green side row 3 outline and fills
    pygame.draw.polygon(SCREEN, switcher(pyraminx.blueSide[2][0]), [[offset - 100, 300], [offset - 150, 350], [offset - 50, 350]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[offset - 100, 300], [offset - 150, 350], [offset - 50, 350]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.blueSide[2][1]), [[offset - 50, 350], [offset - 100, 300], [offset, 300]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[offset - 50, 350], [offset - 100, 300], [offset, 300]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.blueSide[2][2]), [[offset, 300], [offset - 50, 350], [offset + 50, 350]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[offset, 300], [offset - 50, 350], [offset + 50, 350]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.blueSide[2][3]), [[offset + 50, 350], [offset, 300], [offset + 100, 300]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[offset + 50, 350], [offset, 300], [offset + 100, 300]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.blueSide[2][4]), [[offset + 100, 300], [offset + 50, 350], [offset + 150, 350]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[offset + 100, 300], [offset + 50, 350], [offset + 150, 350]], 2)

    # Green side row 4 outline and fills
    pygame.draw.polygon(SCREEN, switcher(pyraminx.blueSide[3][0]), [[offset - 150, 350], [offset - 200, 400], [offset - 100, 400]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[offset - 150, 350], [offset - 200, 400], [offset - 100, 400]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.blueSide[3][1]), [[offset - 100, 400], [offset - 150, 350], [offset - 50, 350]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[offset - 100, 400], [offset - 150, 350], [offset - 50, 350]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.blueSide[3][2]), [[offset - 50, 350], [offset - 100, 400], [offset, 400]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[offset - 50, 350], [offset - 100, 400], [offset, 400]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.blueSide[3][3]), [[offset, 400], [offset - 50, 350], [offset + 50, 350]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[offset, 400], [offset - 50, 350], [offset + 50, 350]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.blueSide[3][4]), [[offset + 50, 350], [offset + 100, 400], [offset, 400]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[offset + 50, 350], [offset + 100, 400], [offset, 400]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.blueSide[3][5]), [[offset + 100, 400], [offset + 150, 350], [offset + 50, 350]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[offset + 100, 400], [offset + 150, 350], [offset + 50, 350]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.blueSide[3][6]), [[offset + 150, 350], [offset + 200, 400], [offset + 100, 400]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[offset + 150, 350], [offset + 200, 400], [offset + 100, 400]], 2)

def redSide():
    offset = HALF_WIDTH - 400
    # Defines middle triangle outline
    # Format follow as defining solid triangle then drawing outline
    pygame.draw.polygon(SCREEN, BLACK, [[HALF_WIDTH - 400, 200], [HALF_WIDTH-600, 400], [HALF_WIDTH - 200, 400]], 2)   # Left Triangle

    pygame.draw.polygon(SCREEN, switcher(pyraminx.redSide[0][0]), [[offset, 200], [offset - 50, 250], [offset + 50, 250]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[offset, 200], [offset - 50, 250], [offset + 50, 250]], 2)

    # Green side row 2 outline and fills
    pygame.draw.polygon(SCREEN, switcher(pyraminx.redSide[1][0]), [[offset - 50, 250], [offset - 100, 300], [offset, 300]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[offset - 50, 250], [offset - 100, 300], [offset, 300]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.redSide[1][1]), [[offset, 300], [offset - 50, 250], [offset + 50, 250]], 0)  # inverted triangle
    pygame.draw.polygon(SCREEN, BLACK, [[offset, 300], [offset - 50, 250], [offset + 50, 250]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.redSide[1][2]), [[offset + 50, 250], [offset, 300], [offset + 100, 300]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[offset + 50, 250], [offset, 300], [offset + 100, 300]], 2)

    # Green side row 3 outline and fills
    pygame.draw.polygon(SCREEN, switcher(pyraminx.redSide[2][0]), [[offset - 100, 300], [offset - 150, 350], [offset - 50, 350]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[offset - 100, 300], [offset - 150, 350], [offset - 50, 350]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.redSide[2][1]), [[offset - 50, 350], [offset - 100, 300], [offset, 300]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[offset - 50, 350], [offset - 100, 300], [offset, 300]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.redSide[2][2]), [[offset, 300], [offset - 50, 350], [offset + 50, 350]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[offset, 300], [offset - 50, 350], [offset + 50, 350]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.redSide[2][3]), [[offset + 50, 350], [offset, 300], [offset + 100, 300]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[offset + 50, 350], [offset, 300], [offset + 100, 300]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.redSide[2][4]), [[offset + 100, 300], [offset + 50, 350], [offset + 150, 350]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[offset + 100, 300], [offset + 50, 350], [offset + 150, 350]], 2)

    # Green side row 4 outline and fills
    pygame.draw.polygon(SCREEN, switcher(pyraminx.redSide[3][0]), [[offset - 150, 350], [offset - 200, 400], [offset - 100, 400]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[offset - 150, 350], [offset - 200, 400], [offset - 100, 400]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.redSide[3][1]), [[offset - 100, 400], [offset - 150, 350], [offset - 50, 350]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[offset - 100, 400], [offset - 150, 350], [offset - 50, 350]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.redSide[3][2]), [[offset - 50, 350], [offset - 100, 400], [offset, 400]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[offset - 50, 350], [offset - 100, 400], [offset, 400]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.redSide[3][3]), [[offset, 400], [offset - 50, 350], [offset + 50, 350]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[offset, 400], [offset - 50, 350], [offset + 50, 350]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.redSide[3][4]), [[offset + 50, 350], [offset + 100, 400], [offset, 400]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[offset + 50, 350], [offset + 100, 400], [offset, 400]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.redSide[3][5]), [[offset + 100, 400], [offset + 150, 350], [offset + 50, 350]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[offset + 100, 400], [offset + 150, 350], [offset + 50, 350]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.redSide[3][6]), [[offset + 150, 350], [offset + 200, 400], [offset + 100, 400]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[offset + 150, 350], [offset + 200, 400], [offset + 100, 400]], 2)
def yellowSide():
    # Defines middle triangle outline
    # Format follow as defining solid triangle then drawing outline
    pygame.draw.polygon(SCREEN, BLACK, [[HALF_WIDTH, 600], [HALF_WIDTH - 200, 400], [HALF_WIDTH + 200, 400]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.yellowSide[0][0]), [[HALF_WIDTH, 600], [HALF_WIDTH - 50, 550], [HALF_WIDTH + 50, 550]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[HALF_WIDTH, 600], [HALF_WIDTH - 50, 550], [HALF_WIDTH + 50, 550]], 2)

    # Green side row 2 outline and fills
    pygame.draw.polygon(SCREEN, switcher(pyraminx.yellowSide[1][0]), [[HALF_WIDTH - 50, 550], [HALF_WIDTH - 100, 500], [HALF_WIDTH, 500]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[HALF_WIDTH - 50, 550], [HALF_WIDTH - 100, 500], [HALF_WIDTH, 500]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.yellowSide[1][1]), [[HALF_WIDTH, 500], [HALF_WIDTH - 50, 550], [HALF_WIDTH + 50, 550]], 0)  # inverted triangle
    pygame.draw.polygon(SCREEN, BLACK, [[HALF_WIDTH, 500], [HALF_WIDTH - 50, 550], [HALF_WIDTH + 50, 550]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.yellowSide[1][2]), [[HALF_WIDTH + 50, 550], [HALF_WIDTH, 500], [HALF_WIDTH + 100, 500]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[HALF_WIDTH + 50, 550], [HALF_WIDTH, 500], [HALF_WIDTH + 100, 500]], 2)

    # Green side row 3 outline and fills
    pygame.draw.polygon(SCREEN, switcher(pyraminx.yellowSide[2][0]), [[HALF_WIDTH - 100, 500], [HALF_WIDTH - 150, 450], [HALF_WIDTH - 50, 450]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[HALF_WIDTH - 100, 500], [HALF_WIDTH - 150, 450], [HALF_WIDTH - 50, 450]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.yellowSide[2][1]), [[HALF_WIDTH - 50, 450], [HALF_WIDTH - 100, 500], [HALF_WIDTH, 500]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[HALF_WIDTH - 50, 450], [HALF_WIDTH - 100, 500], [HALF_WIDTH, 500]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.yellowSide[2][2]), [[HALF_WIDTH, 500], [HALF_WIDTH - 50, 450], [HALF_WIDTH + 50, 450]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[HALF_WIDTH, 500], [HALF_WIDTH - 50, 450], [HALF_WIDTH + 50, 450]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.yellowSide[2][3]), [[HALF_WIDTH + 50, 450], [HALF_WIDTH, 500], [HALF_WIDTH + 100, 500]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[HALF_WIDTH + 50, 450], [HALF_WIDTH, 500], [HALF_WIDTH + 100, 500]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.yellowSide[2][4]), [[HALF_WIDTH + 100, 500], [HALF_WIDTH + 50, 450], [HALF_WIDTH + 150, 450]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[HALF_WIDTH + 100, 500], [HALF_WIDTH + 50, 450], [HALF_WIDTH + 150, 450]], 2)

    # Green side row 4 outline and fills

    pygame.draw.polygon(SCREEN, switcher(pyraminx.yellowSide[3][0]), [[HALF_WIDTH - 150, 450], [HALF_WIDTH - 200, 400], [HALF_WIDTH - 100, 400]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[HALF_WIDTH - 150, 450], [HALF_WIDTH - 200, 400], [HALF_WIDTH - 100, 400]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.yellowSide[3][1]), [[HALF_WIDTH - 100, 400], [HALF_WIDTH - 150, 450], [HALF_WIDTH - 50, 450]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[HALF_WIDTH - 100, 400], [HALF_WIDTH - 150, 450], [HALF_WIDTH - 50, 450]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.yellowSide[3][2]), [[HALF_WIDTH - 50, 450], [HALF_WIDTH - 100, 400], [HALF_WIDTH, 400]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[HALF_WIDTH - 50, 450], [HALF_WIDTH - 100, 400], [HALF_WIDTH, 400]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.yellowSide[3][3]), [[HALF_WIDTH, 400], [HALF_WIDTH - 50, 450], [HALF_WIDTH + 50, 450]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[HALF_WIDTH, 400], [HALF_WIDTH - 50, 450], [HALF_WIDTH + 50, 450]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.yellowSide[3][4]), [[HALF_WIDTH + 50, 450], [HALF_WIDTH + 100, 400], [HALF_WIDTH, 400]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[HALF_WIDTH + 50, 450], [HALF_WIDTH + 100, 400], [HALF_WIDTH, 400]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.yellowSide[3][5]), [[HALF_WIDTH + 100, 400], [HALF_WIDTH + 150, 450], [HALF_WIDTH + 50, 450]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[HALF_WIDTH + 100, 400], [HALF_WIDTH + 150, 450], [HALF_WIDTH + 50, 450]], 2)

    pygame.draw.polygon(SCREEN, switcher(pyraminx.yellowSide[3][6]), [[HALF_WIDTH + 150, 450], [HALF_WIDTH + 200, 400], [HALF_WIDTH + 100, 400]], 0)
    pygame.draw.polygon(SCREEN, BLACK, [[HALF_WIDTH + 150, 450], [HALF_WIDTH + 200, 400], [HALF_WIDTH + 100, 400]], 2)

# Displays a grey box on any position of the screen with text on top of box.
def drawBox(box, text):
    pygame.draw.rect(SCREEN, GREY, box)
    textSurface = altFont.render(text, True, BLACK)
    pygame.draw.rect(SCREEN, GREY, box)
    SCREEN.blit(textSurface, box)

# Draws buttons for various moves on the right of the green face.
def moveButtonR(mousePos = None):
    r = pygame.Rect(300, 40, 40, 30)
    drawBox(r, "r")
    rI = pygame.Rect(342, 40, 40, 30)
    drawBox(rI, "r`")
    rr = pygame.Rect(384, 40, 40, 30)
    drawBox(rr, "rr")
    rrI = pygame.Rect(426, 40, 40, 30)
    drawBox(rrI, "rr`")
    rrr = pygame.Rect(468, 40, 40, 30)
    drawBox(rrr, "rrr")
    rrrI = pygame.Rect(510, 40, 40, 30)
    drawBox(rrrI, "rrr`")
    R = pygame.Rect(552, 40, 40, 30)
    drawBox(R, "R")
    RI = pygame.Rect(594, 40, 40, 30)
    drawBox(RI, "R`")
    RF = pygame.Rect(676, 40, 40, 30)
    drawBox(RF, "RF")
    RFI = pygame.Rect(718, 40, 40, 30)
    drawBox(RFI, "RF`")
    if mousePos:
        if r.collidepoint(mousePos):
            pyraminx.r()
        elif rI.collidepoint(mousePos):
            pyraminx.rI()
        elif rr.collidepoint(mousePos):
            pyraminx.rr()
        elif rrI.collidepoint(mousePos):
            pyraminx.rrI()
        elif rrr.collidepoint(mousePos):
            pyraminx.rrr()
        elif rrrI.collidepoint(mousePos):
            pyraminx.rrrI()
        elif R.collidepoint(mousePos):
            pyraminx.R()
        elif RI.collidepoint(mousePos):
            pyraminx.RI()
        elif RF.collidepoint(mousePos):
            pyraminx.RF()
        elif RFI.collidepoint(mousePos):
            pyraminx.RFI()

# Draw buttons for various moves on the left side of the green face.
def moveButtonL(mousePos = None):
    l = pygame.Rect(300, 72, 40, 30)
    drawBox(l, "l")
    lI = pygame.Rect(342, 72, 40, 30)
    drawBox(lI, "l`")
    ll = pygame.Rect(384, 72, 40, 30)
    drawBox(ll, "ll")
    llI = pygame.Rect(426, 72, 40, 30)
    drawBox(llI, "ll`")
    lll = pygame.Rect(468, 72, 40, 30)
    drawBox(lll, "lll")
    lllI = pygame.Rect(510, 72, 40, 30)
    drawBox(lllI, "lll`")
    L = pygame.Rect(552, 72, 40, 30)
    drawBox(L, "L")
    LI = pygame.Rect(594, 72, 40, 30)
    drawBox(LI, "L`")
    GF = pygame.Rect(676, 72, 40, 30)
    drawBox(GF, "GF")
    GFI = pygame.Rect(718, 72, 40, 30)
    drawBox(GFI, "GFI`")
    if mousePos:
        if l.collidepoint(mousePos):
            pyraminx.l()
        elif lI.collidepoint(mousePos):
            pyraminx.lI()
        elif ll.collidepoint(mousePos):
            pyraminx.ll()
        elif llI.collidepoint(mousePos):
            pyraminx.llI()
        elif lll.collidepoint(mousePos):
            pyraminx.lll()
        elif lllI.collidepoint(mousePos):
            pyraminx.lllI()
        elif L.collidepoint(mousePos):
            pyraminx.L()
        elif LI.collidepoint(mousePos):
            pyraminx.LI()
        elif GF.collidepoint(mousePos):
            pyraminx.GF()
        elif GFI.collidepoint(mousePos):
            pyraminx.GFI()

# Draws buttons for various moves on the top of the green face.
def moveButtonU(mousePos = None):
    u = pygame.Rect(300, 104, 40, 30)
    drawBox(u, "u")
    uI = pygame.Rect(342, 104, 40, 30)
    drawBox(uI, "u`")
    uu = pygame.Rect(384, 104, 40, 30)
    drawBox(uu, "uu")
    uuI = pygame.Rect(426, 104, 40, 30)
    drawBox(uuI, "uu`")
    uuu = pygame.Rect(468, 104, 40, 30)
    drawBox(uuu, "uuu")
    uuuI = pygame.Rect(510, 104, 40, 30)
    drawBox(uuuI, "uuu`")
    U = pygame.Rect(552, 104, 40, 30)
    drawBox(U, "U")
    UI = pygame.Rect(594, 104, 40, 30)
    drawBox(UI, "U`")
    YF = pygame.Rect(676, 104, 40, 30)
    drawBox(YF, "YF")
    YFI = pygame.Rect(718, 104, 40, 30)
    drawBox(YFI, "YFI")
    if mousePos:
        if u.collidepoint(mousePos):
            pyraminx.u()
        elif uI.collidepoint(mousePos):
            pyraminx.uI()
        elif uu.collidepoint(mousePos):
            pyraminx.uu()
        elif uuI.collidepoint(mousePos):
            pyraminx.uuI()
        elif uuu.collidepoint(mousePos):
            pyraminx.uuu()
        elif uuuI.collidepoint(mousePos):
            pyraminx.uuuI()
        elif U.collidepoint(mousePos):
            pyraminx.U()
        elif UI.collidepoint(mousePos):
            pyraminx.UI()
        elif YF.collidepoint(mousePos):
            pyraminx.YF()
        elif YFI.collidepoint(mousePos):
            pyraminx.YFI()

# Draws buttons for various moves on the connecting corner of the green and blue side face.
def moveButtonB(mousePos = None):
    b = pygame.Rect(300, 136, 40, 30)
    drawBox(b, "b")
    bI = pygame.Rect(342, 136, 40, 30)
    drawBox(bI, "b`")
    bb = pygame.Rect(384, 136, 40, 30)
    drawBox(bb, "bb")
    bbI = pygame.Rect(426, 136, 40, 30)
    drawBox(bbI, "bb`")
    bbb = pygame.Rect(468, 136, 40, 30)
    drawBox(bbb, "bbb")
    bbbI = pygame.Rect(510, 136, 40, 30)
    drawBox(bbbI, "bbb`")
    B = pygame.Rect(552, 136, 40, 30)
    drawBox(B, "B")
    BI = pygame.Rect(594, 136, 40, 30)
    drawBox(BI, "B`")
    BE = pygame.Rect(676, 136, 40, 30)
    drawBox(BE, "BF")
    BEI = pygame.Rect(718, 136, 40, 30)
    drawBox(BEI, "BF`")
    if mousePos:
        if b.collidepoint(mousePos):
            pyraminx.b()
        elif bI.collidepoint(mousePos):
            pyraminx.bI()
        elif bb.collidepoint(mousePos):
            pyraminx.bb()
        elif bbI.collidepoint(mousePos):
            pyraminx.bbI()
        elif bbb.collidepoint(mousePos):
            pyraminx.bbb()
        elif bbbI.collidepoint(mousePos):
            pyraminx.bbbI()
        elif B.collidepoint(mousePos):
            pyraminx.B()
        elif BI.collidepoint(mousePos):
            pyraminx.BI()
        elif BE.collidepoint(mousePos):
            pyraminx.BF()
        elif BEI.collidepoint(mousePos):
            pyraminx.BFI()

# Creates input box and randomize button for user to input a number and randomize.
input_box = pygame.Rect(100, 100, 140, 32)
randomizeButton = pygame.Rect(100, 133, 140, 32)

# Defines fonts used for text.
font = pygame.font.Font(None, 32)
altFont = pygame.font.Font(None, 28)

text = "" # Holds user input

# Loop to update display from various actions.
while not DONE:
    for event in pygame.event.get():

        # If you close out of the pygame window the program will end.
        if event.type == pygame.QUIT:
            DONE = True
            print("Thanks for playing!")

        # SOURCE: https://stackoverflow.com/questions/46390231/how-to-create-a-text-input-box-with-pygame
        # Helped with getting user input for pygame

        # Checks for if a user pressed their mouse button.
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = event.pos

            # Checks if the mouse press collides with a move. If it does it will execute that move.
            moveButtonR(mousePos)
            moveButtonL(mousePos)
            moveButtonU(mousePos)
            moveButtonB(mousePos)

            # Checks if the user pressed the randomize button.
            if randomizeButton.collidepoint(mousePos):
                if text != "":
                    # If a user presses randomize, and have a valid number in it.
                    # Will return random moves in an array and will execute each move.
                    moves = pyraminx.randomizePyraminx(int(text))
                    for move in moves:
                        move()
                        # Slows down each move to where you may visualize them.
                        if VISUALIZE_MOVE:
                            time.sleep(.1)
                            greenSide()
                            blueSide()
                            redSide()
                            yellowSide()
                            pygame.display.flip()

        # Checks if the key being pressed is a number. If so, it will add on to the number of times to randomize.
        if event.type == pygame.KEYDOWN:
                if event.unicode.isnumeric():
                    text += event.unicode
                # If the key pressed is a backspace, it will remove one digit from the randomize number.
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]

    # Standard screen updates to always apply the latest moves/updates.
    SCREEN.fill(WHITE)

    # Redraws the move buttons.
    moveButtonR()
    moveButtonL()
    moveButtonU()
    moveButtonB()

    # Draws the randomize button on screen
    pygame.draw.rect(SCREEN, RED, randomizeButton)
    SCREEN.blit(font.render("Randomize", True, BLACK), randomizeButton)

    # Redraws the faces.
    greenSide()
    blueSide()
    redSide()
    yellowSide()

    # Draws and updates the user input for number of times to randomize.
    textSurface = font.render(text, True, BLACK)
    pygame.draw.rect(SCREEN, GREY, input_box)
    SCREEN.blit(textSurface, input_box)
    
    # Updates new changes for what the user views.
    pygame.display.flip()
    CLOCK.tick(60)