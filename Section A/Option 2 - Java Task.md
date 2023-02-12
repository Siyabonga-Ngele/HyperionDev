# Option 2: Java Task

## Corrections to be made in the code
 

- errors in the reverse_string method
	
		line 26: the function call reverseString(myStr.substring(1)) differs from the function definition in line 18 reverse_string(String myStr) this will result
		in a compilation error. 

		Solution: 
		//change line 26 to 
		return reverse_string(myStr.substring(1)) + myStr.charAt(0);
		
- errors in the function method

		line 28: the variable name maxNumber is already defined in the generic method "function" as a generic parameter,therefore a change is needed as it will cause a compile 
		error.
		 
		Solution:
		//change function defintion in line 28 to a non-generic and declare the parameter as an integer 
		public static void function(int maxNumber)

		//in Line 30 you can now remove the entire line as it will already be declared and intialized when the method is called
		
- errors in the main method
	
		line 11: the prinln statement contains some hard code as the method named function is not used to produce the output.

		Solution:
		//Instead you can look to change line 11 to 
		System.out.println("The reversed string is: " + reversed);

		//add a new line after line 11 which will make use of the method named "function"
		function(10);


 ## This is the complete solution for the task


	public class recursion
	{
			public static void main(String[] args) {
	 
			// Saves the string that would be reversed
			String myStr = "emosewA si avaJ";
	 
	 
			//create Method and pass and input parameter string 
			String reversed = reverse_string(myStr);
			System.out.println("The reversed string is: " + reversed);
			function(10);
		}
	 
	 
		//Method take string parameter and check string is empty or not
		public static String reverse_string(String myStr)
		{
			if (myStr.isEmpty()){
			 System.out.println("String in now Empty");
			 return myStr;
			}
			//Calling Function Recursively
			System.out.println("String to be passed in Recursive Function: "+myStr.substring(1));
			return reverse_string(myStr.substring(1)) + myStr.charAt(0);
			}

		public static void function(int maxNumber) {
		
			int previousNumber = 0;
			int nextNumber = 1;
			 
					System.out.print("Fibonacci Series of "+maxNumber+" numbers:");
	 
				for (int i = 1; i <= maxNumber; ++i){
					System.out.print(previousNumber+" ");
					// On each iteration, we are assigning second number
					// to the first number and assigning the sum of last two
					// numbers to the second number
					int sum = previousNumber + nextNumber;
					previousNumber = nextNumber;
					nextNumber = sum;
				}
			}
	}

 ## Efficiency improvements that can be made on the code 
	
	- Your code is efficient and provides the correct output but it is not efficient when it comes to the Fibonnaci series calculation.
	
	- Here are some proposed changes:
	
		//Create a recursive function, fibonacci, 
		//that calculates each Fibonacci number by passing along the current previous and next numbers. This eliminates the need for the loop
     
			public static int fibonacci(int n, int previous, int next) {
				if (n == 0) 
					return previous;
				
				return fibonacci(n-1, next, previous + next);
			}
		
		//The new function method
			public static void function(int maxNumber) {
				System.out.print("Fibonacci Series of "+maxNumber+" numbers:");
				for (int i = 0; i < maxNumber; i++) {
					System.out.print(fibonacci(i, 0, 1) + " ");
				}
			}
		
		//End of solution
	
	- The use of the recursive fibonacci method eliminates the need for the loop, and results in an exponential improvement in efficiency for large values of maxNumber. 
	The for loop in the function method is still used to print the series, 
	but the calculation of each number is now done by the recursive function.

 ## Overall
 
 It looks like your on the right track with your implementation. Just consider following naming convetions consistently and use camelCase for function names, 
 example reverseString instead of reverse_string. Please add more comments and documentation to explain what your code is doing and optimize your code were 
 possible.
	





