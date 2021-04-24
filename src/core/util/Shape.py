class Shape:
    def __init__(self, arr):
        if isinstance(arr, list):
            self.shape = [0,0,0,0]
            for i in range(4):
                self.shape[i] = arr[i]
        elif isinstance(arr, Shape):
            self.shape = [0,0,0,0]
            for i in range(4):
                self.shape[i] = arr.shape[i]
    def __add__(self, num):
        inter = [(self.shape[i] + num.shape[i]) for i in range(4)]
        return Shape(inter)
    def __sub__(self, num):
        inter = [(self.shape[i] - num.shape[i]) for i in range(4)]
        return Shape(inter)
    def __mul__(self, num):
        inter = [(self.shape[i] * num.shape[i]) for i in range(4)]
        return Shape(inter)
    def __floordiv__(self, num):
        inter = [(self.shape[i] // num.shape[i]) for i in range(4)]
        return Shape(inter)
    def __str__(self):
        return "[{},{},{},{}]".format(self.shape[3],self.shape[2],self.shape[1],self.shape[0])
    def __getitem__(self, index):
        if index<0 or 4<=index:
            raise Exception('Out of Range')
        return self.shape[index]
    def size(self):
        return self.shape[3]*self.shape[2]*self.shape[1]*self.shape[0]
