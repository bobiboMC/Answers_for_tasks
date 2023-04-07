def count_max(max_num=None, count=0):
    try:
        new_num = int(input())  # read the next number from the stream
    except ValueError:
        # Invalid input, need to enter again a number
        print("Invalid input, need to input an integer!")
        return count_max(max_num, count)
    
    if new_num == 0:  # base case: end of stream
        return (max_num, count)
    elif max_num is None or new_num > max_num:  # update max_num and count for new max number value
        return count_max(new_num, 1)
    elif new_num == max_num:  # max value is showing once again, so increment count of this number
        return count_max(max_num, count + 1)
    else:  # new inputed number is less than max value, so nothing changes
        return count_max(max_num, count)

if __name__ == "__main__":
    #TEST of count_max(max_num,count) function
	max_num, count = count_max() 
	print(f"(max num; count) ({max_num}; {count})")