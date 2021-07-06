class Gm:
    def __init__(self,ntiles,npoles=3):
        self.ntiles = ntiles
        self.npoles = npoles
        self.board = [[None for y in range(self.ntiles)] for x in range(self.npoles)]
        self.board[0] = list(range(ntiles))
        self.board[0].reverse()
    def firstNone(self,pole,subtract=0):
        for i in range(self.ntiles):
            if self.board[pole][i] is None:
                return i-subtract
        return i
    def move(self,polea,poleb):
        a = self.firstNone(polea,1)
        b = self.firstNone(poleb)
        #print(a,b)
        if polea == poleb:
            return 0
        if self.board[poleb][0] is not None:
            if self.board[polea][a] > self.board[poleb][b-1]:
                return 0
        del self.board[poleb][b]
        self.board[poleb].insert(b,self.board[polea].pop(a))
        self.board[polea].insert(a,None)
        return 1



if __name__ == "__main__":
    a = Gm(3,3)
    a.move(0,2)
    a.move(0,2)
    print(a.board)
