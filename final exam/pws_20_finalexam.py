from tkinter import *
import tkinter.ttk as ttk
import time
import pandas as pd
import numpy as np
import telegram
from math import exp
import matplotlib.pyplot as plt


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


def IV_graph():# I-V 그래프 예측
    I_sat = float(e_sat.get())
    temp = float(e_temp.get())
    
    I_tot = []
    for voltage in range(-200, 200):
        I_tot.append((I_sat/1e6)*(exp(0.01*voltage/(8.617e-4*temp))- 1)) # I_tot = I_sat(exp(qV/kT) - 1), I_sat[uA]: 역방향 포화전류
        #차트 -2V ~ 2V 사이 계산, 자세한 데이터를 위해, 8.617e-4는 상수임.
    
    plt.plot(range(-200, 200), I_tot, label = "Diode Curve", color = "red")#차트 -2V ~ 2V 사이 계산 plot
    plt.title("I-V Curve")
    plt.xlabel("voltage[e-2V]")
    plt.ylabel("current[A]")
    plt.legend()
    plt.show()


def save_data():# I-V 데이터 저장
    I_sat = float(e_sat.get())
    temp = float(e_temp.get())
    
    I_tot = []
    for voltage in range(-200, 200):
        I_tot.append((I_sat/1e6)*(exp(0.01*voltage/(8.617e-4*temp))- 1)) # I_tot = I_sat(exp(qV/kT) - 1), I_sat[uA]: 역방향 포화전류
        #차트 -2V ~ 2V 사이 계산, 자세한 데이터를 위해, 8.617e-4는 상수임.
    
    plt.plot(range(-200, 200), I_tot, label = "Diode Curve", color = "red")#차트 -2V ~ 2V 사이 계산 plot
    plt.title("I-V Curve")
    plt.xlabel("voltage[e-2V]")
    plt.ylabel("current[A]")
    plt.legend()
    plt.savefig("IV_curve.png")# plot 저장
    
    tf = pd.DataFrame(I_tot)
    tf.columns =['I(A)']
    tf.to_csv("IV_predic.csv")# 데이터 저장

    
def send_tel(text):# 텔레그램으로 보내기
    
    token = '5422983794:AAHY3nfMoujJZxpFu6D2FefNh5kYkFP6HQ4'
    id = 5527810192
    bot = telegram.Bot(token=token)# token, id, bot은 설정값(고윳값)
    
    updates = bot.getUpdates()
    for u in updates:
        print(u.message)

    bot.sendMessage(chat_id=id, text=text)
    #bot.send_photo(chat_id =id, photo=open(image, 'rb'))
     


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
    
        p_var.set(i) # progressbar 값 설정
        progressbar.update() # 매번 동작시 반영 ui, 해당 값 표시 안할 경우 완료 후 표기됨
        
    print('happy')
    
def btnstop():
    ttk.Progressbar.stop()



window = Tk()
window.title("LED 물성 및 소자")
window.resizable()# 창 설정


#1층
frm_1 = Frame(master=window)
frm_1.grid(row=0, column=0, padx=20)


#물질바
e_mat = ttk.Combobox(master=frm_1, width=30, values= values)
e_mat.set("물질")
e_mat.grid(row=0, column=0, sticky="e")

l_mat = Label(master=frm_1, text= "name", height=5)
l_mat.grid(row=0, column=1, sticky="w")


#2층
frm_2 = Frame(master=window)
frm_2.grid(row=1, column=0, padx=20)


#온도바
e_temp = Entry(master=window, width= 30)
l_temp = Label(master=window, text="Temp[K]", height=5)

e_temp.grid(row=0, column=2, padx=20)
l_temp.grid(row=0, column=3, padx=20)


#밴드갭바
e_gap = Entry(master=frm_2, width=30)
l_gap = Label(master=frm_2, text= "Eg[eV]", height=3)

e_gap.grid(row=1, column=0, sticky="e")
l_gap.grid(row=1, column=1, sticky="w")


#sat전류바
e_sat = Entry(master=window, width= 30)
l_sat = Label(master=window, text="Isat[uA]")

e_sat.grid(row=1, column=2, padx=20)
l_sat.grid(row=1, column=3, padx=20)


#버튼
btn_gra= Button(master=window, text="그래프", width=15, height=2, command=IV_graph)
btn_chr = Button(master=window, text="물성",width=15, height=2, command=caesar_encode)
btn_app = Button(master=window, text="적용",width=15, height=2, command=mat_gap)
btn_sav = Button(master=window, text="저장", width=15, height=2, command=save_data)
btn_fab = Button(window, text="제작", width=20, height=2, command=btncmd2)

btn_chr.grid(row=5, column=0, pady=20, padx=20)
btn_app.grid(row=5, column=1, pady=20, padx=20)
btn_gra.grid(row=5, column=2, pady=20, padx=20)
btn_sav.grid(row=5, column=3, pady=20, padx=20)
btn_fab.grid(row=6, column=1, pady=20, padx=20)


#진행바
p_var = DoubleVar() # 소수점 단위 실수 반영을 위해 Double 사용
progressbar = ttk.Progressbar(window, maximum=100, length=150, variable=p_var)
progressbar.grid(row=6, column=0, pady=20, padx=20)

window.mainloop()

