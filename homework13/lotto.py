import random

def get_lotto():
    lotto = []
    while len(lotto) < 9:
        num = random.randint(1, 45)
        if num not in lotto:
            lotto.append(num)
    return lotto

def main():
    lotto = get_lotto()
    print(lotto)

if __name__ == "__main__":
    main()
