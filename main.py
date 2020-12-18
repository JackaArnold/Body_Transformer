def calorie_cal(age,gender,weight,height):
    if gender == "male":
        BMR = 66.47 + (13.75 * weight) + (5.0 * height) - (6.75 * age)
        weight_in_cals = weight * 7000
        return BMR


def welcome():
    print('Hello Master, Jacka')
    print('You know the drill!')
    a = float(input('Age:'))
    g = input('Gender:')
    w = float(input('Weight:'))
    h = float(input('Height:'))
    cal_goal = int(calorie_cal(a,g,w,h)-1000)
    current_cal = 0
    print(f'in theory you my friend are burning {calorie_cal(a,g,w,h)} just by existing')
    print('And with that in mind i know you and you want to lose some weight (now you are trying for real xd)')
    print(f'sooooooo.... that means i allow you (yes i have power over you hehe): {calorie_cal(a,g,w,h)-1000} yeesssh kinda harsh')
    while cal_goal >= current_cal:
        item = int(input('Cal of food you had:'))
        current_cal = current_cal + item
        cal_goal = cal_goal - item
        print(f'Cal goal is now: {cal_goal}')
welcome()

