#1 решение
"""
def main(x: int) -> str:
    t6 = (x >> 29) & 0x1FF
    t5 = (x >> 26) & 0x7
    t4 = (x >> 25) & 0x1
    t3 = 0
    t2 = (x >> 9) & 0x7F
    t1 = x & 0x1FF

    result = (
        ((t4 << 36) |
         (t6 << 28) |
         (t3 << 19) |
         (t1 << 10) |
         (t2 << 3) |
         t5)
    )
    return f'0x{result:x}'

if __name__ == "__main__":
    print(main(82212717073))
    print(main(75108933842))
    print(main(35757636677))
    print(main(75851221697))
    """
#2 решение
