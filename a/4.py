class Analizator:
    def __init__(self, string):
        self.file_object = string
        self.line = self.file_object.read()

    sentence_symbols = ['.', '!', '?']
    word_symbols = sentence_symbols + [' ', ':', '-', '"']
    words = 0
    sentences = 0
    characters = 0

    def count(self):
        for i in self.line:
            if i in self.word_symbols:
                self.words = self.words + 1
                print(self.words)
                if i in self.sentence_symbols:
                    self.sentences = self.sentences + 1
                    print(self.sentences)
            self.characters = self.charecters + 1

    def add_smt(self, sentence):
        self.file_object.write(sentence)


with open('textfile.txt', 'r+') as file_object:
    a = Analizator(file_object)
    print(a.line)
    print(a.sentences)
    print(a.words)
    print(a.characters)
    a.add_smt('Hello.')
