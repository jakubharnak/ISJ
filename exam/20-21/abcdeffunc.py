class A(object):
    def __init__(self):
        print("entering A")
        super().__init__()
        print("leaving A")

class B(A):
    def __init__(self):
        print("entering B")
        super().__init__()
        print("leaving B")

class C(A):
    def __init__(self):
        print("entering C")
        super().__init__()
        print("leaving C")

class D(object):
    def __init__(self):
        print("entering D")
        super().__init__()
        print("leaving D")

class E(object):
    def __init__(self):
        print("no super() in E")
    
class F(object):
    def __init__(self):
        print("entering F")
        super().__init__()
        print("leaving F")

class G(B, C, D, E, F):
    def __init__(self):
        print("entering G")
        super().__init__()
        print("leaving G")

g = G()

# entering G
# entering B
# entering C
# entering A
# entering D
# no super() in E
# leaving D
# leaving A
# leaving C
# leaving B
# leaving G