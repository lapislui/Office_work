class myclass:
    def __init__(self, x):
        self.x = x

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i < self.x:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration
    
nums= myclass(5)
myiter = iter(nums)
while True:
    try:
        print(next(myiter))
    except StopIteration:
        break
    