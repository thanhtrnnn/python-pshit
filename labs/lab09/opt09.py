"""
Optional exercises on 2d lists.

To cut down on the number of files, this module is its own test script.  The test
cases are at the bottom of the file.  Run the file as a script to test your implementations.

THANH TRAN
APRIL 16TH, 2025
"""
import introcs


# DEFINE THESE FUNCTIONS
def replace_table(table,a,b):
    """
    Returns: A copy of table with all instance of a replaced by b
    
    Example: replace_table([[1,2],[3,1]], 1, 4) returns [[4,2],[3,4]
    
    Parameter table: The table to copy
    Precondition: table is a rectangular 2d list of numbers
    
    Parameter a: The number to remove
    Precondition: a is a number
    
    Parameter b: The number to replace with
    Precondition: b is a number
    """
    # Create a new table with the same dimensions as the original
    new_table = [[0 for _ in range(len(table[0]))] for _ in range(len(table))]
    
    # Iterate through each element in the original table
    for i in range(len(table)):
        for j in range(len(table[i])):
            # If the element is equal to a, replace it with b
            if table[i][j] == a:
                new_table[i][j] = b
            else:
                new_table[i][j] = table[i][j]
    
    return new_table


def table_pair(table):
    """
    Returns: True if the table has an adjacent pair horizontally or vertically.
    
    Examples:
        table_pair([[1,1], [2,3]]) is True (horizontal pair of 1) 
        table_pair([[2,3], [4,3]]) is True (vertical pair of 3).  
        table_pair([[1,2], [3,4]]) is False.
        table_pair([[1,2,1], [3,4,2], [1,3,1]]) is False (nothing adjacent).
    
    Parameter table: The table to check
    Precondition: table is a rectangular 2d list of numbers
    """
    # Iterate through each element in the table
    for i in range(len(table)):
        for j in range(len(table[i])):
            # Check right neighbor
            if j < len(table[i]) - 1 and table[i][j] == table[i][j + 1]:
                return True
            # Check bottom neighbor
            if i < len(table) - 1 and table[i][j] == table[i + 1][j]:
                return True

    return False


# TEST CASES
def test_replace_table():
    """
    Test the function replace_table
    """
    introcs.assert_equals([[2,0,2],[0,2,0]],replace_table([[1,0,1], [0,1,0]],1,2))
    introcs.assert_equals([[1,3,1],[3,1,3]],replace_table([[1,0,1], [0,1,0]],0,3))
    introcs.assert_equals([[1,0,1],[0,1,0]],replace_table([[1,0,1], [0,1,0]],4,5))
    introcs.assert_equals([[1, 2, 3], [4, 5, 6], [7, 8, 10]],
                          replace_table([[1, 2, 3], [4, 5, 6], [7, 8, 9]],9,10))
    introcs.assert_equals([[-1, 0, 4], [0, 3, 2], [4, 4, 0]],
                          replace_table([[-1, 0, 1], [0, 3, 2], [1, 1, 0]], 1, 4))


def test_table_pair():
    """
    Test the function table_pair
    """
    introcs.assert_equals(False,table_pair([[1,2,1], [3,4,2], [1,3,1]]))
    introcs.assert_equals(False,table_pair([[1, 0, 1], [0, 1, 0]]))
    introcs.assert_equals(False,table_pair([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    introcs.assert_equals(True,table_pair([[-1, 0, 1], [0, 3, 2], [1, 1, 0]]))
    introcs.assert_equals(True,table_pair([[0, 0], [1, 2]]))
    introcs.assert_equals(True,table_pair([[1, 0], [1, 2]]))
    introcs.assert_equals(True,table_pair([[0, 1], [3, 4], [3, 5], [6, 7]]))


if __name__ == '__main__':
    test_replace_table()
    test_table_pair()
    print('Module opt.py is working correctly')