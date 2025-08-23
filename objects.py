class Dog(object):
  def __init__(self,name,age):
    self.name=name 
    self.age=age
  def speak(self):
    print(f'hello, i am{self.name}and i am{self.age} years old')
cat=Dog('tim',22)
puppy=Dog('ram',24)
cat.speak()
puppy.speak()
