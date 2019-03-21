class PointNode(object):
    def __init__(self,id,x,y):
        self.x = x
        self.y = y
        self.id = id

    def getCoord(self):
        return [self.x,self.y]

    def mulCoord(self,zx,zy, mul):
        self.x = (self.x - zx) * mul
        self.y = (self.y - zy) * mul