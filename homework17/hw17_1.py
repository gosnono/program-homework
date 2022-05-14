import tkinter as tk

from requests import delete

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

window = tk.Tk()
window.title("암호 설정 및 해독기")
window.resizable(width=False, height=False)

frm_entry_e = tk.Frame(master=window)
ent_word_e = tk.Entry(master=frm_entry_e, width=30)
lbl_word_e = tk.Label(master=frm_entry_e, text= "word")

ent_word_e.grid(row=0, column=0, sticky="e")
lbl_word_e.grid(row=0, column=1, sticky="w")

btn_convert_e = tk.Button(master=window, text= "\N{RIGHTWARDS BLACK ARROW}", command=caesar_encode)

ent_result_e = tk.Entry(master=window, width= 30)
lbl_result_e = tk.Label(master=window, text="code")

frm_entry_e.grid(row=0, column=0, padx=10)
btn_convert_e.grid(row=0, column=1, pady=10)
ent_result_e.grid(row=0, column=2, padx=10)
lbl_result_e.grid(row=0, column=3, padx=10)

frm_entry_d = tk.Frame(master=window)
ent_code = tk.Entry(master=frm_entry_d, width=30)
lbl_code = tk.Label(master=frm_entry_d, text= "code")

ent_code.grid(row=1, column=0, sticky="e")
lbl_code.grid(row=1, column=1, sticky="w")

btn_convert_d = tk.Button(master=window, text= "\N{RIGHTWARDS BLACK ARROW}", command=caesar_decode)

ent_result_d = tk.Entry(master=window, width= 30)
lbl_result_d = tk.Label(master=window, text="word")

frm_entry_d.grid(row=1, column=0, padx=10)
btn_convert_d.grid(row=1, column=1, pady=10)
ent_result_d.grid(row=1, column=2, padx=10)
lbl_result_d.grid(row=1, column=3, padx=10)

window.mainloop()


