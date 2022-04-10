한라봉 = int(input("한라봉 g을 쓰시오."))
한라봉calorie = (49/100)*한라봉
print("{}g의 칼로리는 = {}kcal 이다.".format(한라봉, 한라봉calorie))

딸기 = int(input("딸기 g을 쓰시오."))
딸기calorie = (35/100)*딸기
print("{}g의 칼로리는 = {}kcal이다.".format(딸기, 딸기calorie))

바나나 = int(input("바나나 g을 쓰시오."))
바나나calorie = (80/100)*바나나
print("{}g의 칼로리는 = {}kcal이다.".format(바나나, 바나나calorie))

한라봉calorie['(49/100)*한라봉']= 49


newdict = dict( 한라봉calorie = (49/100)*한라봉, 딸기calorie = (35/100)*딸기, 바나나calorie = (80/100)*바나나 )

name_and_calorie = [['한라봉', 10], ['딸기', 10], ['바나나', 10]]
dict(name_and_calorie)
for key in newdict:
    print(key)







