def check_triangle(side_a, side_b, side_c) -> bool:

    if side_a >= side_b + side_c or side_b >= side_a + side_c or side_c >= side_a + side_b:
        return False
    else:
        return True


if __name__ == "__main__":
    side_a = int(input('side_a: '))
    side_b = int(input('side_b: '))
    side_c = int(input('side_c: '))

    if check_triangle(side_a, side_b, side_c):
        print('possible')
    else:
        print('impossible')
