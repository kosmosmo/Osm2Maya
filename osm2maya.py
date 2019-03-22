import json
import maya.cmds as cmds
def loadJson(file):
    with open(file+'.json') as json_data:
        res = json.load(json_data)
        json_data.close()
    return res

def ps2tuple(points,pIDs):
    tPoint = []
    for pID in pIDs:
        if pID in points and points[pID]:
            tPoint.append((points[pID][0], 0, points[pID][1]))
    return tPoint


pfile = "C:\Users\momo\PycharmProjects\OsmReader\points"
bfile = "C:\Users\momo\PycharmProjects\OsmReader\geos"
buildings = loadJson(bfile)
points = loadJson(pfile)

for key,val in buildings.items():
    if val[-1] == 0:
        tPoint = ps2tuple(points,val[0])
        if len(tPoint) <=2: continue
        bid = "b" + str(key)
        cmds.polyCreateFacet( p= tPoint, n = bid )
        if val[-3]:
            cmds.select( bid)
            cmds.xform(cp= True)
            if cmds.polyInfo(fn = True)[0].split(' ')[-2][0] == "-":cmds.polyNormal( nm=0 )
            cmds.polyExtrudeFacet( kft=False, ltz=val[-3])