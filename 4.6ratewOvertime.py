def computepay(hrs,rate):
    if hrs <=40 :
        tot=hrs*rate
    elif hrs >40 :
        tot=(40*rate)+((hrs-40)*(rate*1.5))
    return tot

totpay = computepay(45,10)

print(totpay)
