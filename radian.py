def radian(angle):
    pie = 3.1415926535897932384
    fradian = 180/pie

    nradian = angle/fradian

    return nradian

angle = float(input("0~360 사이에 숫자를 입력하시오"))

print(radian(angle),"라디안")
