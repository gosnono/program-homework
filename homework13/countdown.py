import time

def read_input():
    return 5


def main():
    # 몇초를 카운트 할지 시간 입력
    countdown_sec = read_input()


    # 주어진 시간에서 매 1초마다 시간이 1초씩 줄어들고, 그때 남은 시간을 출력하고 시간이 0이되면 멈춘다.
    while countdown_sec>0:
        print("남은 시간은 {:2d}초".format(countdown_sec))
        # 1초 쉬고
        time.sleep(1)
        countdown_sec -= 1


    # 0초가 되면 소리 낸다.
    print("카운트 다운이 끝났습니다.")


if __name__ == "__main__":
    main()


