import math
x=int(input("x값을 입력하시오."))
y=int(input("y값을 입력하시오."))
if x>0 and y>0:
    print("입력한 좌표는 1사분면입니다.".format(x, y))
elif x<0 and y>0:
    print("입력한 좌표는 2사분면입니다.".format(x, y))
elif x<0 and y<0:
    print("입력한 좌표는 3사분면입니다.".format(x, y))
else:
    print("입력한 좌표는 4사분면입니다.".format(x, y))

