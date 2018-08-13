import random
guest_int = random.randint(1,100)
user_int = int(input('아무 숫자 입력 : '))
print(guest_int is not user_int)
while(guest_int is not user_int):
    if(guest_int > user_int):
        print("값이 작음.")
    else:
        print('값이 큼')
    user_int = int(input('숫자 다시 입력 : '))
else:
    print('정답입니다.')
