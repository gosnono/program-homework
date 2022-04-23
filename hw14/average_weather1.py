import os
from typing import List

import pit as pit
import requests
import matplotlib.pyplot as plt


def download_weather(filename: str) -> None:
    """기상청에서 자료를 다운받아서 저장합니다."""
    URL = "https://data.kma.go.kr/stcs/grnd/downloadGrndTaList.do?fileType=csv&pgmNo=70&menuNo=432&serviceSe=F00101&stdrMg=99999&startDt=19820101&endDt=20211231&taElement=MIN&taElement=AVG&taElement=MAX&stnGroupSns=&selectType=1&mddlClssCd=SFC01&dataFormCd=F00501&dataTypeCd=standard&startDay=19820101&startYear=1982&endDay=20211231&endYear=2021&startMonth=01&endMonth=12&sesnCd=0&txtStnNm=%EC%A0%84%EC%A3%BC&stnId=146&areaId=&gFontSize="

    if not os.path.exists(filename):
        res = requests.get(URL)
        with open(filename, "w", newline="") as f:
            f.write(res.text)


def str2float(text: str, default_value: float = -999) -> float:
    try:
        return float(text)
    except ValueError:
        return default_value


def read_data(filename) -> (List[str], List[float], List[float]):
    """기상자료를 읽어서 날짜, 최저기온, 최고기온 리스트를 리턴합니다."""
    date_list = []
    tavg_list = []
    tmin_list = []
    tmax_list = []

    with open(filename) as f:
        lines = f.readlines()
        for line in lines[8:]:
            line = line.strip()
            if line == "":
                continue
            tokens = line.split(",")
            date_list.append(tokens[0].split("-"))
            tavg_list.append(str2float(tokens[2], 999))
            tmin_list.append(str2float(tokens[3], 999))
            tmax_list.append(str2float(tokens[4], -999))

    return date_list, tavg_list, tmin_list, tmax_list


def main():
    # 1) 데이터 구해오기 (기상청)
    filename = "./history_jeonju.csv"
    download_weather(filename)

    # 2) 데이터 읽기 (주의: 빈 데이터 처리하기)
    dates, tavg, tmin, tmax = read_data(filename)

    year = int(input("연도: "))
    month = int(input("월: "))
    day = int(input("일: "))


    tavg_history = [x[1] for x in zip(dates, tavg)
                    if (int(x[0][1]) == month) and (int(x[0][2]) == day)]
    dates_history = [x[0] for x in zip(dates, tavg)
                     if (int(x[0][1]) == month) and (int(x[0][2]) == day)]
    tokens = sum(dates_history, [])

    year_token = tokens[0::3]

    tavg_sorted = sorted(tavg_history, reverse=True)

    tavg_history_pick = []
    for x in zip(dates, tavg):
        if (int(x[0][1]) == month) and (int(x[0][2]) == day) and (
                int(x[0][0]) == year):
            tavg_history_pick = x[1]

    # num_tavg = 어떻게 정의해야할지 모르겠습니다. tavg.sorted(float(tavg_history_pick))

    print("{},{},{} 온도는 {}번째 높습니다.".format(year, month, day, num_tavg))

    plt.plot(year_token, tavg_history, label="temp_avg", color="green")
    plt.title("temp_chart_list")
    plt.xlabel("year")
    plt.ylabel("temp")
    plt.axhline(y=tavg_history_pick, color='pink', linestyle=':')
    plt.xticks(tokens[0::6], rotation=90)
    plt.legend()
    plt.show()

if __name__ =="__main__":
    main()
