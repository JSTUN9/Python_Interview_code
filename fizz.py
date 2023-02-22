n = 10
fizz = 2
buzz = 5
for i in range (n):
	if (i%2==0):
		print("Fizz")
	elif(i%5==0):
		print("buzz")
	elif(i%2==0 and i%5==0):
		print("Fizzbuzz")
	else:
		print(i)