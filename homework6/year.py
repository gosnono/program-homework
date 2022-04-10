def is_leap_year(y):

    if y%4 == 0:
        return True
    elif y%100 ==0:
        return False
    else:
        return False

def main():
    y=int(input("연도를 입력하시오."))
    print(is_leap_year(y))

if __name__ == "__main__":
    main()
