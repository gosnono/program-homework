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
    x =dates, tavg
    # 여름철, 겨울철 평균기온 분포
    tavg_summer = [x[1]for x in zip(dates, tavg) if int(x[0][1]) == 8]
    tavg_winter = [x[1]for x in zip(dates, tavg) if int(x[0][1]) == 1]

    plt.hist(tavg_summer, color="r", bins=50, label ="summer")
    plt.hist(tavg_winter, color="b", bins=50, label ="winter")

    plt.show()

    #2) 특정 날짜의 평균 기온 그려보기
    tavg_history = [x[1] for x in zip(dates, tavg) if (int(x[0][1])==5) and int(x[0][2])== 15]
    tavg_birthday = [x[1] for x in zip(dates, tavg) if (int(x[0][1]) == 5) and int(x[0][2]) == 15 and int(x[0][0]) >= 2002]
    # print(tavg_birthday)
    plt.plot(range(1982, 2022), tavg_history, "pink")
    plt.plot(range(2002, 2022), tavg_birthday, "r")
    plt.axhline(y=tavg_birthday[-2], color = "black", linestyle='--')

    plt.plot(result,'green')
    plt.show()


if __name__ == "__main__":
    main()

