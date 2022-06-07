class Rectangle:
  def __init__(self, width = 0, height = 0):
    self.width = width
    self.height = height
     
  def __str__(self):    
    return "Rectangle(width={}, height={})".format(self.width, self.height)
    
  def set_width(self,width):
    self.width = width
    
  def set_height(self,high):
    self.height = high
    
  def get_area(self):
    return (self.width * self.height)
    
  def get_perimeter(self):
    return (2 * self.width + 2 * self.height)
    
  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2)** .5)
    
  def get_picture(self):
    if self.width < 50 and self.height < 50:
      tmp = ''
      for i in range(self.height):
        for y in range(self.width):
          tmp += '*'
        tmp += '\n'
      return tmp
    return 'Too big for picture.'
  def get_amount_inside(self, shape):
    return self.get_area()//shape.get_area()
    
class Square(Rectangle):
  def __init__(self, length = 0):
    super().__init__(length,length)
     
  def __str__(self):
    return "Square(side={})".format(self.width)
  def set_side(self, length):
    self.set_height(length)
    self.set_width(length)