string = input("Enter a string: ")
n = len(string)
reverse = ""
for i in range(n - 1, -1, -1):
    reverse = reverse + string[i]
print("Reversed string:", reverse)
# Time Complexity: O(n)
# Space Complexity: O(n)
