import random
i=4
j=0
value = random.randint(1,20)
print(value)
while(i > 0):
    j += 1
    compare = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: ".format(i)))
    if(value==compare):
        print("축하합니다. {}번 만에 숫자를 맞히셨습니다.".format(j))
        break
    else:
        i -= 1
        if(compare > value):
            print("Down")
        else:
            print("Up")
if(i<=0):
    print("아쉽습니다. 정답은 {}였습니다.".format(value))

print("git add .")

print("git status")
print("commit -m '코멘트'")