import os
import numpy as np

path = r"C:/Users/jaein/PycharmProjects/2022/2022/final exam/diode" # 폴더 경로
os.chdir(path) # 해당 폴더로 이동
files = os.listdir(path) # 해당 폴더에 있는 파일 이름을 리스트 형태로 받음

png_img = []
for file in files:
    if '.png' in file:
        f = np.fromfile('blue')
        png_img.append(f)
