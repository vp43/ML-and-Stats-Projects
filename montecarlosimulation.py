#drunk man walk
import random
def random_walk(n):
    """Return coordinates after n block random walk"""
    x,y = 0,0
    for i in range(n):
        (dx,dy) = random.choice([(0,1),(1,0),(0,-1),(-1,0)])
        x += dx
        y+=dy
    return(x,y)

"""for i in range(25):
    walk = random_walk(10)
    print(walk,abs(walk[0])+abs(walk[1]))"""

number_of_walks = 10000

for walk_length in range(1,31):
    no_transport =0
    for i in range(10000):
        (x,y) = random_walk(walk_length)
        distance = abs(x)+abs(y)
        if distance <=4:
            no_transport+=1

    per = float(no_transport)/10000
    print(walk_length,per)

        






