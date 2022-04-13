import os
from typing import List

import requests

import hw11_submission


def download_weather(filename: str) -> None:
    """기상청에서 자료를 다운받아서 저장합니다."""
    URL = "https://data.kma.go.kr/stcs/grnd/downloadGrndTaList.do?fileType=csv&pgmNo=70&menuNo=432&serviceSe=F00101&stdrMg=99999&startDt=19040101&endDt=20220405&taElement=MIN&taElement=AVG&taElement=MAX&stnGroupSns=&selectType=1&mddlClssCd=SFC01&dataFormCd=F00501&dataTypeCd=standard&startDay=19040101&startYear=1904&endDay=20220405&endYear=2022&startMonth=01&endMonth=12&sesnCd=0&txtStnNm=%EC%A0%84%EC%A3%BC&stnId=146&areaId=&gFontSize="

    if not os.path.exists(filename):
        res = requests.get(URL)
        with open(filename, "w") as f:
            f.write(res.text)

def find_hottest_date(dates: List[str], tmax: List[float]) -> (str, float):
    no_dates = len(dates)
    tm = -999
    tm_date = None
    for i in range(no_dates):
        if tm< tmax[i]:
            tm = tmax[i]
            tm_date = dates[i]


def find_coldest_date(dates: List[str], tmin: List[float]):
    no_dates = len(dates)
    tmin_date = None
    tmin = 999

    for i in range(no_dates):
        if tm > tmin[i]:
            tm = tmin[i]
            tm_date = dates[i]




def read_data(filename) -> (List[str], List[float], List[float]):
    """기상자료를 읽어서 날짜, 최저기온, 최고기온 리스트를 리턴합니다."""
    date_list = []
    tmin_list = []
    tmax_list = []

    with open(filename) as f:
        lines = f.readlines()
        for line in lines[8:]:
            line = line.strip()
            tokens = line.split(",")
            date_list.append(tokens[0])
            print(line)
            print(tokens[3])

            if tokens[3] == "":
                tmin = 999
            else:
                tmin = float(tokens[3])
            if tokens[4] == "":
                tmax = -999
            else:
                print("!!"+ tokens[4]+"!!")
                tmax = float(tokens[4])
            tmin_list.append(tmin)
            tmax_list.append(tmax)



    return date_list, tmin_list, tmax_list


def main():
    # 1) 데이터 구해오기 (기상청)
    filename = "./history_jeonju.csv"
    download_weather(filename)

    # 2) 데이터 읽기 (주의: 빈 데이터 처리하기)
    dates, tmin, tmax = read_data(filename)

    # 3) 주어진 문제 계산하기
    hottest_date, hottest_temp = find_hottest_date(dates, tmax)
    coldest_date, coldest_temp = find_coldest_date(dates, tmin)

    print(
        "홍길동",
        hottest_date, hottest_temp,
        coldest_date, coldest_temp,
    )

    # 4) 결과를 서버로 보내기
    # hw11_submission.submit(
    #     "홍길동",
    #     hottest_date, hottest_temp,
    #     coldest_date, coldest_temp,
    # )


def str2float(text: str, default_value: float = -999) -> float:
    try:
        return float(text)
    except ValueError:
        return default_value


if __name__ == "__main__":
    main()
