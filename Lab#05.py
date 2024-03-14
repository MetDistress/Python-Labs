""" Lab#05 / Christian Gower / 2.2.2023 """

class cg:
    c = 9
    m = 9
    g = 9
    print(c, m, g)
    def __init__(self):
        self.c = 0
        self.m = 0
        self.g = 0
        print(self.c, self.m, self.g)
    def set_c(self, c):
        self.c = c
    def set_m(self, m):
        self.m = m
    def set_g(self, g):
        self.g = g
    def get_c(self):
        return self.c
    def get_m(self):
        return self.m
    def get_g(self):
        return self.g

a1_cg = cg()
a1_cg.set_c(40)
a1_cg.set_m(20)
a1_cg.set_g(10)

a2_cg = cg()
a2_cg.set_c(320)
a2_cg.set_m(160)
a2_cg.set_g(80)

print('c', a1_cg.get_c())
print('m', a1_cg.get_m())
print('g', a1_cg.get_g())

print('c', a2_cg.get_c())
print('m', a2_cg.get_m())
print('g', a2_cg.get_g())
