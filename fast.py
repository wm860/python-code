import numpy as np
#from numpy.fft import fft

if __name__ == "__main__":
    x = [0, 1, 2, 3]
    #y = fft(x)
    y=np.fft.fft(x)
    print(y)
