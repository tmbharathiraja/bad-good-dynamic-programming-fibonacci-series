# Bad Vs Good Vs Dynamic Fibonacci Sequence recursive functions
In this I go through the three ways of writing Fibonacci series generator. Then I provide the time complexity measure using timeit module and I provide the recursion visualization using functools wraps.
Language: Python 3.6
Fibonacci numbers: The Fibonacci series numbers start with 0, 1 and every next number is sum of previous two numbers in the series.
	0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144…
	Mathematically
		Fn = Fn-1 + Fn-2 and F0 = 0, F1 = 1
1. General Recursive method, this method has O (2n) time complexity with duplicate calculations.
2. Good Fibonacci series generator, this method has O (n) time complexity using tuple to avoid duplicate calculations.
3. Dynamic Programming method, this method has O (n) time complexity with O (n) space complexity using dictionary to avoid duplicate calculations.
4. Finally I print the trace for each of these methods for given n to visualize the recursion.
