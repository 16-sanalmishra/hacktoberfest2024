// Java program for the above approach
import java.util.*;

class GFG{

// Function to check if the number N
// is a heptadecagonal number
static boolean isheptadecagonal(int N)
{
	float n = (float) ((13 + Math.sqrt(120 * N + 
									169)) / 30);

	// Condition to check if number N
	// is a heptadecagonal number
	return (n - (int)n) == 0;
}

// Driver Code
public static void main(String[] args)
{
	
	// Given Number
	int N = 17;

	// Function call
	if (isheptadecagonal(N))
	{
		System.out.print("Yes");
	}
	else
	{
		System.out.print("No");
	}
}
}

// This code is contributed by Amit Katiyar
