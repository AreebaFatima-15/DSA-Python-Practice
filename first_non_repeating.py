string = input("Enter a string: ")
frequency = {}
for i in string:
    if i in frequency:
        frequency[i] = frequency[i] + 1
    else:
        frequency[i] = 1
for i in string:
    if frequency[i] == 1:
        print("First non-repeating character:", i)
        break
else:
    print("No non-repeating character found")
# Time Complexity: O(n)
# Space Complexity: O(n)
