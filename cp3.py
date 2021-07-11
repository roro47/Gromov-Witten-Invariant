from sympy import *

# N_{d, k} is the number of rational degree d curves in CP3 through k generic points and
# 4d - 2k generic lines
def cp3_recursion(d, k):
    if d == 1 and k == 2:
        return 1

    if d == 1 and k == 1:
        return 1

    if d == 1 and k == 0:
        return 2

    acc = 0
    if 0 <= k and k <= 2*d - 3/2:
        acc = 0
        for d0 in range(1, d+1):
            d1 = d - d0
            for k0 in range(1, k+1):
                k1 = k - k0
                acc += binomial(k, k0) \
                    * (Pow(d0, 3)*binomial(4*d - 2*k - 3, 4*d0 - 2*k0) \
                        - Pow(d0, 2)*d1*binomial(4*d - 2*k - 3, 4*d0 - 2*k0 - 1)) \
                    * cp3_recursion(d0, k0) * cp3_recursion(d1, k1)

        acc += cp3_recursion(d, k)
        acc = acc/d

    elif 1 <= k and k <= 2*d - 1:
        print("this case")
        k = k - 1
        for d0 in range(1, d+1):
            d1 = d - d0
            for k0 in range(1, k+1):
                k1 = k - k0
                acc += binomial(4*d - 2*k - 2, 4*d0 - 2*k0) \
                    * (Pow(d0, 3) * binomial(k - 1, k0) - Pow(d0, 2) *d1*binomial(k - 1, k1)) \
                    * cp3_recursion(d0, k0) * cp3_recursion(d1, k1)

        acc += cp3_recursion(d, k)
        acc = acc/d

        
    elif 1 <= k and k <= 2*d - 3/2:
        k = k - 1
        for d0 in range(1, d+1):
            d1 = d - d0
            for k0 in range(1, k+1):
                k1 = k - k0
                acc += binomial(k-1, k0) \
                        * (d1*d1*binomial(4*d - 2*k -3, 4*d1 - 2*k1) \
                            - d0*d0*binomial(4*d - 2*k -3, 4*d0- 2*k0 - 1)) \
                        * cp3_recursion(d0, k0) * cp3_recursion(d1, k1)
                                
                
                
    else:
        return 0


print(cp3_recursion(2, 3))

"""
class TestCP3Recursion(unittest.TestCase):

    def test_N_1_1(self):
        self.assertEqual(cp3_recursion(1, 1), 1, "Should be 1")

    def test_N_1_0(self):
        self.assertEqual(cp3_recursion(1, 0), 2, "Should be 2")

    def test_N_1_2(self):
        self.assertEqual(cp3_recursion(1, 2), 1, "Should be 1")

    def test_N_2_4(self):
        self.assertEqual(cp3_recursion(2, 4), 0, "Should be 0")

    def test_N_2_3(self):
        self.assertEqual(cp3_recursion(2, 3), 1, "Should be 1")

    def test_N_2_2(self):
        self.assertEqual(cp3_recursion(2, 2), 4, "Should be 4")

    def test_N_2_1(self):
        self.assertEqual(cp3_recursion(2, 1), 18, "Should be 18")

    def test_N_2_0(self):
        self.assertEqual(cp3_recursion(2, 0), 92, "Should be 92")

    def test_N_3_6(self):
        self.assertEqual(cp3_recursion(3, 6), 1, "Should be 1")

    def test_N_3_5(self):
        self.assertEqual(cp3_recursion(3, 5), 5, "Should be 5")
    
    def test_N_3_4(self):
        self.assertEqual(cp3_recursion(3, 4), 30, "Should be 30")

    def test_N_3_3(self):
        self.assertEqual(cp3_recursion(3, 3), 190, "Should be 190")

 
"""