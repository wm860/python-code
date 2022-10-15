def calc_freq(sentence):
    freq = {}
    for word in sentence.lower().split():
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq
if __name__ == "__main__":
    print(calc_freq("This is a simple text this"))
