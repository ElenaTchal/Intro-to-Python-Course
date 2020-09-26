largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break

    try:
        num=int(num)

	if smallest is None:
		smallest = num
	elif smallest > num:
		smallest = num
	if largest is None:
		largest = num
	elif largest < num:
		largest = num

    except:
        print("Invalid input")
        continue
print("Maximum is", largest)
print("Minimum is", smallest)




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
