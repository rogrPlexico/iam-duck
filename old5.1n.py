
def looped(entry):
    x=0
    float(entry)
    x = entry+looped
    return x



goanenter = input('enter number\n')
        # tries to turn user input into float
        # if successful, uses user input as input into the looped() function
while goanenter!='done':
    try:
        float(goanenter)
    except:
        print("please enter a number\n")

    prant = looped(goanenter)

print(prant)
