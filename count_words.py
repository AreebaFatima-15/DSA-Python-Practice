sentence = input("Enter a sentence: ")
count = 1
for i in sentence:
    if i == " ":
        count = count + 1
print("Number of words:", count)
# Time Complexity: O(n)
# Space Complexity: O(1)
