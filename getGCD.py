class FinderGCD:

    def __init__(self):
        self.initialized = True

    # calculates the GCD between two numbers
    def the_gcd(self, x, y):
        while(y):
            x, y = y, x % y
        return x

    # calculates the GCD of an entire array of numbers
    def find_gcd(self, array):
        gcd = self.the_gcd(array[0], array[1])
        for x in range(2, len(array)):
            gcd = self.the_gcd(gcd,array[x])
        return gcd