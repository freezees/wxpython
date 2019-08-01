
class Human:
    def __init__(self, name , age ):
        self.name=name
        self.age=age
    def hello(self):
        print('I am human')


class Chinese(Person):
  def __init__(self,high, weight):
    self.high = high
    self.weight=weight
  hair='black'


p1 = Chinese(180,75)

p1.hello()
