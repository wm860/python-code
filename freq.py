from collections import Counter

def calc_freq(sentence):
    return Counter(sentence.lower().split())
if __name__ == "__main__":
    print(calc_freq("This is a simple text this"))
