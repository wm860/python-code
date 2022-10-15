from collections import Counter
from string import punctuation



class FileFreqCounter:

    def __init__(self, path):
        self.path = path
        self.counter = Counter()
        self.symbols = set(punctuation)

    def read(self):
        with open(self.path, "r") as f:
            return [line.replace("\n", "") for line in f]

    def remove_punctuation(self, sentence):
        for ch in sentence:
            if ch in punctuation:
                sentence = sentence.replace(ch, " ")

    def remove_punctuation2(self, sentence):

        for ch in sentence:
            if ch in symbols:
                sentence = sentence.replace(ch, " ")
    def calc_freq(sentence):
        return Counter(sentence.lower().split())

    def calc_freq2(self):
        sentences = self.read_lines()
        for sentence in sentences:
            cleaned = self.remove_punctuation(sentence)
            self.counter = Counter(cleaned.lower().split())
        return self.counter

    def calc_freq3(self, sentence):
        cleaned = self, remove_punctuation(sentence)
        return Counter(cleaned.lower().split())

    def most_common(self, n=3):
        self.cal_freq2()
        return self.counter.most_common(n)

if __name__ == "__main__":
# print(calc_freq("This is a simple text this"))
    file_counter = FileFreqCounter
    print(file_counter.most_common(3))
