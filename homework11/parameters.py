import requests
import hw11_submission




def main():
    hw11_submission.submit("이재인", "2021-08-15", 40.1, "1978-01-04", -32.5)

    URL ="https://data.kma.go.kr/stcs/grnd/downloadGrndTaList.do?fileType=csv&pgmNo=70&menuNo=432&serviceSe=F00101&stdrMg=99999&startDt=19040101&endDt=20220405&taElement=MIN&taElement=AVG&taElement=MAX&stnGroupSns=&selectType=1&mddlClssCd=SFC01&dataFormCd=F00501&dataTypeCd=standard&startDay=19040101&startYear=1904&endDay=20220405&endYear=2022&startMonth=01&endMonth=12&sesnCd=0&txtStnNm=%EC%A0%84%EC%A3%BC&stnId=146&areaId=&gFontSize="

    filename ="/.weather_temp.csv"

    if not os.path.exists(filename)
        with open(filename, "w", encoding="UTF-8-sig", newline="") as f:
            res = requests.get(URL)
            f.write(res..text)
    with open(filename, "r", encoding="UTF-8") as f:
        lines = f.readline()

    data = list(line[8:])

    tmax = [x.split(",")[4] for x in data[:-1]]
    tmin = [x.split(",")[3] for x in data[:-1]]
    date = [x.split(",")[0] for x in data[1:]]

    blank = [1.strip() for i in tmax]

    x_b = [float(x) for x in blank if x]
    y_b = [float(y) for y in tmax if y]

    xb = max(x_b)
    yb = min(y_b)

    xd = date[x_b.index(xb)]
    yd = date[y_b.index(yb)]
    print("이재인", xd, xb, yd, yb)

    hw11_submission.submit("이재인", hot_date= xd, tmax=xb, cold_date=yd, tmin=yb)


if __name__ == "__main__":
    main()

