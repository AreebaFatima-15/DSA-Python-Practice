string = input("Enter a string: ")
frequency = {}
for i in string:
    if i in frequency:
        frequency[i] = frequency[i] + 1
    else:
        frequency[i] = 1
for i in frequency:
    print(i, "→", frequency[i])
# Time Complexity: O(n)
# Space Complexity: O(n)
