import math

x1=int(input("x1의 값을 쓰시오."))
x2=int(input("x2의 값을 쓰시오."))
y1=int(input("y1의 값을 쓰시오."))
y2=int(input("y2의 값을 쓰시오."))

distance = math.sqrt((x2-x1)**2+(y2-y1)**2)

print("x1값 {}, x2값 {}, y1값 {}, y2값 {} 이면 = distance 값은 {}이다.".format(x1, x2, y1, y2, distance))
