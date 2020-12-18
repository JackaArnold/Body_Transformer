def calorie_cal(age,gender,weight,height):
    if gender == "male":
        BMR = 66.47 + (13.75 * weight) + (5.0 * height) - (6.75 * age)
        return BMR

print(calorie_cal(19,'male',94,183))