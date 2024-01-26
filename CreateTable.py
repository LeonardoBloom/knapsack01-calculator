class CreateTable:

    def __init__(self):
        self.initialize = True

    # creates all the weight values for table
    def table(self, array_gcd, LIMIT):
        weights = [0]
        count = array_gcd
        while count <= LIMIT:
            weights.append(count)
            count += array_gcd

        print("WEIGHT ROWS:", weights, " ", len(weights), " rows")
        return weights

        
