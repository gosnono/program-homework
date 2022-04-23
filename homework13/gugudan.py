import random

def main():
    n = 5
    score = 0

    for i in range(n):
        x = random.randint(1, 9)
        y = random.randint(2, 9)
        ans = int(input("{} * {} = ".format(x, y)))
        if ans == x * y:
            score += 1
            print("정답입니다.")
        else:
            print("오답입니다.")

    print("5개 증 {}개 정답입니다.".format(score))
    print("점수는 {:0f}점입니다.".format(100* score/n))
if __name__ =="__main__":
    main()

