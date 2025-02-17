import math

#1 варик
def main(y):
    if y < 46:
        return 66 * (y ** 2) + (6 * y) + ((y ** 5) / 59)
    elif 46 <= y < 101:
        return (math.ceil(86 * (y ** 2)) ** 7) + 55 * (y ** 3)
    elif 101 <= y < 189:
        return (math.tan((y**3)+1))**4 + (y**0.5/56) + 0.01
    elif y >= 189:
        return ((y ** 2) + 13 + (y ** 3)) ** 5 + ((y ** 4) / 20)




if __name__ == "__main__":
    print(main(-25))
    print(main(2))
    print(main(136))
    print(main(61))
    print(main(209))
