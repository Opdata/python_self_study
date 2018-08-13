user = int(input('구구단 몇 단을 계산할까요? : '))
while(user!=0):
    for i in range(1,10):
        print("%d X %d = %d" %(user,i,user*i))
    user=int(input('구구단 몇 단을 계산할까요? : '))
else :
    print("구구단을 종료합니다.")
