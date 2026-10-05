string = input("Enter a string: ")
vowels = ["a", "e", "i", "o", "u"]
count = 0
for i in string:
    if i in vowels:
        count = count + 1
print("Number of vowels:", count)
# Time Complexity: O(n)
# Space Complexity: O(1)
