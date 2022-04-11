class Bird:
    def fly(self):
        raise NotImplementedError


class Eagle(Bird):
    def fly(self):
        print("eagle is very fast bird")


eagle = Eagle()
eagle.fly()
