import requests
import os

def main():
    URL = "http://sobi.chonbuk.ac.kr/function/ajax.get.rest.data.php"
    data = {"code": "mobile3"}

    filename = "./cafeteria_menu.html"

    if not os.path.exists(filename):
        with open("./cafeteria_menu.html","w", encoding="UTF-8") as f:
            res = requests.post(URL, data=data)
            print(res.status_code)
            res.encoding = "UTF-8"
            f.write(res.text)

    else:
        print("이미 파일을 다운로드 받았습니다.")

if __name__ =="__mani__":
    main()

