class Animal(ABC):
      def move(self):
            pass
class human(Animal):
      def move(self):
            print("I can walk and run")
class snake(Animal):
      def move(self):
            print("I can crawl")
class dog(Animal):
      def move(self):
            print("I can bark")
class lion(Animal):
      def move(self):
            print("I can roar")
R = human()
R.move()

K = dog()
K.move()

R = dog()
R.move()

k = lion()
k.move()
