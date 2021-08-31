"""
In computer science, regular numbers are often called Hamming numbers, after Richard Hamming, 
who proposed the problem of finding computer algorithms for generating these numbers in ascending order.

In number theory, these numbers are called 5-smooth, 
because they can be characterized as having only 2, 3, or 5 as prime factors. 
"""

class Hamming:
    __doc__ = __doc__

    @staticmethod
    def get_nth(n):
        """
        :param n:   int     nth position
        :return:    int     nth Hamming Nummber
        """
        if n <= 0: raise ValueError("n should be more than 0 (positive integer)")

        table = [1] * n
        i, j, k = 0, 0, 0
        ri, rj, rk = 2, 3, 5
        
        for ref in range(1, n):
            table[ref] = min(ri, min(rj, rk))
            if table[ref] == ri:
                i += 1
                ri = 2 * table[i]
            if table[ref] == rj:
                j+= 1
                rj = 3 * table[j]
            if table[ref] == rk:
                k += 1
                rk = 5 * table[k]
        return table[-1]
    
    @staticmethod
    def is_hamming_number(n):
        """
        :param n:   int     positive integer to test
        :return:    bool    the number is hamming number or not
        """
        if n <= 0: raise ValueError("n should be more than 0 (positive integer)")

        ref = n
        while ref>1:
            if   ref%2==0:  ref//=2
            elif ref%3==0:  ref//=3
            elif ref%5==0:  ref//=5
            else: return False
        return True


if __name__ == "__main__":
    print("Testing for " + __file__)

    ###############################################################################

    RES = (
        -1, 1, 2, 3, 4, 5, 6, 8, 9, 10, 
        12, 15, 16, 18, 20, 24, 25, 27, 
        30, 32, 36, 40, 45, 48, 50, 54
    )

    ###############################################################################

    print("\nTesting get_nth: ")

    for n in range(1, len(RES)):
        check = Hamming.get_nth(n)
        if n%5==1: print("\n\t", end='')
        print(check,  "==", RES[n], check==RES[n], end = " : ")
    print()

    ###############################################################################

    print("\nTesting is_hamming_number:\n")

    #############

    print("\tShould Return True")

    for n in range(1, len(RES)):
        if Hamming.is_hamming_number(RES[n]):
            print("\t\t==>", True)
            break
    else:
        print("\t\t==>", False)

    #############

    print("\tShould Return False")

    for n in range(11, 20):
        if n not in RES:
            if Hamming.is_hamming_number(n):
                print("\t\t==>", True)
                break
    else:
        print("\t\t==>", False)

    #############

    print("\tShould Return True")

    for i in range(20, 50):
        if Hamming.is_hamming_number(Hamming.get_nth(n)): 
            print("\t\t==>", True)
            break
    else:
        print("\t\t==>", False)

    ###############################################################################
