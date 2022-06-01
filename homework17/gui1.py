import tkinter as tk
from tkinter import simpledialog

window =tk.Tk()
window.withdraw()

def gui_input(text: str) -> str:
    return simpledialog.askstring(title="Test", prompt=text)

def main():
    input_text = gui_input("이름은?")
    print(input_text)
    input_text = gui_input("나이는?")
    print(input_text)

if __name__ =="__main__":
    main()

    