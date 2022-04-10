import requests
import os

def main():
    URL = "http://api.taegon.kr/stations/146/?sy=2021&ey=2021&format=csv"

    filename = "./weather_146_2021.csv"

    if not os.path.exists(filename):
        with open(filename, "w") as f:
            res = requests.get(URL)
            res.encoding = "UTF-8"
            f.write(res.text)
            print(res.status_code)
    else:
        print("이미 다운 받음")

if __name__ =="__main__":
    main()

