string = input("Enter a string: ")
n = len(string)
reverse = ""
for i in range(n - 1, -1, -1):
    reverse = reverse + string[i]
if reverse == string:
    print("Palindrome")
else:
    print("Not a palindrome")
# Time Complexity: O(n)
# Space Complexity: O(n)
