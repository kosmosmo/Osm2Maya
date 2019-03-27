import json
import maya.cmds as cmds
import collections


def loadJson(file):
    with open(file + '.json') as json_data:
        res = json.load(json_data)
        json_data.close()
    return res


def ps2tuple(points, pIDs):
    tPoint = []
    for pID in pIDs:
        if pID in points and points[pID]:
            tPoint.append((points[pID][0], 0, points[pID][1]))
    return tPoint


pfile = "C:\Users\momo\PycharmProjects\OsmReader\points"
bfile = "C:\Users\momo\PycharmProjects\OsmReader\geos"
buildings = loadJson(bfile)
points = loadJson(pfile)

ct = 0

total = len(buildings)
onek = 1000
for key, val in buildings.items():
    ct += 1
    if ct == onek:
        print str(ct) + "/" + str(total)
        onek += 1000
    if val[2] and val[2].startswith("build"):
        tPoint = ps2tuple(points, val[0])
        if len(tPoint) <= 2: continue
        bid = "b" + str(key)
        cmds.polyCreateFacet(p=tPoint, n=bid)
        if cmds.polyInfo(fn=True)[0].split(' ')[-2][0] == "-": cmds.polyNormal(nm=0)
        if val[1]:
            cmds.select(bid)
            cmds.xform(cp=True)
            cmds.polyExtrudeFacet(kft=False, ltz=val[1])
    elif len(val[0]) >= 3 and val[0][0] == val[0][-1]:
        tPoint = ps2tuple(points, val[0])
        if len(tPoint) <= 2: continue
        bid = "b" + str(key)
        cmds.polyCreateFacet(p=tPoint, n=bid)
        if cmds.polyInfo(fn=True)[0].split(' ')[-2][0] == "-": cmds.polyNormal(nm=0)
        if val[1]:
            cmds.select(bid)
            cmds.xform(cp=True)
            cmds.polyExtrudeFacet(kft=False, ltz=val[1])
        else:
            cmds.select(bid)
            cmds.xform(cp=True)
            cmds.polyExtrudeFacet(kft=False, ltz=1)
    elif "boundary" in val[-1]:
        tPoint = ps2tuple(points, val[0])
        if len(tPoint) <= 2: continue
        cmds.curve(p=tPoint,d=1)
