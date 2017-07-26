import csv
import string

# Open the CSV File and read it in.
f = open('countries.csv')
data = f.read()

# Split the data into an array of countries.
elementsList = data.split('\n')

# print length of the list
length = len(elementsList)



print(elementsList[len(elementsList)-1])

print(elementsList)


Country = input("Name your country.")
beginningIndex = 0
endingIndex = len(elementsList)-1

index = int((endingIndex+beginningIndex)/2)
while elementsList[index] != Country:
    print(index)
    if Country > elementsList[index]:
        beginningIndex = index
        index = int((endingIndex+beginningIndex)/2)

    elif Country < elementsList[index]:
        beginningIndex = beginningIndex
        endingIndex = index
        index = int((endingIndex+beginningIndex)/2)
    else:
        print(index)
        break
    print(index)


# Start your search algorithm here.
