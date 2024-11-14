class StringReverser:
    def reverse_words(self, s):
        words = s.split()
        reversed_words = ' '.join(reversed(words))
        return reversed_words
reverser = StringReverser()
print(reverser.reverse_words("Hello World"))