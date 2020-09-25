import random

class Pyraminx:

    # Initializes the matrix used for defining the master pyraminx.
    def __init__(self):
        self.redSide = [["R"],["R","R","R"],["R","R","R","R","R"],["R","R","R","R","R","R","R"]]
        self.blueSide = [["B"],["B","B","B"],["B","B","B","B","B"],["B","B","B","B","B","B","B"]]
        self.yellowSide = [["Y"],["Y","Y","Y"],["Y","Y","Y","Y","Y"],["Y","Y","Y","Y","Y","Y","Y"]]
        self.greenSide = [["G"],["G","G","G"],["G","G","G","G","G"],["G","G","G","G","G","G","G"]]


    def move(self, move):
        moveList = {
            "l": self.l,
            "lI": self.lI,
            "ll": self.ll,
            "llI": self.llI,
            "lll": self.lll,
            "lllI": self.lllI,
            "L": self.L,
            "LI": self.LI,
            "r": self.r,
            "rI": self.rI,
            "rr": self.rr,
            "rrI": self.rrI,
            "rrr": self.rrr,
            "rrrI": self.rrrI,
            "R": self.R,
            "RI": self.RI,
            "u": self.u,
            "uI": self.uI,
            "uu": self.uu,
            "uuI": self.uuI,
            "uuu": self.uuu,
            "uuuI": self.uuuI,
            "U": self.U,
            "UI": self.UI,
            "b": self.b,
            "bI": self.bI,
            "bb": self.bb,
            "bbI": self.bbI,
            "bbb": self.bbb,
            "bbbI": self.bbbI,
            "B": self.B,
            "BI": self.BI,
            "RF": self.RF,
            "RFI": self.RFI,
            "BF": self.BF,
            "BFI": self.BFI,
            "YF": self.YF,
            "YFI": self.YFI,
            "GF": self.GF,
            "GFI": self.GFI
        }
        moveList[move]()

    # Returns a random move object from all moves and appends it to an array.
    def randomizePyraminx(self, num):
        moves = ""
        movesList = []
        randomizer = {
            "l": self.l,
            "lI": self.lI,
            "ll": self.ll,
            "llI": self.llI,
            "lll": self.lll,
            "lllI": self.lllI,
            "L": self.L,
            "LI": self.LI,
            "r": self.r,
            "rI": self.rI,
            "rr": self.rr,
            "rrI": self.rrI,
            "rrr": self.rrr,
            "rrrI": self.rrrI,
            "R": self.R,
            "RI": self.RI,
            "u": self.u,
            "uI": self.uI,
            "uu": self.uu,
            "uuI": self.uuI,
            "uuu": self.uuu,
            "uuuI": self.uuuI,
            "U": self.U,
            "UI": self.UI,
            "b": self.b,
            "bI": self.bI,
            "bb": self.bb,
            "bbI": self.bbI,
            "bbb": self.bbb,
            "bbbI": self.bbbI,
            "B": self.B,
            "BI": self.BI,
            "RF": self.RF,
            "RFI": self.RFI,
            "BF": self.BF,
            "BFI": self.BFI,
            "YF": self.YF,
            "YFI": self.YFI,
            "GF": self.GF,
            "GFI": self.GFI
        }
        for i in range(num):
            move, execute = random.choice(list(randomizer.items()))
            moves += move + " "
            movesList.append(execute)
        print("Random Moves:", moves)
        return movesList

    def wrongPos(self):
        total = 0
        for piece in [(self.redSide, "R"), (self.blueSide, "B"), (self.greenSide, "G"), (self.yellowSide, "Y")]:
            for i in range(4):
                for j in range(len(piece[0][i])):
                    if piece[0][i][j] != piece[1]:
                        total += 1
        return total

    """
    Below defines all the moves implemented in the master pyraminx. All the moves deal with swapping positions in the matrix.
    """
    def l(self):
        self.greenSide[3][0], self.redSide[3][-1], self.yellowSide[3][0] = \
        self.yellowSide[3][0], self.greenSide[3][0], self.redSide[3][-1]
    def lI(self):
        self.yellowSide[3][0], self.greenSide[3][0], self.redSide[3][-1]= \
        self.greenSide[3][0], self.redSide[3][-1], self.yellowSide[3][0] 
    def ll(self):
        (self.greenSide[2][0], self.greenSide[3][1], self.greenSide[3][2],
        self.redSide[2][-1], self.redSide[3][4], self.redSide[3][5],
        self.yellowSide[2][0], self.yellowSide[3][1], self.yellowSide[3][2]) =\
        (self.yellowSide[3][2],self.yellowSide[3][1], self.yellowSide[2][0],
        self.greenSide[3][2], self.greenSide[2][0], self.greenSide[3][1],
        self.redSide[2][-1], self.redSide[3][5], self.redSide[3][4])
    def llI(self):
        (self.yellowSide[3][2],self.yellowSide[3][1], self.yellowSide[2][0],
        self.greenSide[3][2], self.greenSide[2][0], self.greenSide[3][1],
        self.redSide[2][-1], self.redSide[3][5], self.redSide[3][4])=\
        (self.greenSide[2][0], self.greenSide[3][1], self.greenSide[3][2],
        self.redSide[2][-1], self.redSide[3][4], self.redSide[3][5],
        self.yellowSide[2][0], self.yellowSide[3][1], self.yellowSide[3][2])
    def lll(self):
        (self.greenSide[1][0], self.greenSide[2][1], self.greenSide[2][2], self.greenSide[3][3], self.greenSide[3][4],
        self.redSide[1][-1], self.redSide[2][3], self.redSide[2][2], self.redSide[3][2], self.redSide[3][3],
        self.yellowSide[1][0], self.yellowSide[2][1], self.yellowSide[2][2], self.yellowSide[3][3], self.yellowSide[3][4]) =\
        (self.yellowSide[3][4], self.yellowSide[3][3], self.yellowSide[2][2], self.yellowSide[2][1], self.yellowSide[1][0],
        self.greenSide[3][4], self.greenSide[3][3], self.greenSide[2][2], self.greenSide[1][0],self.greenSide[2][1],
        self.redSide[1][-1], self.redSide[2][3], self.redSide[2][2], self.redSide[3][3], self.redSide[3][2])
    def lllI(self):
        (self.yellowSide[3][4], self.yellowSide[3][3], self.yellowSide[2][2], self.yellowSide[2][1], self.yellowSide[1][0],
        self.greenSide[3][4], self.greenSide[3][3], self.greenSide[2][2], self.greenSide[1][0],self.greenSide[2][1],
        self.redSide[1][-1], self.redSide[2][3], self.redSide[2][2], self.redSide[3][3], self.redSide[3][2]) =\
        (self.greenSide[1][0], self.greenSide[2][1], self.greenSide[2][2], self.greenSide[3][3], self.greenSide[3][4],
        self.redSide[1][-1], self.redSide[2][3], self.redSide[2][2], self.redSide[3][2], self.redSide[3][3],
        self.yellowSide[1][0], self.yellowSide[2][1], self.yellowSide[2][2], self.yellowSide[3][3], self.yellowSide[3][4])
    def L(self):
        self.l()
        self.ll()
        self.lll()
    def LI(self):
        self.lI()
        self.llI()
        self.lllI()
    def r(self):
        self.greenSide[3][-1], self.blueSide[3][0], self.yellowSide[3][-1] =\
        self.yellowSide[3][-1], self.greenSide[3][-1], self.blueSide[3][0]
    def rI(self):
        self.yellowSide[3][-1], self.greenSide[3][-1], self.blueSide[3][0] =\
        self.greenSide[3][-1], self.blueSide[3][0], self.yellowSide[3][-1]
    def rr(self):
        (self.greenSide[2][-1], self.greenSide[3][4], self.greenSide[3][5],
        self.blueSide[2][0], self.blueSide[3][1], self.blueSide[3][2], 
        self.yellowSide[2][-1], self.yellowSide[3][4], self.yellowSide[3][5]) =\
        (self.yellowSide[3][4], self.yellowSide[2][-1],self.yellowSide[3][5], 
        self.greenSide[3][4], self.greenSide[3][5], self.greenSide[2][-1], 
        self.blueSide[2][0], self.blueSide[3][2], self.blueSide[3][1])
    def rrI(self):
        (self.yellowSide[3][4], self.yellowSide[2][-1],self.yellowSide[3][5], 
        self.greenSide[3][4], self.greenSide[3][5], self.greenSide[2][-1], 
        self.blueSide[2][0], self.blueSide[3][2], self.blueSide[3][1]) =\
        (self.greenSide[2][-1], self.greenSide[3][4], self.greenSide[3][5],
        self.blueSide[2][0], self.blueSide[3][1], self.blueSide[3][2], 
        self.yellowSide[2][-1], self.yellowSide[3][4], self.yellowSide[3][5])
    def rrr(self):
        (self.greenSide[1][-1], self.greenSide[2][2], self.greenSide[2][3], self.greenSide[3][2], self.greenSide[3][3],
        self.blueSide[1][0], self.blueSide[2][1], self.blueSide[2][2], self.blueSide[3][3], self.blueSide[3][4],
        self.yellowSide[1][-1], self.yellowSide[2][2], self.yellowSide[2][3], self.yellowSide[3][2], self.yellowSide[3][3]) = \
        (self.yellowSide[3][2], self.yellowSide[2][2], self.yellowSide[3][3], self.yellowSide[1][-1],self.yellowSide[2][3],
        self.greenSide[3][2], self.greenSide[3][3], self.greenSide[2][2], self.greenSide[2][3], self.greenSide[1][-1],
        self.blueSide[1][0], self.blueSide[2][2], self.blueSide[2][1], self.blueSide[3][4], self.blueSide[3][3])
    def rrrI(self):
        (self.yellowSide[3][2], self.yellowSide[2][2], self.yellowSide[3][3], self.yellowSide[1][-1],self.yellowSide[2][3],
        self.greenSide[3][2], self.greenSide[3][3], self.greenSide[2][2], self.greenSide[2][3], self.greenSide[1][-1],
        self.blueSide[1][0], self.blueSide[2][2], self.blueSide[2][1], self.blueSide[3][4], self.blueSide[3][3]) =\
        (self.greenSide[1][-1], self.greenSide[2][2], self.greenSide[2][3], self.greenSide[3][2], self.greenSide[3][3],
        self.blueSide[1][0], self.blueSide[2][1], self.blueSide[2][2], self.blueSide[3][3], self.blueSide[3][4],
        self.yellowSide[1][-1], self.yellowSide[2][2], self.yellowSide[2][3], self.yellowSide[3][2], self.yellowSide[3][3])    
    def R(self):
        self.r()
        self.rr()
        self.rrr()
    def RI(self):
        self.rI()
        self.rrI()
        self.rrrI()
    def u(self):
        self.greenSide[0][0], self.blueSide[0][0], self.redSide[0][0] =\
        self.blueSide[0][0], self.redSide[0][0], self.greenSide[0][0] 
    def uI(self):
        self.blueSide[0][0], self.redSide[0][0], self.greenSide[0][0] =\
        self.greenSide[0][0], self.blueSide[0][0], self.redSide[0][0]
    def uu(self):
        self.greenSide[1], self.blueSide[1], self.redSide[1] =\
        self.blueSide[1], self.redSide[1], self.greenSide[1]
    def uuI(self):
        self.blueSide[1], self.redSide[1], self.greenSide[1] =\
        self.greenSide[1], self.blueSide[1], self.redSide[1]
    def uuu(self):
        self.greenSide[2], self.blueSide[2], self.redSide[2] =\
        self.blueSide[2], self.redSide[2], self.greenSide[2]
    def uuuI(self):
        self.blueSide[2], self.redSide[2], self.greenSide[2] =\
        self.greenSide[2], self.blueSide[2], self.redSide[2]
    def U(self):
        self.u()
        self.uu()
        self.uuu()
    def UI(self):
        self.uI()
        self.uuI()
        self.uuuI()
    def b(self):
        self.blueSide[3][-1], self.redSide[3][0], self.yellowSide[0][0] =\
        self.yellowSide[0][0], self.blueSide[3][-1], self.redSide[3][0]
    def bI(self):
        self.yellowSide[0][0], self.blueSide[3][-1], self.redSide[3][0] =\
        self.blueSide[3][-1], self.redSide[3][0], self.yellowSide[0][0]
    def bb(self):
        (self.blueSide[2][-1], self.blueSide[3][4], self.blueSide[3][5],
        self.redSide[2][0], self.redSide[3][1], self.redSide[3][2],
        self.yellowSide[1][0], self.yellowSide[1][1], self.yellowSide[1][2]) =\
        (self.yellowSide[1][2], self.yellowSide[1][0], self.yellowSide[1][1],
        self.blueSide[3][4], self.blueSide[3][5], self.blueSide[2][-1], 
        self.redSide[2][0], self.redSide[3][1],self.redSide[3][2])
    def bbI(self):
        (self.yellowSide[1][2], self.yellowSide[1][0], self.yellowSide[1][1],
        self.blueSide[3][4], self.blueSide[3][5], self.blueSide[2][-1], 
        self.redSide[2][0], self.redSide[3][1],self.redSide[3][2]) =\
        (self.blueSide[2][-1], self.blueSide[3][4], self.blueSide[3][5],
        self.redSide[2][0], self.redSide[3][1], self.redSide[3][2],
        self.yellowSide[1][0], self.yellowSide[1][1], self.yellowSide[1][2])
    def bbb(self):
        (self.blueSide[1][-1], self.blueSide[2][2], self.blueSide[2][3], self.blueSide[3][2], self.blueSide[3][3],
        self.redSide[1][0], self.redSide[2][1], self.redSide[2][2], self.redSide[3][3], self.redSide[3][4],
        self.yellowSide[2][0], self.yellowSide[2][1], self.yellowSide[2][2], self.yellowSide[2][3], self.yellowSide[2][4]) =\
        (self.yellowSide[2][4],self.yellowSide[2][2], self.yellowSide[2][3], self.yellowSide[2][0],self.yellowSide[2][1],
        self.blueSide[3][2], self.blueSide[3][3], self.blueSide[2][2], self.blueSide[2][3], self.blueSide[1][-1],
        self.redSide[1][0], self.redSide[2][1], self.redSide[2][2], self.redSide[3][3], self.redSide[3][4])
    def bbbI(self):
        (self.yellowSide[2][4],self.yellowSide[2][2], self.yellowSide[2][3], self.yellowSide[2][0],self.yellowSide[2][1],
        self.blueSide[3][2], self.blueSide[3][3], self.blueSide[2][2], self.blueSide[2][3], self.blueSide[1][-1],
        self.redSide[1][0], self.redSide[2][1], self.redSide[2][2], self.redSide[3][3], self.redSide[3][4]) =\
        (self.blueSide[1][-1], self.blueSide[2][2], self.blueSide[2][3], self.blueSide[3][2], self.blueSide[3][3],
        self.redSide[1][0], self.redSide[2][1], self.redSide[2][2], self.redSide[3][3], self.redSide[3][4],
        self.yellowSide[2][0], self.yellowSide[2][1], self.yellowSide[2][2], self.yellowSide[2][3], self.yellowSide[2][4])
    def B(self):
        self.b()
        self.bb()
        self.bbb()
    def BI(self):
        self.bI()
        self.bbI()
        self.bbbI()
    def YF(self):
        self.greenSide[3], self.redSide[3], self.blueSide[3] =\
        self.blueSide[3], self.greenSide[3], self.redSide[3]

        (self.yellowSide[3][0], self.yellowSide[3][1], self.yellowSide[2][0], self.yellowSide[2][1], self.yellowSide[1][0], self.yellowSide[1][1],
        self.yellowSide[0][0], self.yellowSide[1][-2], self.yellowSide[1][-1], self.yellowSide[2][-2], self.yellowSide[2][-1], self.yellowSide[3][-2],
        self.yellowSide[3][-1], self.yellowSide[3][-2], self.yellowSide[3][-3], self.yellowSide[3][-4], self.yellowSide[3][-5], self.yellowSide[3][-6]) =\
        (self.yellowSide[3][-1], self.yellowSide[3][-2], self.yellowSide[3][-3], self.yellowSide[3][-4], self.yellowSide[3][-5], self.yellowSide[3][-6],
        self.yellowSide[3][0], self.yellowSide[3][1], self.yellowSide[2][0], self.yellowSide[2][1], self.yellowSide[1][0], self.yellowSide[1][1],
        self.yellowSide[0][0], self.yellowSide[1][-2], self.yellowSide[1][-1], self.yellowSide[2][-2], self.yellowSide[2][-1], self.yellowSide[3][-2])
    def YFI(self):
        self.blueSide[3], self.greenSide[3], self.redSide[3] =\
        self.greenSide[3], self.redSide[3], self.blueSide[3] 
        
        (self.yellowSide[3][-1], self.yellowSide[3][-2], self.yellowSide[3][-3], self.yellowSide[3][-4], self.yellowSide[3][-5], self.yellowSide[3][-6],
        self.yellowSide[3][0], self.yellowSide[3][1], self.yellowSide[2][0], self.yellowSide[2][1], self.yellowSide[1][0], self.yellowSide[1][1],
        self.yellowSide[0][0], self.yellowSide[1][-2], self.yellowSide[1][-1], self.yellowSide[2][-2], self.yellowSide[2][-1], self.yellowSide[3][-2]) =\
        (self.yellowSide[3][0], self.yellowSide[3][1], self.yellowSide[2][0], self.yellowSide[2][1], self.yellowSide[1][0], self.yellowSide[1][1],
        self.yellowSide[0][0], self.yellowSide[1][-2], self.yellowSide[1][-1], self.yellowSide[2][-2], self.yellowSide[2][-1], self.yellowSide[3][-2],
        self.yellowSide[3][-1], self.yellowSide[3][-2], self.yellowSide[3][-3], self.yellowSide[3][-4], self.yellowSide[3][-5], self.yellowSide[3][-6])
    def BF(self):
        (self.redSide[0][0], self.redSide[1][1], self.redSide[1][0], self.redSide[2][1], self.redSide[2][0], self.redSide[3][1], self.redSide[3][0],
        self.yellowSide[0][0],self.yellowSide[1][1],self.yellowSide[1][-1], self.yellowSide[2][-2], self.yellowSide[2][-1], self.yellowSide[3][-2], self.yellowSide[3][-1],
        self.greenSide[0][0], self.greenSide[1][1], self.greenSide[1][-1], self.greenSide[2][-2], self.greenSide[2][-1], self.greenSide[3][-2], self.greenSide[3][-1]) =\
        (self.greenSide[3][-1], self.greenSide[3][-2], self.greenSide[2][-1], self.greenSide[2][-2], self.greenSide[1][-1], self.greenSide[1][1], self.greenSide[0][0],
        self.redSide[0][0], self.redSide[1][1], self.redSide[1][0], self.redSide[2][1], self.redSide[2][0], self.redSide[3][1], self.redSide[3][0],
        self.yellowSide[3][-1], self.yellowSide[3][-2], self.yellowSide[2][-1], self.yellowSide[2][-2], self.yellowSide[1][-1], self.yellowSide[1][1], self.yellowSide[0][0])

        (self.blueSide[3][0], self.blueSide[3][1], self.blueSide[2][0], self.blueSide[2][1], self.blueSide[1][0], self.blueSide[1][1],
        self.blueSide[0][0], self.blueSide[1][-2], self.blueSide[1][-1], self.blueSide[2][-2], self.blueSide[2][-1], self.blueSide[3][-2],
        self.blueSide[3][-1], self.blueSide[3][-2], self.blueSide[3][-3], self.blueSide[3][-4], self.blueSide[3][-5], self.blueSide[3][-6]) =\
        (self.blueSide[3][-1], self.blueSide[3][-2], self.blueSide[3][-3], self.blueSide[3][-4], self.blueSide[3][-5], self.blueSide[3][-6],
        self.blueSide[3][0], self.blueSide[3][1], self.blueSide[2][0], self.blueSide[2][1], self.blueSide[1][0], self.blueSide[1][1],
        self.blueSide[0][0], self.blueSide[1][-2], self.blueSide[1][-1], self.blueSide[2][-2], self.blueSide[2][-1], self.blueSide[3][-2])
    def BFI(self):
        (self.greenSide[3][-1], self.greenSide[3][-2], self.greenSide[2][-1], self.greenSide[2][-2], self.greenSide[1][-1], self.greenSide[1][1], self.greenSide[0][0],
        self.redSide[0][0], self.redSide[1][1], self.redSide[1][0], self.redSide[2][1], self.redSide[2][0], self.redSide[3][1], self.redSide[3][0],
        self.yellowSide[3][-1], self.yellowSide[3][-2], self.yellowSide[2][-1], self.yellowSide[2][-2], self.yellowSide[1][-1], self.yellowSide[1][1], self.yellowSide[0][0]) =\
        (self.redSide[0][0], self.redSide[1][1], self.redSide[1][0], self.redSide[2][1], self.redSide[2][0], self.redSide[3][1], self.redSide[3][0],
        self.yellowSide[0][0],self.yellowSide[1][1],self.yellowSide[1][-1], self.yellowSide[2][-2], self.yellowSide[2][-1], self.yellowSide[3][-2], self.yellowSide[3][-1],
        self.greenSide[0][0], self.greenSide[1][1], self.greenSide[1][-1], self.greenSide[2][-2], self.greenSide[2][-1], self.greenSide[3][-2], self.greenSide[3][-1])

        (self.blueSide[3][-1], self.blueSide[3][-2], self.blueSide[3][-3], self.blueSide[3][-4], self.blueSide[3][-5], self.blueSide[3][-6],
        self.blueSide[3][0], self.blueSide[3][1], self.blueSide[2][0], self.blueSide[2][1], self.blueSide[1][0], self.blueSide[1][1],
        self.blueSide[0][0], self.blueSide[1][-2], self.blueSide[1][-1], self.blueSide[2][-2], self.blueSide[2][-1], self.blueSide[3][-2])=\
        (self.blueSide[3][0], self.blueSide[3][1], self.blueSide[2][0], self.blueSide[2][1], self.blueSide[1][0], self.blueSide[1][1],
        self.blueSide[0][0], self.blueSide[1][-2], self.blueSide[1][-1], self.blueSide[2][-2], self.blueSide[2][-1], self.blueSide[3][-2],
        self.blueSide[3][-1], self.blueSide[3][-2], self.blueSide[3][-3], self.blueSide[3][-4], self.blueSide[3][-5], self.blueSide[3][-6]) 
    def RF(self):
        (self.greenSide[0][0], self.greenSide[1][1], self.greenSide[1][0], self.greenSide[2][1], self.greenSide[2][0], self.greenSide[3][1], self.greenSide[3][0],
        self.yellowSide[3][0], self.yellowSide[3][1], self.yellowSide[2][0], self.yellowSide[2][1], self.yellowSide[1][0], self.yellowSide[1][1], self.yellowSide[0][0],
        self.blueSide[3][-1], self.blueSide[3][-2], self.blueSide[2][-1], self.blueSide[2][-2], self.blueSide[1][-1], self.blueSide[1][1], self.blueSide[0][0]) =\
        (self.yellowSide[3][0], self.yellowSide[3][1], self.yellowSide[2][0], self.yellowSide[2][1], self.yellowSide[1][0], self.yellowSide[1][1], self.yellowSide[0][0],
        self.blueSide[3][-1], self.blueSide[3][-2], self.blueSide[2][-1], self.blueSide[2][-2], self.blueSide[1][-1], self.blueSide[1][1], self.blueSide[0][0],
        self.greenSide[0][0], self.greenSide[1][1], self.greenSide[1][0], self.greenSide[2][1], self.greenSide[2][0], self.greenSide[3][1], self.greenSide[3][0])

        (self.redSide[3][-1], self.redSide[3][-2], self.redSide[3][-3], self.redSide[3][-4], self.redSide[3][-5], self.redSide[3][-6],
        self.redSide[3][0], self.redSide[3][1], self.redSide[2][0], self.redSide[2][1], self.redSide[1][0], self.redSide[1][1],
        self.redSide[0][0], self.redSide[1][-2], self.redSide[1][-1], self.redSide[2][-2], self.redSide[2][-1], self.redSide[3][-2]) =\
        (self.redSide[3][0], self.redSide[3][1], self.redSide[2][0], self.redSide[2][1], self.redSide[1][0], self.redSide[1][1],
        self.redSide[0][0], self.redSide[1][-2], self.redSide[1][-1], self.redSide[2][-2], self.redSide[2][-1], self.redSide[3][-2],
        self.redSide[3][-1], self.redSide[3][-2], self.redSide[3][-3], self.redSide[3][-4], self.redSide[3][-5], self.redSide[3][-6])
    def RFI(self):
        (self.yellowSide[3][0], self.yellowSide[3][1], self.yellowSide[2][0], self.yellowSide[2][1], self.yellowSide[1][0], self.yellowSide[1][1], self.yellowSide[0][0],
        self.blueSide[3][-1], self.blueSide[3][-2], self.blueSide[2][-1], self.blueSide[2][-2], self.blueSide[1][-1], self.blueSide[1][1], self.blueSide[0][0],
        self.greenSide[0][0], self.greenSide[1][1], self.greenSide[1][0], self.greenSide[2][1], self.greenSide[2][0], self.greenSide[3][1], self.greenSide[3][0]) =\
        (self.greenSide[0][0], self.greenSide[1][1], self.greenSide[1][0], self.greenSide[2][1], self.greenSide[2][0], self.greenSide[3][1], self.greenSide[3][0],
        self.yellowSide[3][0], self.yellowSide[3][1], self.yellowSide[2][0], self.yellowSide[2][1], self.yellowSide[1][0], self.yellowSide[1][1], self.yellowSide[0][0],
        self.blueSide[3][-1], self.blueSide[3][-2], self.blueSide[2][-1], self.blueSide[2][-2], self.blueSide[1][-1], self.blueSide[1][1], self.blueSide[0][0])


        (self.redSide[3][0], self.redSide[3][1], self.redSide[2][0], self.redSide[2][1], self.redSide[1][0], self.redSide[1][1],
        self.redSide[0][0], self.redSide[1][-2], self.redSide[1][-1], self.redSide[2][-2], self.redSide[2][-1], self.redSide[3][-2],
        self.redSide[3][-1], self.redSide[3][-2], self.redSide[3][-3], self.redSide[3][-4], self.redSide[3][-5], self.redSide[3][-6]) =\
        (self.redSide[3][-1], self.redSide[3][-2], self.redSide[3][-3], self.redSide[3][-4], self.redSide[3][-5], self.redSide[3][-6],
        self.redSide[3][0], self.redSide[3][1], self.redSide[2][0], self.redSide[2][1], self.redSide[1][0], self.redSide[1][1],
        self.redSide[0][0], self.redSide[1][-2], self.redSide[1][-1], self.redSide[2][-2], self.redSide[2][-1], self.redSide[3][-2])
    def GF(self):
        (self.blueSide[3][0], self.blueSide[3][1], self.blueSide[2][0], self.blueSide[2][1], self.blueSide[1][0], self.blueSide[1][1], self.blueSide[0][0],
        self.yellowSide[3][0], self.yellowSide[3][1], self.yellowSide[3][2], self.yellowSide[3][3], self.yellowSide[3][4], self.yellowSide[3][5], self.yellowSide[3][6],
        self.redSide[0][0], self.redSide[1][-2], self.redSide[1][-1], self.redSide[2][-2], self.redSide[2][-1], self.redSide[3][-2], self.redSide[3][-1]) =\
        (self.redSide[0][0], self.redSide[1][-2], self.redSide[1][-1], self.redSide[2][-2], self.redSide[2][-1], self.redSide[3][-2], self.redSide[3][-1],
        self.blueSide[3][0], self.blueSide[3][1], self.blueSide[2][0], self.blueSide[2][1], self.blueSide[1][0], self.blueSide[1][1], self.blueSide[0][0],
        self.yellowSide[3][0], self.yellowSide[3][1], self.yellowSide[3][2], self.yellowSide[3][3], self.yellowSide[3][4], self.yellowSide[3][5], self.yellowSide[3][6])
        (self.greenSide[3][0], self.greenSide[3][1], self.greenSide[2][0], self.greenSide[2][1], self.greenSide[1][0], self.greenSide[1][1],
        self.greenSide[0][0], self.greenSide[1][-2], self.greenSide[1][-1], self.greenSide[2][-2], self.greenSide[2][-1], self.greenSide[3][-2],
        self.greenSide[3][-1], self.greenSide[3][-2], self.greenSide[3][-3], self.greenSide[3][-4], self.greenSide[3][-5], self.greenSide[3][-6]) =\
        (self.greenSide[3][-1], self.greenSide[3][-2], self.greenSide[3][-3], self.greenSide[3][-4], self.greenSide[3][-5], self.greenSide[3][-6],
        self.greenSide[3][0], self.greenSide[3][1], self.greenSide[2][0], self.greenSide[2][1], self.greenSide[1][0], self.greenSide[1][1],
        self.greenSide[0][0], self.greenSide[1][-2], self.greenSide[1][-1], self.greenSide[2][-2], self.greenSide[2][-1], self.greenSide[3][-2])
    def GFI(self):
        (self.redSide[0][0], self.redSide[1][-2], self.redSide[1][-1], self.redSide[2][-2], self.redSide[2][-1], self.redSide[3][-2], self.redSide[3][-1],
        self.blueSide[3][0], self.blueSide[3][1], self.blueSide[2][0], self.blueSide[2][1], self.blueSide[1][0], self.blueSide[1][1], self.blueSide[0][0],
        self.yellowSide[3][0], self.yellowSide[3][1], self.yellowSide[3][2], self.yellowSide[3][3], self.yellowSide[3][4], self.yellowSide[3][5], self.yellowSide[3][6]) =\
        (self.blueSide[3][0], self.blueSide[3][1], self.blueSide[2][0], self.blueSide[2][1], self.blueSide[1][0], self.blueSide[1][1], self.blueSide[0][0],
        self.yellowSide[3][0], self.yellowSide[3][1], self.yellowSide[3][2], self.yellowSide[3][3], self.yellowSide[3][4], self.yellowSide[3][5], self.yellowSide[3][6],
        self.redSide[0][0], self.redSide[1][-2], self.redSide[1][-1], self.redSide[2][-2], self.redSide[2][-1], self.redSide[3][-2], self.redSide[3][-1]) 

        (self.greenSide[3][-1], self.greenSide[3][-2], self.greenSide[3][-3], self.greenSide[3][-4], self.greenSide[3][-5], self.greenSide[3][-6],
        self.greenSide[3][0], self.greenSide[3][1], self.greenSide[2][0], self.greenSide[2][1], self.greenSide[1][0], self.greenSide[1][1],
        self.greenSide[0][0], self.greenSide[1][-2], self.greenSide[1][-1], self.greenSide[2][-2], self.greenSide[2][-1], self.greenSide[3][-2])=\
        (self.greenSide[3][0], self.greenSide[3][1], self.greenSide[2][0], self.greenSide[2][1], self.greenSide[1][0], self.greenSide[1][1],
        self.greenSide[0][0], self.greenSide[1][-2], self.greenSide[1][-1], self.greenSide[2][-2], self.greenSide[2][-1], self.greenSide[3][-2],
        self.greenSide[3][-1], self.greenSide[3][-2], self.greenSide[3][-3], self.greenSide[3][-4], self.greenSide[3][-5], self.greenSide[3][-6])
    
    # Defines printing the screen in the terminal instead of using the GUI.
    def printFace(self):
        arr = [self.redSide, self.greenSide, self.blueSide]
        for face in arr:
            print(' ' *14,face[0])
            print(' '*9,face[1])
            print(' '*4,face[2])
            print(face[3])
            print()
        print(self.yellowSide[3])
        print(' '*4,self.yellowSide[2])
        print(' '*9,self.yellowSide[1])
        print(' ' *14,self.yellowSide[0])

# Used for running only in terminal.
if __name__ == "__main__":
    pyraminx = Pyraminx()
    
    # Gets user input for random moves and executes.
    usrInput = int(input("How many randomizations would you like? "))
    moves = pyraminx.randomizePyraminx(usrInput)
    for move in moves:
        move()
    # Prints pyraminx in terminal.
    pyraminx.printFace()
