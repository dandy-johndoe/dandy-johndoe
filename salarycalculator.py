def computepay():
    if h <= 40:
        gross = h * r
        print(gross)
    elif h > 40:
        gross = h * r
        extra = (h - 40) * (r * 0.5)
        gross1 = gross + extra
        return(gross1)

hrs = input("Enter Hours:")
rate = input("Enter rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("please enter a numeric value")


p=computepay()
print("Pay" , p)
