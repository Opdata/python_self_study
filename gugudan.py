dan = int(input('구구단 몇단을 계산할까요 ? : '))
i = 1
#print("구구단 %d단을 계산합니다."%dan)
print("구구단 {0}단을 계산합니다".format(dan))
for i in range(1,10,1):
    print("{0} X {1} = {2}".format(dan,i,dan*i))
