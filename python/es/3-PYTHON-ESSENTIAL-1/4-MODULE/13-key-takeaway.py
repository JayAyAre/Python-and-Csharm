"""
    Key takeaways

        1. A function can call other functions or even itself. When a function calls itself, this situation is known as recursion
            and the function which calls itself and contains a specified termination condition (i.e., the base case - a condition which 
            doesn't tell the function to make any further calls to that function) is called a recursive function.

        2. You can use recursive functions in Python to write clean, elegant code, and divide it into smaller, organized chunks. 
            On the other hand, you need to be very careful as it might be easy to make a mistake and create a function which never terminates.
            You also need to remember that recursive calls consume a lot of memory, and therefore may sometimes be inefficient.

            # Recursive implementation of the factorial function.

                def factorial(n):
                    if n == 1:    # The base case (termination condition.)
                        return 1
                    else:
                        return n * factorial(n - 1)


                print(factorial(4)) # 4 * 3 * 2 * 1 = 24


            Exercise 1

                What will happen when you attempt to run the following snippet and why?

                    def factorial(n):
                        return n * factorial(n - 1)


                    print(factorial(4))

            Exercise 2

                What is the output of the following snippet?

                    def fun(a):
                        if a > 30:
                            return 3
                        else:
                            return a + fun(a + 3)


                    print(fun(25))
"""
