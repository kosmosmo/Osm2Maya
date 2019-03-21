class BuildingNode(object):
    def __init__(self,id,type,height,pID):
        self.id = id
        self.pID = pID
        self.height = height
        self.type = type

    def getpID(self):
        return self.pID

    def getHeight(self):
        return self.height