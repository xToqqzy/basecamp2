human_years = int(input())

dog_years = 0
if human_years < 0:
    print("Only positive numbers are allow")

elif human_years <= 2:
    dog_years += human_years * 10.5


elif human_years > 2:
    dog_years += (human_years - 2) * 4 + 21

print(dog_years)
