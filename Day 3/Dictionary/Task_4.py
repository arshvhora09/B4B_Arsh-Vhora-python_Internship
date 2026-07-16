words = ["apple", "ant", "banana", "bat", "cat", "carrot"]

grouped = {}

for word in words:
    grouped.setdefault(word[0], []).append(word)

print(grouped)