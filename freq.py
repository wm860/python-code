from collections import defaultdict

def calc_freq(sentence):
    freq = defaultdict(int)
    for word in sentence.lower().split():
        freq[word] += 1
    return freq
if __name__ == "__main__":
    print(calc_freq("This is a simple text this"))
