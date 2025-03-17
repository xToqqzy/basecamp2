input = input("Sides: (input format a=5, b=6, c=5)").split(",")

side_a = int(input[0].split("=")[1])
side_b = int(input[1].split("=")[1])
side_c = int(input[2].split("=")[1])


if side_a == side_b and side_c == side_c:
    print("equilateral triangle")
elif side_a == side_b or side_b == side_c or side_a == side_c:
    print("isosceles tirangle")
else:
    print("scalene triangle")
