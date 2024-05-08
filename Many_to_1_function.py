# t1 and t2 are whole numbers
t1 = 3
t2 = 2
max = t1*t2 - 1

print("p_max =", t1)
print("q_max =", t2)
print("\n\n")

print("last number to appear in the program:")
print(max, "\n\n")

# function from 2 numbers to 1 number
for p in range(t1):
	for q in range(t2):
		print("if p = ", p, " and q = ", q, " then:", sep="")
		x = (p+1)*t2 - (t2 - (q+1)) -1
		print("x =", x)

print("\n\n\n")
# functions from 1 number to 2 numbers
for r in range(max +1):
	rem = (r+1) % t2
	if (rem == 0):
		p = (r+1 -rem)/t2 -1
		q = t2 -1
	else:
		p = (r+1 -rem)/t2
		q = rem -1
	print("if x =", r, "then:")
	print("p =", int(p))
	print("q =", q)
	

