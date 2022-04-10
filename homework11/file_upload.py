import requests
import os

def main():
    URL = "https://data.kma.go.kr/stcs/grnd/grndTaList.do?pgmNo=70"

    filename = "./ta_20220409150223.csv"

    if not os.path.exists(filename):
        with open(filename, "w") as f:
            res = requests.get(URL)
            res.encoding = "UTF-8"
            f.write(res.text)
            print(res.status_code)
    else:
        print("이미 다운 받음")


def submit(name: str, hot_date: str, tmax: float, cold_date: str, tmin: float) -> None:
    URL = "https://data.kma.go.kr/stcs/grnd/grndTaList.do?pgmNo=70"
    PARAMS = {
        '제출자': name,
        '최고기온': tmax,
        '최고기온날짜': hot_date,
        '최저기온': tmin,
        '최저기온날짜': cold_date}

    r = requests.get(url=URL, params=PARAMS)
    if r.status_code !=200:
        print("과제가 정상적으로 제출되지 않았습니다.")

if __name__=="__main__":
    main()

