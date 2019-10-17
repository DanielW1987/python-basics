mathsPoints: int = int(input("Enter the math points: "))
physicsPoints: int = int(input("Enter the physics points: "))
chemistryPoints: int = int(input("Enter the chemistry points: "))

if mathsPoints >= 35 and physicsPoints >= 35 and chemistryPoints >= 35:
    averageGrade: float = (mathsPoints + physicsPoints + chemistryPoints) / 3

    finalGrade: str = ""
    if averageGrade <= 59:
        finalGrade = "C"
    elif averageGrade <= 69:
        finalGrade = "B"
    else:
        finalGrade = "A"

    print("The final grade is '{}'".format(finalGrade))
else:
    print("I'm afraid you failed.")
