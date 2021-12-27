try:

    hrs = input("Enter Hours:")
    hrs = float(hrs)
    rate = input("Enter Rate:")
    rate = float(rate)

    if hrs >=40 :
        othrs = hrs - 40
        print((rate*40)+(othrs*rate*1.5))
    else :
        print(hrs*rate)

except: print('Make sure you have entered a numeric number.')
