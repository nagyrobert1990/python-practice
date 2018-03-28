number1 = input("Enter the 1st number: ")
number2 = input("Enter the 2nd number: ")
number3 = input("Enter the 3rd number: ")
number4 = input("Enter the 4th number: ")
number5 = input("Enter the 5th number: ")
number6 = input("Enter the 6th number: ")
number7 = input("Enter the 7th number: ")
number8 = input("Enter the 8th number: ")
number9 = input("Enter the 9th number: ")
numbers = [number1, number2, number3, number4, number5, number6, number7, number8, number9]
N = 9
print(numbers)
iterations = 1
while (iterations < N):
    j=0
    while (j <= N-2):
        if (numbers[j]>numbers[j+1]):
            temp = numbers[j+1]
            numbers[j+1]=numbers[j]
            numbers[j]=temp
            j=j+1
        else:
            j=j+1
    iterations = iterations + 1
print(numbers)