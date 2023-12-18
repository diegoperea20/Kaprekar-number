def solve(number: int) -> bool:
    #ecuation of square kaprekar number
    square = str(number**2)
    length = len(str(square))

    #verify if the number is kaprekar
    for i in range(1,length):
        left_p = int(square[:i])
        right_p = int(square[i:])
        if left_p + right_p == number and right_p != 0:
            return True
        
    return False

#test cases
#print(solve(22222))  #True
#print(solve(75))      #False
#print(solve(99))      #True
