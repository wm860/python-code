def calculate_bmi (weight, height):
    bmi = weight/height ** 2
    if bmi < 18.5:
        return "underweight"
    elif bmi > 20:
        return "overweight"
    return "normal"

if __name__ == "__main__":
    height = float(input("weight: "))
    weight = float(input("height: "))

    result = calculate_bmi(weight, height)
    print("Your status: " + result)
    print(f"Your status z fstringa: {result}")
