import random

total_sought = random.randint(2,20)
print('total sought: ',total_sought)
a = 1
b = 2
while True:
    ball1 = random.randint(1,10)
    ball2 = random.randint(1,10)
    total = ball1 + ball2
    print(f'result of picks %d and %d: {total}'%(a,b))    
    if total == total_sought:
        print('you got your total in %d picks'%b)
        break
    else:
        a = a + 1
        b = b + 1
        continue