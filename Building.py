class BuildingNode(object):
    def __init__(self,id,x,y,height):
        self.pID = []
        self.id = id
        self.height = height

    def getpID(self):
        return self.pID

    def getHeight(self):
        return self.height