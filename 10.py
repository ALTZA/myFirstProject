def ExOh(str):
    x = 0
    o = 0
    for i in str:
        if i == "x":
            x += 1
        elif i == "o":
            o += 1
    return x == o



print (ExOh(input()))