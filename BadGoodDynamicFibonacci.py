#!/usr/bin/env python
# coding: utf-8

# # Recursion Trace Function

# The trace wrapper function is implemented to print the recursiom trace with indentation for easy visualization of function execution.

# In[161]:


import timeit                #timeit for timecomplexity calculation
from functools import wraps  #wraps for recursion trace

def trace(func):
    func_name = func.__name__  #get the function name
    separator = "|  "          #separator for recursion indentation
    trace.recursion_depth = 0  #recursion depth
    
    @wraps(func)
    def trace_func(*args, **kwargs):
        # Print recursion invokation with indentation based on recursion_depth
        print(f"{separator * trace.recursion_depth}|--{func_name}({'. '.join(map(str, args))})") 
        trace.recursion_depth += 1 #keep track of recursion depth
        result = func(*args, **kwargs) #invoke new function call
        # Print recursion return with indentation based on recursion_depth
        print(f"{separator*trace.recursion_depth}|-- return {result}")
        trace.recursion_depth -= 1 #keep track of recursion depth
        #return the results
        return result
    
    #return the wrapper function
    return trace_func


# # BAD Fibonacci function

# The bad_fib is implemented to call the bad_fib(n-2) and bad_fib(n-1). This function has duplicate calls computation of lower ordered terms multiple times.

# In[162]:


def bad_fib(n):
    if n <= 1: 
        return n
    else: 
        return bad_fib(n-2) + bad_fib(n-1)


# # Good Fibonacci function

# The good_fib is implemented to use the tuple of last numbers in series to avoid duplicate calculations.

# In[163]:


def good_fib(n):
    if n <= 1: 
        return n, 0
    else: 
        a, b = good_fib(n-1)
        return a + b, a


# # Fibonacci function with Dynamic Programming

# The dynamic_fib is implemented to use dictionary memory to keep track of previously computed values to avoid duplicate calculations.

# In[164]:


def dynamic_fib(n, memo = {}):
    if n in memo.keys():    #if value calulated before return from memory
        return memo[n]
    else:
        if n <= 1: 
            rv = n
        else: 
            rv =  dynamic_fib(n-2, memo) + dynamic_fib(n-1, memo)  #claculate new value
        memo[n] = rv    #keep track of calcualted values
        return rv


# In[165]:


#calculate time complexity
print("Bad Fib for 10:    ", timeit.timeit(setup = "from __main__ import bad_fib", stmt = "bad_fib(10)", number = 10000))
print("Good Fib for 10:   ", timeit.timeit(setup = "from __main__ import good_fib", stmt = "good_fib(10)", number = 10000))
print("Dynamic Fib for 10:", timeit.timeit(setup = "from __main__ import dynamic_fib", stmt = "dynamic_fib(10)", number = 10000))


# In[166]:


#Get trace wraper function
bad_fib = trace(bad_fib)
good_fib = trace(good_fib)
dynamic_fib = trace(dynamic_fib)


# In[167]:


print(bad_fib(10)) #print recursion trace for bad_fib


# In[168]:


print(good_fib(10)) #print recursion trace for good_fib


# In[169]:


print(dynamic_fib(10, {})) #print recursion trace for dynamic_fib

