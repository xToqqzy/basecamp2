input = (
    input("Please enter the cost (format 'Cost of the meal: xy.wz")).split(":")

cost = float(input[1])


tip = cost * 0.15
tax = cost * 0.21

total = cost + tip + tax

print(f"Tax:{tax},Tip:{tip},Total:{total:.3f}")
