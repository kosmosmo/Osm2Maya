import json
import maya.cmds as cmds
import pooper
import collections
from PySide2 import QtCore, QtGui, QtWidgets
import output
class mayaSucks(QtCore.QObject):
    valueUpdated = QtCore.Signal(int)
    def progressBar(self,length, portion):
        prog = collections.defaultdict(int)
        each = length / portion
        ct = 0
        for i in range(portion):
            prog[ct] = i * (100 / portion)
            ct += each
        return prog
    
    def ps2tuple(self,points, pIDs):
        tPoint = []
        for pID in pIDs:
            if pID in points and points[pID]:
                tPoint.append((points[pID].x, 0, points[pID].y))
        return tPoint

    def build(self,file):
        print "start to build"
        osm = pooper.data()
        osm.castData(file)
        osm.freezePoints(100000)
        ct = 0
        pro = self.progressBar(len(osm.buildings),100)
        for key, val in osm.buildings.items():            
            if ct in pro:
                self.valueUpdated.emit(pro[ct])
            ct += 1
            if val.type and val.type.startswith("build"):
                tPoint = self.ps2tuple(osm.points, val.pID)
                if len(tPoint) <= 2: continue
                bid = "b" + str(key)
                cmds.polyCreateFacet(p=tPoint, n=bid)
                if cmds.polyInfo(fn=True)[0].split(' ')[-2][0] == "-": cmds.polyNormal(nm=0)
                if val.height:
                    cmds.select(bid)
                    cmds.xform(cp=True)
                    cmds.polyExtrudeFacet(kft=False, ltz=val.height)
            elif len(val.pID) >= 3 and val.pID[0] == val.pID[-1]:
                tPoint = self.ps2tuple(osm.points, val.pID)
                if len(tPoint) <= 2: continue
                bid = "b" + str(key)
                cmds.polyCreateFacet(p=tPoint, n=bid)
                if cmds.polyInfo(fn=True)[0].split(' ')[-2][0] == "-": cmds.polyNormal(nm=0)
                if val.height:
                    cmds.select(bid)
                    cmds.xform(cp=True)
                    cmds.polyExtrudeFacet(kft=False, ltz=val.height)
            elif "boundary" in val.tags:        
                tPoint = self.ps2tuple(osm.points, val.pID)
                if len(tPoint) <= 2: continue
                cmds.curve(p=tPoint,d=1)
