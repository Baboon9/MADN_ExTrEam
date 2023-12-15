class Spot:
    def __init__(self, figure):
        self.figure_at_spot = figure
    def getFigure(self):
        return self.figure_at_spot
    def setFigureIn(self, figure):
        self.figure_at_spot = figure
    def print(self):
        if not self.figure_at_spot == None:
            print(self.figure_at_spot.color,end="")
        else:
            print("O",end="")
    def removeFigure(self, figure):
        self.figure_at_spot = None
    def isEmpty(self):
        return self.figure_at_spot == None


