# Exercice 1 compte bancaire
class Point:
    def __init__(self, x, y, z=None):
        self.x = x;
        self.y = y;
        self.z = z;

    def ToString(self):
        print("P(", self.x, " ,", self.y,self.z == None and ")" or  ", "+str(self.z) + ")")
