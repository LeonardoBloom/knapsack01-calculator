class Knapsacker:

    def __init__(self):
        self.x = "hi"

    # initializes values for knapsack table
    def knapsack_initializer(self, k_tbl):
        for column in range(len(k_tbl[0])):
            k_tbl[0][column] = 0
        for row in range(len(k_tbl)):
            k_tbl[row][0] = 0
        return k_tbl

    #knapsackie filler
    def knapsack(self, array, values, weights, item_weights):
        array = self.knapsack_initializer(array)

        for rows in range(1, len(array)):
            for columns in range(1, len(array[0])):
                b1 = array[rows][columns-1]
                #thing2 = array[array[rows] - array[columns]][columns-1] + values[columns]
                if weights[rows] >= item_weights[columns]:
                    b2 = weights[rows] - item_weights[columns]
                    for element in range(len(weights)):
                        if b2 == weights[element]:
                            b2 = element
                            break
                    array[rows][columns] = max( b1 , array[ b2 ][ columns-1 ] + values[columns])
                else:
                    array[rows][columns] = array[rows][columns-1]
        return array

