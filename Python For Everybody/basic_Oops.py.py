class partyanimal:
    x = 0
    name  = ""
    def __init__(self,z):
        self.name  = z
        print (self.name," constructed")
    def party(self):
        self.x = self.x + 1
        print (self.name,"party count", self.x)

class fan (partyanimal):
    points = 0

    def down (self):
        self.points  = self.points + 7
        self.party()
        print (self.name,"points",self.points)
s = partyanimal('Sally')
s.party()
j = fan ('jim')
j.party()
j.down()
