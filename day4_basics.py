def check_number(n):
    if n>0:
        return "positive"
    elif n<0:
        return "negative"
    else:
        return "zero"
for i in [-4,5,0]:
    print(i,check_number(i))    
