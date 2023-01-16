

numbers = (1,2,3)
letters = ("a", "b", "c")

print(numbers[0])
print(letters[-1])

result = numbers + letters

print(len(result))

if 4 in numbers:
    print("the number 4 is in the Tuple")
else:
    print("the number 4 is NOT in the Tuple")

numberslist = [4,5,6]
tupleList = tuple(numberslist)
print(tupleList)

firstNumber, secondNumber, thirdnumber = tupleList
print(firstNumber, secondNumber, thirdnumber)