string = input("Enter the string: ")
substr = input("Enter the search string: ")
print("Occurances: ", string.count(substr), "\nPositions: ", ", ".join([str(i+1) for i in range(len(string)) if substr in string[i:i+len(substr)]]))