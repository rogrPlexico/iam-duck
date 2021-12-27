def ot(hrs,rate):
    if hrs <=40 :
        pay=hrs*rate
    elif hrs > 40 :
        pay=((40*rate)+(hrs-40)*(rate*1.5))

    return pay


#run these after
    #   tot = ot(41,10)
    #   print(tot)
