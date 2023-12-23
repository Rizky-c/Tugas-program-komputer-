input_sentence = input("Masukkan sebuah kalimat: ")
words = input_sentence.split()
for word in words:
    for letter in reversed(word):
        print(letter)
    print()