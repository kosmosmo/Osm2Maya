import Point,Building
import re
import collections
class data():
    def __init__(self):
        self.points = collections.defaultdict()
        self.buildings = []

    def castPoint(self,line):
        res = [None,None,None]
        line = line.split(' ')
        res[0] = re.sub("[^0-9]", "", line[2])
        res[1] = float(re.sub("[^\d\.\-]", "", line[-2]))
        res[2] = float(re.sub("[^\d\.\-]", "", line[-1]))
        return res

    def castBuild(self,start,end,lines):
        ID,type, height, pID= None, None, None, []
        ID = re.sub("[^0-9]", "", lines[start].split(' ')[2])
        for i in range(start+1,end):
            if "<tag k=\"height\"" in lines[i]:
                height = float(re.sub("[^\d\.\-]", "", lines[i]))
            elif "<nd ref=" in lines[i]:
                pID.append(re.sub("[^0-9]", "", lines[i]))
            else:
                curType = self.getBuildType(lines[i])
                if curType:type = curType
        return [ID,type,height,pID]

    def getBuildType(self,line):
        ##Building
        if "<tag k=\"building\" v=\"yes\"/>" in line:
            return "building"
        elif "<tag k=\"building:part\" v=\"yes\"/>" in line:
            return "buildingPart"
        elif "<tag k=\"building\" v=\"fire_station\"/>" in line:
            return "buildingFireStation"
        elif "<tag k=\"building\" v=\"roof\"/>" in line:
            return "buildingRoof"
        elif "<tag k=\"building\" v=\"construction\"/>" in line:
            return "buildingConstruction"
        ##HighWay
        elif "<tag k=\"highway\" v=\"service\"/>" in line:
            return "highwayService"
        elif "<tag k=\"highway\" v=\"pedestrian\"/>" in line:
            return "highwayPedestrian"
        elif "<tag k=\"highway\" v=\"cycleway\"/>" in line:
            return "highwayCycleway"
        elif "<tag k=\"highway\" v=\"residential\"/>" in line:
            return "highwayResidential"
        elif "<tag k=\"highway\" v=\"secondary\"/>" in line:
            return "highwaySecondary"
        elif "<tag k=\"highway\" v=\"footway\"/>" in line:
            return "highwayFootway"
        elif "<tag k=\"highway\" v=\"steps\"/>" in line:
            return "highwaySteps"
        elif "<tag k=\"highway\" v=\"motorway\"/>" in line:
            return "highwayMotorway"
        elif "<tag k=\"highway\" v=\"unclassified\"/>" in line:
            return "highwayUnclassified"
        elif "<tag k=\"highway\" v=\"motorway_link\"/>" in line:
            return "highwayMotorway_link"
        elif "<tag k=\"highway\" v=\"trunk\"/>" in line:
            return "highwayTrunk"
        elif "<tag k=\"highway\"" in line:
            return "highway"

        ##Others
        elif "<tag k=\"bicycle\" v=\"yes\"/>" in line:
            return "bicycle"
        elif "<tag k=\"barrier\" v=\"wall\"/>" in line:
            return "barrierWall"
        elif "<tag k=\"leisure\" v=\"park\"/>" in line:
            return "leisurePark"
        elif "<tag k=\"leisure\" v=\"pitch\"/>" in line:
            return "leisurePitch"
        elif "<tag k=\"amenity\" v=\"school\"/>" in line:
            return "amenitySchool"
        elif "<tag k=\"amenity\" v=\"ferry_terminal\"/>" in line:
            return "amenityFerryTerminal"
        elif "<tag k=\"man_made\" v=\"pier\"/>" in line:
            return "manMadePier"
        elif "tag k=\"railway\" v=\"subway\"/>" in line:
            return "railwaySubway"
        elif "<tag k=\"boundary\" v=\"administrative\"/>" in line:
            return "boundaryAdmin"
        elif "<tag k=\"landuse\" v=\"grass\"/>" in line:
            return "landuseGrass"
        elif "<tag k=\"aeroway\" v=\"helipad\"/>" in line:
            return "aerowayHelipad"
        elif "<tag k=\"public_transport\" v=\"station\"/>" in line:
            return "publicTransportStation"
        elif "<tag k=\"natural\"" in line:
            return "natural"
        return None

    def castData(self,file):
        way = None
        lines = open(file).readlines()
        ct = 0
        with open(file, "r") as fp:
            for lineNumber, line in enumerate(fp):
                if line.startswith(" <node id="):
                    pointInfo = self.castPoint(line)
                    self.points[pointInfo[0]] = Point.PointNode(pointInfo[0],pointInfo[1],pointInfo[2])
                if "</way>" in line:
                    if way:
                        temp = self.castBuild(way,lineNumber+1,lines)
                        #print temp

                        if not temp[1]:
                            ct += 1
                            print temp

                    way = lineNumber + 1
        print ct








file = "bigData.osm"
a = data()
print a.castData(file)
