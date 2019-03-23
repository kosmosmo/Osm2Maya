import Point,Building
import re
import json
import collections
import copy
import convertor
import random

class data():
    def __init__(self):
        self.points = collections.defaultdict()
        self.buildings = collections.defaultdict()

    def castPoint(self,line):
        res = [None,None,None]
        line = line.split(' ')
        for item in line:
            if item.startswith ("id="):
                res[0] = re.sub("[^0-9]", "", item)
            elif item.startswith ("lat=\""):
                res[1] = float(re.sub("[^\d\.\-]", "", item))
            elif item.startswith ("lon=\""):
                res[2] = float(re.sub("[^\d\.\-]", "", item))
        return res

    def castBuild(self,start,end,lines):
        typeNo = 2
        ID,type, height, pID= None, None, None, []
        bre = lines[start].split(' ')
        for item in bre:
            if item.startswith("id=\""):
                ID = re.sub("[^0-9]", "", item)
        flag = False
        for i in range(start+1,end):
            if "tag" in lines[i]: flag =True
            if "<tag k=\"height\"" in lines[i]:
                try:height = float(re.sub("[^\d\.\-]", "", lines[i]))
                except:height = 0
            elif "<nd ref=" in lines[i]:
                pID.append(re.sub("[^0-9]", "", lines[i]))
            else:
                curType = self.getBuildType(lines[i])
                if curType:
                    type = curType
                    if "build" in type:typeNo = 0
                    elif "highway" in type: typeNo = 1
        if not flag: type = "NullType"
        return [ID,type,height,pID,typeNo]



    def castData(self,file):

        way = None
        lines = open(file).readlines()

        with open(file, "r") as fp:
            for lineNumber, line in enumerate(fp):
                if "<node id=" in line:
                    pointInfo = self.castPoint(line)
                    self.points[pointInfo[0]] = Point.PointNode(pointInfo[0],pointInfo[1],pointInfo[2])

                if "</way>" in line:
                    if way:
                        buildInfo = self.castBuild(way,lineNumber+1,lines)
                        self.buildings[buildInfo[0]] = Building.BuildingNode(buildInfo[0],buildInfo[1],buildInfo[2],buildInfo[3],buildInfo[4])
                    way = lineNumber + 1



    def freezePoints(self,mult):
        zeroX = None
        zeroY = None
        for key,val in self.points.items():
            if not zeroX:zeroX,zeroY = val.x,val.y
            val.mulCoord(zeroX,zeroY,mult)

    def toJson(self,pName,bName):
        print "hi"
        points = copy.deepcopy(self.points)
        buildings = copy.deepcopy(self.buildings)
        for key,val in points.items():
            points[key] = [val.x,val.y]
        with open(pName+'.json', 'w') as outfile:
            json.dump(points, outfile)
        for key,val in buildings.items():
            buildings[key] = [val.pID,val.height,val.type,val.typeNo]
        with open(bName+'.json', 'w') as outfile:
            json.dump(buildings, outfile)

    def loadJson(self,file):

        with open(file+'.json') as json_data:
            res = json.load(json_data)
            json_data.close()
        return res



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
        elif "<tag k=\"building\" v=\"commercial\"/>" in line:
            return "buildingCommercial"
        elif "<tag k=\"building\" v=\"office\"/>" in line:
            return "buildingOffice"
        elif "<tag k=\"building\" v=\"church\"/>" in line:
            return "buildingChurch"
        elif "<tag k=\"building\" v=\"apartments\"/>" in line:
            return "buildingApartments"
        elif "<tag k=\"building" in line:
            return "building"
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
        elif "<tag k=\"barrier\" v=\"fence\"/>" in line:
            return "barrierFence"
        elif "<tag k=\"area\" v=\"yes\"/>" in line:
            return "area"
        elif "<tag k=\"railway\" v=\"abandoned\"/>" in line:
            return "railwayAbandoned"
        elif "<tag k=\"public_transport\" v=\"platform\"/>" in line:
            return "publicTransportPlatform"
        elif "<tag k=\"amenity\" v=\"bench\"/>" in line:
            return "amenityBench"
        elif "<tag k=\"route\" v=\"ferry\"/>" in line:
            return "routeFerry"
        elif "<tag k=\"landuse\" v=\"construction\"/>" in line:
            return "landuseConstruction"
        elif "<tag k=\"leisure\" v=\"garden\"/>" in line:
            return "leisureGarden"
        elif "<tag k=\"traffic_calming\" v=\"island\"/>" in line:
            return "trafficCalmingIsland"
        elif "<tag k=\"barrier\" v=\"retaining_wall\"/>" in line:
            return "barrierRetainingWall"
        return None

def ps2tuple(points,pIDs):
    tPoint = []
    for pID in pIDs:
        if pID in points and points[pID]:
            tPoint.append((points[pID].x, 0, points[pID].y))
    return tPoint

file = "bigData.osm"
a = data()
a.castData(file)
a.freezePoints(100000)
a.toJson("points","geos")



for key,val in a.buildings.items():
    tPoint = ps2tuple(a.points,val.pID)
