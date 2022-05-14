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
    print("초성게임 START~!")
    print("기회는 3번")
    trial = 3

    while trial > 0:
        word = str(words[random.randint(0, len(words) - 1)])
        r_lst = []

        for w in list(word.strip()):

            if '가' <= w <= '힣':

                ch1 = (ord(w) - ord('가')) // (21 * 28)
                r_lst.append(CHOSUNG_LIST[ch1])

            else:
                r_lst.append([w])
        r_lst = "".join(r_lst)

        answer = gui_input("{}초성에 알맞은 단어는?".format(r_lst))

        if word == answer:
            print("정답")
            break

        else:
            trial -= 1
            print("오답입니다!\n남은 목숨: {}개".format(trial))


    if trial == 0:
        print("다음에 다시 도전하세요~")


window = tk.Tk()
window.withdraw()


def main():
    words = ["닥터스트레인지", "헐크", "캡틴아메리카", "아이언맨", "스파이더맨","블랙위도우"]
    chosung_game(words)


if __name__ == "__main__":
    main()
