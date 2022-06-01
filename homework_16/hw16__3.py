import tkinter as tk
from tkinter import simpledialog
import random

# 초성 리스트. 00 ~ 18
CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
# 중성 리스트. 00 ~ 20
JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ',
                 'ㅣ']
# 종성 리스트. 00 ~ 27 + 1(1개 없음)
JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ',
                 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

def gui_input(text: str) -> str:
    return simpledialog.askstring(title="초성게임", prompt=text)

def chosung_game(words):
    print("초성게임 START!")
    print("기회 5번")

    trials = 5

    while trials > 0:
        word = str(words[random.randint(0, len(words) - 1)])
        r_lst = []

        for w in list(word.strip()):

            if '가' <= w <= '힣':
                ch1 = (ord(w) - ord('가')) // (21 * 28)
                r_lst.append(CHOSUNG_LIST[ch1])

            else:
                r_lst.append([w])
        r_lst = "".join(r_lst)

        print("{}".format(r_lst))
        answer = gui_input("{}에 정답을 입력하세요.".format(r_lst))

        if word == answer:
            print("성공입니다.")
            break

        else:
            trials -=1
            print("실패입니다.")

window = tk.Tk()
window.withdraw()

def main():
    words = ["스파이더맨", "닥터스트레인지", "아이언맨", "토르", "헐크", "캡틴아메리카"]
    print(len(words))
    chosung_game(words)


if __name__ =="__main__":
    main()
