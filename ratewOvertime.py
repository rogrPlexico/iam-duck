hrs = input("Enter Hours:")
rate = input("Enter Rate:")

if float(hrs) <=40 :
    print(float(hrs)*float(rate))
elif float(hrs) >40 :
    print((40*float(rate))+(((float(hrs)-40)*float(rate)*1.5)))
