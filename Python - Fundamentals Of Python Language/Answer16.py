User_Sentence = input("Enter Your Sentence: ")

Words = User_Sentence.split()

Word_Count = {}
for Word in Words:
    Word = Word.lower()
    Word_Count[Word] = Word_Count.get(Word, 0) + 1

for Word, count in Word_Count.items():
    print(f"{Word}: {count}")

# Help From Google