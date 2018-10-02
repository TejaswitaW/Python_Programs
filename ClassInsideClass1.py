#use of class inside class
class Human:
    def __init__(self):
        self.name="Durga"
        self.head=self.Head()
        self.brain=self.Brain()
    def disp(self):
        print("Hello  ",self.name)
    class Head:
        def talk(self):
            print("Talking...")
    class Brain:
        def think(self):
            print("Thinking...")
h=Human()
h.disp()
h.head.talk()
h.brain.think()
    
