firstnumber = int(raw_input("first number"))
secondnumber = int(raw_input("second number"))
thirdnumber = int(raw_input("third number"))

if(firstnumber + secondnumber == thirdnumber):
	print("true")
elif(secondnumber + thirdnumber == firstnumber):
	print("true")
elif(thirdnumber + firstnumber == secondnumber):
	print("true")