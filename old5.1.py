def looped(entry):
    x = 0
    while entry!='done':
        if type(entry) != float or int:
            print("please enter a number\n")
        elif entry == 'done':
            print(x)
        else: x = entry+x
        return x

looped(input('enter Number\n'))
