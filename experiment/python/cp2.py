from sympy import *
import unittest


# CP^2 recursion formula
def cp2_recursion(d):
    if d <= 0:
        return 0

    if d == 1:
        return 1 # N_d = 1

    acc = 0
    for k in range(1, d): # k from 1 to d - 1
        l = d - k
        acc += cp2_recursion(k)* cp2_recursion(l) * \
            (Pow(k, 2)*Pow(l,2)*binomial(3*d - 4, 3*k - 2) - \
                Pow(k, 3)*l*binomial(3*d - 4, 3*k - 1))
    return acc

print(cp2_recursion(4))



class TestCP2Recursion(unittest.TestCase):

    def test_N_1(self):
        self.assertEqual(cp2_recursion(1), 1, "Should be 1")

    def test_N_2(self):
        self.assertEqual(cp2_recursion(2), 1, "Should be 1")

    def test_N_3(self):
        self.assertEqual(cp2_recursion(3), 12, "Should be 12")

    def test_N_4(self):
        self.assertEqual(cp2_recursion(4), 620, "Should be 620")

    def test_N_5(self):
        self.assertEqual(cp2_recursion(5), 87304, "Should be 87,304")

    def test_N_6(self):
        self.assertEqual(cp2_recursion(6), 26312976, "Should be 26,312,976")

    def test_N_7(self):
        self.assertEqual(cp2_recursion(7), 14616808192, "Should be 14,616,808,192")
   

if __name__ == '__main__':
    unittest.main()