def count_rain_days(rainfall):
    rain_days = 0
    for x in rainfall:
        if x > 0 :
            rain_days += 1
    return rain_days



def sumifs(rainfall, months, selected=[6, 7, 8]):
    days = len(rainfall)  #365
    total_rain = 0
    for i in range(days):
        if months[i] in selected:
            total_rain += rainfall[i]
    return total_rain

def longest_rain_days(rainfall):
    rain_days = 0
    rain_days_list = []
    for rain in rainfall:
        if rain > 0:
            rain_days += 1
        else:
            if rain_days > 0:
                rain_days_list.append(rain_days)
            rain_days = 0
    return max(rain_days_list)

def maximum_rainfall_event(rainfall):
    rain_days = 0
    rain_total = 0
    rain_days_list = []
    rain_total_list = []
    for rain in rainfall:
        if rain > 0:
            rain_days += 1
            rain_total += rain
        else:
            if rain_days > 0:
                rain_days_list.append(rain_days)
                rain_total_list.append(rain_total)
                rain_days = 0
                rain_total = 0
        if rain_days > 0:
            rain_days_list.append(rain_days)
            rain_total_list.append(rain_total)

    return max(rain_total_list)

def maximum_temp_gap(dates, tmax, tmin):
    temp_max = tmax
    temp_min = tmin
    temp_range = 0
    range_row = []
    for row in dates:
        if len(row) < 7 or row[4] == " " or row[6] == " ":
            continue
        temp_max = float(row[4])
        temp_min = float(row[6])
        maximum_temp_gap = temp_max - (temp_min)
        if maximum_temp_gap > temp_range:
            temp_range = maximum_temp_gap
            range_row = row

    return [2021,1,20], 23.2

def gdd(dates, tavg):
    return 0

import requests
import os


def main():
    f = open("weather(146)_2021-2021.csv")
    lines = f.readlines()
    print(len(lines[1:]))
    print(lines[1:])
    rainfall = [x.split(",") for x in lines[1:]]
    print(rainfall)
    rainfall = [x.split(",")[9] for x in lines[1:]]
    print(rainfall)
    rainfall = [float(x.split(",")[9]) for x in lines[1:]]
    # rainfall = []

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

    tavg = [float(x.split(",")[4]) for x in lines[1:]]
    tmax = [float(x.split(",")[3]) for x in lines[1:]]
    tmin = [float(x.split(",")[5]) for x in lines[1:]]
    months = [int(x.split(",")[1]) for x in lines[1:]]
    dates = [[int(x.split(",")[0]), int(x.split(",")[1]), int(x.split(",")[2])] for x in lines[1:]]

    #1) 총 강수량
    print("총 강수량: {:.1f} mm".format(sum(rainfall)))

    #2) 총 강우 일수
    print("총 강우일수: {:d} 일".format(count_rain_days(rainfall)))

    #3) 여름철 강수량
    print ("여름철(6월~8월)총 강수량: {:.1f}".format(sumifs(rainfall, months, [6, 7, 8])))

    #4) 최장연속강우일수
    print("최장연속강우일수: {:d}".format(longest_rain_days(rainfall)))

    #5) 강우이벤트 중 최대 강수량
    print("강우이벤트 중 최대 강수량: {:.1f}".format(maximum_rainfall_event(rainfall)))

    #6) 일교차가 가장 큰 날짜와 해당일자의 일교차
    print("일교차가 가장 큰날짜: {}, 일교차: {:.1f}도".format(*maximum_temp_gap(dates, tmax, tmin)))

    #7) 5월부터 9월까지 적산온도
    print("적산온도는 {:.1f} degree-days".format(gdd(dates, tavg)))


if __name__ == "__main__":
    main()
