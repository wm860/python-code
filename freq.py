from collections import defaultdict

def calc_freq(sentence):
    return Counter(sentence.lower().split())
if __name__ == "__main__":
    print(calc_freq("This is a simple text this"))
