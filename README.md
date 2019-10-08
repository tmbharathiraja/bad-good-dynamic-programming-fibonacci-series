# Bad Vs Good Vs Dynamic Fibonacci Sequence recursive functions
In this I go through the three ways of writing Fibonacci series generator. Then I provide the time complexity measure using timeit module and I provide the recursion visualization using functools wraps.
Language: Python 3.6
Fibonacci numbers: The Fibonacci series numbers start with 0, 1 and every next number is sum of previous two numbers in the series.
	
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144…
	
Mathematically

F<sub>n</sub> = F<sub>n-1</sub> + F<sub>n-2</sub> and F<sub>0</sub> = 0, F<sub>1</sub> = 1

1. Bad Fibonacci method is a general recursive method with duplicate calculations, this method has O(2<sup>n</sup>) time complexity and O(1) sapce complexity.
3. Dynamic Programming method uses dictionary to avoid duplicate calculations, this method has O(n) time complexity and O(n) space complexity 
3. Good Fibonacci method uses tuple to avoid duplicate calculations, this method has O(n) time complexity and O(1) sapce complexity.

## Complexity Comparison

![complexity_comparisons](https://user-images.githubusercontent.com/56274068/66413629-9a119100-e9ac-11e9-98ce-708393a561a7.png)

## Good Fib Recusrion Trace for n = 10
The duplicate calculations are avoided using tuple as return value and calculating only n-1 in the recusrion.

![good_fib_trace](https://user-images.githubusercontent.com/56274068/66357519-10b67c00-e924-11e9-8057-ad9bdefaf6f1.png)

## Dynamic Fib Recusrion Trace for n = 10
The duplicate calculations are avoided using dictionary to keep track of previously calculated values. Dictionary grows linearly.

![dynamic_fib_trace](https://user-images.githubusercontent.com/56274068/66357578-32affe80-e924-11e9-8d1c-79683ecedd47.png)

## Bad Fib Recursion Trace for n = 10
This function wastes time in calculating previous calculated lower order terms again and again. For example bad_fib(8) twice one for bad_fib(10) and other for bad_fib(9). Likewise bad_fib(1) called 55 times, bad_fib(2) called 34 times, bad_fib(3) called 21 times, bad_fib(4) called 13 times, bad_fib(5) called 8 times, bad_fib(6) called 5 times, bad_fib(7) called 3 times.

![bad_fib_trace](https://user-images.githubusercontent.com/56274068/66413786-ea88ee80-e9ac-11e9-85c1-17159a4d620b.png)



