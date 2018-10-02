#use of decorator
def d1(f):
    def in1():
        x=f()
        return x+100
    return in1
def d2(f):
    def in1():
        x=f()
        return x+10
    return in1
def d3(f):
    def in1():
        x=f()
        return x+1
    return in1
@d3#it will check is there any decorator,then control will go in d3
@d2
@d1
def w1():
    return 20
print(w1())
              
 
              
              
          
    
        
        
