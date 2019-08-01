class A():
   def __init__(self):
      self.n=2
   def add(self,m):
      print('A')
      self.n=self.n+2*m

class B(A):
   def __init__(self):
      self.n=3
   def add(self,m):
      print('B')
      self.n=self.n+1

class C(B):
   def __init__(self):
      self.n=3
   def add(self,m):
      super(B,self).add(m)
      print('C')
      self.n=self.n+4


x=C()
x.add(3)
print(x.n)
