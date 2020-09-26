def computepay(h,r):
    return total

h = input("Enter Hours:")
h = float(h)
r = input("Enter Rate:")
r = float(r)
if h>40:
    reg = 40*r
    otp = (h-40)*((r*1.5))
    total = reg+otp
else:
    total = (r*h)

p = computepay(h,r)
print("Pay",p)




# hrs = input("Enter Hours:")
# h = float(hrs)
# rate = input("Enter Rate:")
# r = float(rate)
# if h>40:
    #reg = 40*r
    #otp = (h-40)*((r*1.5))
    #total = reg+otp
    #print(total)
#else:
   # print(r*h)
