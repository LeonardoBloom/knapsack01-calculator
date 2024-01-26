class Select:

    def __init__(self):
        self.initialized = True

    # calculates the selection items for optimal profit
    def k_selection(self, array):
        opt_row = len(array)-1
        opt_column = len(array[0])-1
        optimal = array[ opt_row ][ opt_column ]
        selection = []
        stop = False # flag to stop loop
        while stop == False:
            while opt_row >= 0 and opt_column >= 0:
                tracker = array[ opt_row ][ opt_column ] # tracker for 0 before entering the rest of operations
                if tracker == 0:
                    stop = True
                    break
                elif array[ opt_row ][ opt_column ] != array[ opt_row ][ opt_column-1 ]:
                    selection.insert(0, opt_column)
                    opt_row -= 1
                    opt_column -= 1
                elif array[ opt_row ][ opt_column ] == array[ opt_row ][ opt_column-1 ]:
                    opt_column -= 1

        print("The optimal profit is: ", optimal, "with selection: ", selection)