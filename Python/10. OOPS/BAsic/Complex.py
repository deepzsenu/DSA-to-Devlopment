class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def print(self):
        print(str(self.real)+'+i' + str(self.img))

    def add(self, C):
        self.real += C.real
        self.img += C.img


a = Complex(1, 2)
a.print()

c2 = Complex(4, 5)

a.add(c2)

a.print()