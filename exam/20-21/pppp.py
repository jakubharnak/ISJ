class First():
    def __init__(self, *args, ** kwargs):
        print("First 1")
        super(First, self) .__init__()
        print("First 2")
class Second():
    def __init__(self, *args, ** kwargs):
        print("Second 1")
        super(Second, self) .__init__()
        print("Second 2")
class Third(First, Second):
    def __init__(self, *args, ** kwargs):
        print("Third 1")
        super(Third, self) .__init__()
        print("Third 2")
        
third = Third()

# Third 1
# First 1
# Second 1
# Second 2
# First 2
# Third 2