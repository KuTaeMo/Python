from unittest import result


class FourCal:

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result


class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result


class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second


a = FourCal(4, 2)

print("============")
print("add : ", a.add())
print("sub : ", a.sub())
print("mul : ", a.mul())
print("div : ", a.div())
print("============")

b = MoreFourCal(4, 2)

print("add : ", b.add())
print("sub : ", b.sub())
print("mul : ", b.mul())
print("div : ", b.div())
print("pow : ", b.pow())
print("============")

c = SafeFourCal(4, 0)

print("add : ", c.add())
print("sub : ", c.sub())
print("mul : ", c.mul())
print("div : ", c.div())
print("============")
