def caesar_encode(text:str, shift:int= 3)-> str:
    t_list = []

    for n in text:
        if ord(n) > ord('C'):
            temp = chr(ord(n) - 3)
        elif ord(n) < ord('D'):
            temp = chr(ord('Z') - ord('C') + ord(n))


        t_list.append(temp)
    return "".join(t_list)

def caesar_decode(text:str, shift:int= 3)-> str:
    t_list = []

    for n in text:
        if ord(n) > ord('A'):
            temp = chr(ord(n) + 3)
        elif ord(n) < ord('B'):
            temp = chr(ord('D') - ord('A') + ord(n))

        t_list.append(temp)
    return "".join(t_list)


def main():
    text = input("영문자를 입력하세요.")
    print(caesar_encode(text))
    print(caesar_decode(text))


if __name__ == "__main__":
    main()


