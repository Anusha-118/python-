class nanna:
    def na(self):
        m="manchithanam"
        a="amaayakam"
        print(m)
        print(a)
class amma:
    def ma(self):
        h="hardworking"
        k="kind hearted"
        m="mondi"
        print(h)
        print(k)
        print(m)
class anusha(nanna,amma):
    def anu(self):
        print("strong")
class chintu(nanna,amma):
    def chin(self):
        print("passionate")
a=anusha()
a.na()
a.ma()
a.anu()       
c=chintu()
c.na()
c.ma()
c.chin()
