def transcode(input_number):
    output = 0
    # Extract and shift T6 (bit 29 -> 35)
    t6 = (input_number >> 29) & 1
    output |= t6 << 35
    # Extract and shift T5 (bit 28 -> 2)
    t5 = (input_number >> 28) & 1
    output |= t5 << 2
    # Extract and shift T4 (bit 26 -> 36)
    t4 = (input_number >> 26) & 1
    output |= t4 << 36
    # Extract and shift T2 (bit 16 -> 3)
    t2 = (input_number >> 16) & 1
    output |= t2 << 3
    # Extract and shift T1 (bit 0 -> 10)
    t1 = (input_number >> 0) & 1
    output |= t1 << 10
    # Extract and shift T3 (bit 15 -> 9)
    t3 = (input_number >> 15) & 1
    output |= t3 << 9
    return output


def main(input_number):
    result = transcode(input_number)
    return f"0x{result:X}"


if __name__ == "__main__":
    # Тесты
    print(main(82212717073))  # Ожидаемый вывод: '0x990004609'
    print(main(75108933842))  # Ожидаемый вывод: '0x8b0034987'
    print(main(35757636677))  # Ожидаемый вывод: '0x14200114f4'
    print(main(75851221697))  # Ожидаемый вывод: '0x8d003072a'