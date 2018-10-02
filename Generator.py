#use of generator
def mygen():
    yield 'A'
    yield 2*'A'
    yield 'C'
g=mygen()
print(g)
print(next(g))
print(next(g))
print(next(g))
