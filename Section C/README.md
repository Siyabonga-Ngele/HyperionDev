# Instructions to build and run the solution:

1. Save the code above in a file with a .py extension (e.g. isbn13.py)
2. Open a terminal or command prompt window
3. Navigate to the directory where you saved the file (e.g. cd path/to/directory)
4. Run the code by entering python isbn13.py in the terminal or command prompt window

# Worst-case space complexity

The worst-case space complexity of this solution is O(n), where n is the length of the ISBN number (either 10 or 13). 
This is because the solution uses a single loop to sum up the products, and the size of the sum grows linearly with the length of the ISBN number.
This is assuming that the ISBN number contains digits 0 - 9 and an 'X'
