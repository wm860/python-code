from math import sqrt

def solve_equation(a, b, c):
    if b*b - 4*a*c == 0:
        return -b/a
    else:
        return ((-b-(b*b -4*a*c)**0.5)/(2*a),(-b+(b*b -4*a*c)**0.5)/(2*a))
    #else :
    #    return None

if __name__ == "__main__":
    print(solve_equation(1,1,1))