class grandparent:
    prabha="anusha"
    print(prabha)
    def prabhas(self):
        a="anu"
        b="bannu"
        c="chintu"
        print(a)
        print(b)
        print(c)
class parent(grandparent):
    print("working")
    def ammi(self):
        d="dadi"
        e="eppi"
        print(d)
        print(e)
class child(parent):
    print("spending")
    def appi(self):
        f="fuggi"
        g="gayi"
        print(f)
        print(g)
    def mani(self):
        print("relax")
c=child()
c.prabhas()
c.ammi()
c.appi()
c.mani()
        
        
