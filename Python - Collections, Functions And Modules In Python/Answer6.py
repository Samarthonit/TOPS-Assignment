list_words = ["212", "aa", "zz", "abcd", "good"]

count = 0

for word in list_words:
    if len(word) >= 2 and word[0] == word[-1]:
        count += 1
    
print(count, "strings")