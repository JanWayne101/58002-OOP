class Circle:
  def __init__(self, radius):
    self.radius = radius
    self.pi = 3.14159

  def Perimeter(self):
     return 2*self.pi*self.radius

  def Area(self):
      return self.pi*self.radius**2

  def Display(self):
      print("Perimeter:", self.Perimeter())
      print("Area", self.Area())

radius = float(input("Enter the radius od the circle: "))
c = Circle(radius)
c.Display()
