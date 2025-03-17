def calculate_fare(distance):
    distance_in_meters = distance * 1000
    rounded_distance = ((distance_in_meters + 139) // 140) * 140

    base_fare = 4.00
    fare_per_140 = (rounded_distance / 140) * 0.25
    total_fare = base_fare + fare_per_140
    return total_fare


if __name__ == "__main__":
    distance = float(input("Distance traveled (in kilometers):"))
    print(f"Total fare:{calculate_fare(distance)} EUR")
()
# met behulp van chatgtp ik kwam niet uit op de berekening en de rounding
