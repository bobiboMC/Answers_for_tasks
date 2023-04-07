
#calculate sum of digits of a number
def sum_of_digits(num):
	#base of recursion
    if num == 0:
        return 0
    else:
        return num % 10 + sum_of_digits(num // 10)
		
if __name__ == "__main__":
    print(sum_of_digits(2347623)) #27
    print(sum_of_digits(573241)) #22