
class cylinder:
    def __init__(self,height,radius):
        self.height=height
        self.radius=radius

    def volume(self):
        return self.height * 3.14 * (self.radius)**2

    def surfacevolume(self):
        top=(3.14)*(self.radius)**2
        return 2*top+2*3.14*self.radius*self.height

c=cylinder(3,5)
print(c.volume())
print(c.surfacevolume())






class line():
    def __init__(self,cor1,cor2):
        self.cor1=cor1
        self.cor2=cor2

    def distance(self):
        x1,y1=self.cor1
        x2,y2=self.cor2
        return ((x2-x1)**2/(y2-y1)**2)**0.5

    def slope(self):
        x1,y1=self.cor1
        x2,y2=self.cor2
        return float (y2-y1)/(x2-x1)
coordinate1=(3,4)
coordinate2=(5,6)
x=line(coordinate1,coordinate2)
print(x.distance())


