score=input('Enter Score')
score=float(score)

if score <0.0 or score>1.0 :
    print('Scores should fall between 0 and 1.0')
else :
    if score >=.9 :
        print('Grade:', "A")
    elif score <.9 and score >=.8 :
        print('Grade:', "B")
    elif score <.8 and score >=.7 :
        print('Grade:', "C")
    elif score <.7 and score >=.6 :
        print('Grade:', "D")
    elif score <.6 :
        print('Grade:', "F")
