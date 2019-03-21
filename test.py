import Point
import re
class data():
    def __init__(self):
        self.points = []
        self.buildings = []

    def castPoint(self,line):
        res = [None,None,None]
        line = line.split(' ')
        res[0] = re.sub("[^0-9]", "", line[2])
        res[1] = float(re.sub("[^\d\.\-]", "", line[-2]))
        res[2] = float(re.sub("[^\d\.\-]", "", line[-1]))
        return res

    def castData(self,file):
        with open(file, "r") as fp:
            for lineNumber, line in enumerate(fp):
                if line.startswith(" <node id="):
                    pointInfo = self.castPoint(line)
                    self.points.append(Point.PointNode(pointInfo[0],pointInfo[1],pointInfo[2]))




file = "bigData.osm"
a = data()
print a.castData(file)