from tkinter import *
import tkinter.ttk as ttk
import time
import pandas as pd
import telegram



mdf = pd.read_csv('mat_band.csv')#판다스 추출
values = mdf['material'].to_list()
num = mdf['band gap(eV)'].to_list()#리스트 변환

def caesar_encode():# 카이사르 암호로 변환
    return 
    text = ent_word.get()
    shift: int = 3
    t_list = []
    
    for n in text:
        
        if ord("a") <= ord(n) <= (ord("z") - shift) or ord("A") <=  ord(n) <= (ord("Z") - shift):
            t_list.append(chr(ord(n) + shift))
        
        else:
            t_list.append(chr(ord(n) - 26 + shift))
            
    ent_result_e.delete(0, "end")
    ent_result_e.insert(0, "".join(t_list))


def caesar_decode():# 카이사르 암호 해독
    return
    text = ent_code.get()
    shift: int = 3
    t_list = []
    
    for n in text:
        
        if (ord("a") + shift) <= ord(n) <= ord("z") or (ord("A") + shift) <=  ord(n) <= ord("Z"):
            t_list.append(chr(ord(n) - shift))
        
        else:
            t_list.append(chr(ord(n) + 26 - shift))
    
    ent_result_d.delete(0, "end")
    ent_result_d.insert(0, "".join(t_list))


def send_tel(text):
    
    token = '5422983794:AAHY3nfMoujJZxpFu6D2FefNh5kYkFP6HQ4'
    id = 5527810192
    bot = telegram.Bot(token=token)# token, id, bot은 설정값(고윳값)
    
    updates = bot.getUpdates()
    for u in updates:
        print(u.message)

    bot.sendMessage(chat_id=id, text=text)
    #bot.send_photo(chat_id =id, photo=open(image, 'rb'))
     



send_tel("hi")

def mat_gap():
    country  = e_mat.get()
    
    for i in range(0,len(values)):
        
        if(country == values[i]):
            e_gap.delete(0,END)
            e_gap.insert(0,num[i])
            break
        else:
            continue
    

def btncmd2():
    for i in range(1, 101) :
        time.sleep(0.01)
    
        p_var2.set(i) # progressbar 값 설정
        progressbar2.update() # 매번 동작시 반영 ui, 해당 값 표시 안할 경우 완료 후 표기됨
        
    print('happy')
    
def btnstop():
    ttk.Progressbar.stop()

window = Tk()
window.title("LED 물성 및 소자")
window.resizable(width=False, height=False)# 창 설정


#여기는 인코딩창 설정
frm_1 = Frame(master=window)
frm_1.grid(row=0, column=0, padx=10)


e_mat = ttk.Combobox(master=frm_1, width=30, values= values)
e_mat.set("물질")
e_mat.grid(row=0, column=0, sticky="e")

l_mat = Label(master=frm_1, text= "name", height=5)# 입력창
l_mat.grid(row=0, column=1, sticky="w")


frm_2 = Frame(master=window)

e_temp = Entry(master=window, width= 30)
l_temp = Label(master=window, text="Temp[K]", height=5)

e_temp.grid(row=0, column=2, padx=10)
l_temp.grid(row=0, column=3, padx=10)


frm_2 = Frame(master=window)
e_gap = Entry(master=frm_2, width=30)
l_gap = Label(master=frm_2, text= "Eg[eV]", height=3)

e_gap.grid(row=1, column=0, sticky="e")
l_gap.grid(row=1, column=1, sticky="w")


e_sat = Entry(master=window, width= 30)
l_sat = Label(master=window, text="Isat[A]")

frm_2.grid(row=1, column=0, padx=10)
e_sat.grid(row=1, column=2, padx=10)
l_sat.grid(row=1, column=3, padx=10)#디코딩 GUi


btn_gra= Button(master=window, text="그래프", width=20, height=5, command=caesar_encode)# 버튼
btn_chr = Button(master=window, text="물성",width=20, height=5, command=caesar_encode)# 버튼
btn_app = Button(master=window, text="적용",width=20, height=5, command=mat_gap)
btn_fab = Button(window, text="제작", width=20, height=5, command=btncmd2)

btn_gra.grid(row=3, column=2, pady=30, padx=30)
btn_app.grid(row=3, column=1, pady=30, padx=30)
btn_chr.grid(row=3, column=0, pady=30, padx=30)
btn_fab.grid(row=4, column=1, pady=30, padx=30)


p_var2 = DoubleVar() # 소수점 단위 실수 반영을 위해 Double 사용
progressbar2 = ttk.Progressbar(window, maximum=100, length=150, variable=p_var2)
progressbar2.grid(row=4, column=0, pady=30, padx=30)

window.mainloop()

