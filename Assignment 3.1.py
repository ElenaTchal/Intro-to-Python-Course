hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
if h>40:
    reg = 40*r
    otp = (h-40)*((r*1.5))
    total = reg+otp
    print(total)
else:
    print(r*h)
