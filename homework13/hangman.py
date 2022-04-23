import random

def main():
    succes = "apple"
    answer = ["_"] * len(succes)
    answer = ["_" for x in range[len(answer)]


    trials = 7

    while trials > 0:
        print("".join(answer))
        letter = input("알파벳을 입력하시오.")
        if letter in succes:
            for i in range(len(succes)):
                if letter == succes[i]:
                    answer[i] = letter
        else:
            trials -= 1
        if "_" not in answer:
            break

    if trials > 0:
        print("성공입니다.")
    else:
        print("실패입니다.".format(succes))




if __name__ =="__main__":
    main()