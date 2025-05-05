# Demonstrate List Slicing
list=[1,2,3,4,5,6,7,8,9,10]
extract_five=list[0:5]
reverse_five=extract_five.copy()
reverse_five.reverse()

# printing the desired output
print("Original list:",list)
print("Extracted first five elements:",extract_five)
print("Reversed extracted elements: ",reverse_five)