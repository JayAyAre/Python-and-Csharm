"""
    Shortcut operators

        It's time for the next set of operators that make a developer's life easier.

        we want to use one and the same variable both to the right and left sides of the = operator.

        For example, if we need to calculate a series of successive values of powers of 2,
            we may use a piece like this:

            x = x * 2

        You may use an expression like this if you can't fall asleep and you're trying to deal with it using some good,
            with old-fashioned methods

            sheep = sheep + 1

        Python offers you a shortened way of writing operations like these, which can be coded as follows:

            x *= 2
            sheep += 1

        If op is a two-argument operator, and is used in the following context:

            variable = variable op expression

        it can be simplified to:

            variable op= expression

        i = i + 2 * j ⇒ i += 2 * j

        var = var / 2 ⇒ var /= 2

        rem = rem % 10 ⇒ rem %= 10

        j = j - (i + var + rem) ⇒ j -= (i + var + rem)

        x = x ** 2 ⇒ x **= 2

        Go to LAB-6 and then LAB-7
"""
