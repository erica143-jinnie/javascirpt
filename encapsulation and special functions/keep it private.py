class myclass:
        __privateVar = 27;
        
        def __privMeth(self):
                Print("I'm inside class myclass")
         
        def hello(self):
                print("Private Variable value:"(myclass.__privateVar))

foo = myclass()
foo.hello()
foo.__privMeth