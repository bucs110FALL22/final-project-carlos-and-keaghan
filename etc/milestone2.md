class Rectangle: 
  def __init__(self, x=0, y=0, width=0, height=0):
    self.x = x
    self.y = y
    self.width = width
    self.height = height

  def __str__(self):
    return str("x =",self.x, "y =", self.y,"Height =",self.height,          "Width =",self.width)
  
Class Screen: 
  def __init__(self,filename,x,y,height,width):
    self.rect = Rectangle.Rectangle(x,y,height,width)
    self.image = filename

  def getRect(self):
    return(self.rect)


Class Enter_problem:
  def __init__(self, input = none):
    self.rect = Rectangle.Rectangle(x,y,height,width)
    self.data = []

  def add_data(self, data):
    self.data.append(data)

  def __str__(self):
    problem_str = ""
    for d in self.data:
        point_str = f" ({d.x}, {d.y})"
    return f"{problem_str}"

