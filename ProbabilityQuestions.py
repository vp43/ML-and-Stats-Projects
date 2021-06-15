#rolling 2 die
import random
n = 1000
count = 0
i=0

while i<n+1:
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    total = die1+die2
    if total>7:
        count+=1
    i+=1
prec_tot = (count/n)*100
print(prec_tot)

balls in a bag
import random
import numpy as np
dict1 = {}

for i in range(60):
    if i<10:
        dict1[i]="white"
    elif i >9 and i<30:
        dict1[i] = "red"
    else:
        dict1[i] = "green"
n =1000
partacount = 0

for i in range(1000):
    lst = []
    for i in range(5):
        lst.append(dict1[random.randint(0,59)])
    
    lst = np.array(lst)

    white = sum(lst =="white")
    red = sum(lst=="red")

    if white ==3 and red ==2:
        partacount +=1

print((partacount/1000)*100)

"#coin flip game
import random
def flip(N)


N=10000
total_lose = 0
n =0

for i in range(N):
    bet = random.choice([-10,20])
    if bet<0:
        total_lose +=1
prec = total_lose/N
print(prec)












