"""
    Key takeaways

    1. The list is a type of data in Python used to store multiple objects.
        It is an ordered and mutable collection of comma-separated items between square brackets, e.g.:

            my_list = [1, None, True, "I am a string", 256, 0]

    2. Lists can be indexed and updated, e.g.:

            my_list = [1, None, True, 'I am a string', 256, 0]
            print(my_list[3])  # outputs: I am a string
            print(my_list[-1])  # outputs: 0

            my_list[1] = '?'
            print(my_list)  # outputs: [1, '?', True, 'I am a string', 256, 0]

            my_list.insert(0, "first")
            my_list.append("last")
            print(my_list)  # outputs: ['first', 1, '?', True, 'I am a string', 256, 0, 'last']

    3. Lists can be nested, e.g.:

            my_list = [1, 'a', ["list", 64, [0, 1], False]]

    4. List elements and lists can be deleted, e.g.:

            my_list = [1, 2, 3, 4]
            del my_list[2]
            print(my_list)  # outputs: [1, 2, 4]

            del my_list  # deletes the whole list

    5. Lists can be iterated through using the for loop, e.g.:

            my_list = ["white", "purple", "blue", "yellow", "green"]

            for color in my_list:
                print(color)

    6. The len() function may be used to check the list's length, e.g.:

            my_list = ["white", "purple", "blue", "yellow", "green"]
            print(len(my_list))  # outputs 5

            del my_list[2]
            print(len(my_list))  # outputs 4

    7. A typical function invocation looks as follows: result = function(arg),
        while a typical method invocation looks like this:result = data.method(arg).


    Exercise 1

        What is the output of the following snippet?

            lst = [1, 2, 3, 4, 5]
            lst.insert(1, 6)
            del lst[0]
            lst.append(1)

            print(lst)

    Exercise 2

        What is the output of the following snippet?

            lst = [1, 2, 3, 4, 5]
            lst_2 = []
            add = 0

            for number in lst:
                add += number
                lst_2.append(add)

            print(lst_2)

    Exercise 3

        What happens when you run the following snippet?

            lst = []
            del lst
            print(lst)

    Exercise 4

        What is the output of the following snippet?

            lst = [1, [2, 3], 4]
            print(lst[1])
            print(len(lst))
"""