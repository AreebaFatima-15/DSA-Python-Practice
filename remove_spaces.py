string = input("Enter a string: ")
new_string = ""
for i in string:
    if i != " ":
        new_string = new_string + i
print("String without spaces:", new_string)
# Time Complexity: O(n)
# Space Complexity: O(n)
