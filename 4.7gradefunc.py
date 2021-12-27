def compgrade(score):

    if score <0.0 or score>1.0 :
        print('Scores should fall between 0 and 1.0')
    else :
        if score >=.9 :
            grade="A"
        elif score <.9 and score >=.8 :
            grade="B"
        elif score <.8 and score >=.7 :
            grade="C"
        elif score <.7 and score >=.6 :
            grade="D"
        elif score <.6 :
            grade="F"

    return grade

scoretograde = input('enter somethin bitch\n')
scoretograde = float(scoretograde)

print(compgrade(scoretograde))
