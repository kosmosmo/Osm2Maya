from math import sin, cos, sqrt, atan2, radians
import math
class Convert(object):
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2

    def latDis(self):
        R = 6373.0
        lat1 = radians(self.p1[0])
        lon1 = radians(self.p1[1])
        lat2 = radians(self.p2[0])
        lon2 = radians(self.p2[1])
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = R * c
        return distance

    def pointDis(self):
        return math.hypot( self.p2[0] - self.p1[0], self.p2[1] - self.p1[1])

    def getMul(self):
        return self.latDis()*1000/self.pointDis()


p1 = [40.7088406,-74.0160348]
p2 = [40.7040245,-73.9948691]
a = Convert(p1,p2)
print a.latDis()

