def decor1(func):
    def inner(name):
        if name=="Sunny":
            print("Hello Sunny bad morning")
        else:
            func(name)
    return inner

def wish(name):
    print("Hellooooo!!!!!!!!!",name,"Good Morning")

d=decor1(wish)
print(type(d("Sunny")))
wish("Tejaswita")
wish("Manisha")
wish("Rita")
d("Sunny")
