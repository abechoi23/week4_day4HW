# Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.


def strip_comments(text, comment_markers):
    lines = text.split('\n')
    # O(n)
    for i in range(len(lines)):
        # O(n)
        for marker in comment_markers:
            index = lines[i].find(marker)
            # O(1)
            if index != -1:
                lines[i] = lines[i][:index].rstrip()
                break
        else:
            lines[i] = lines[i].rstrip()
    return '\n'.join(lines)


#Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

def even_or_odd(number):
    # O(n)
        if number % 2 == 0:
            return 'Even'
        else: 
            return 'Odd'


# #  What if we need the length of the words separated by a space to be added at the end of that same word and have it returned as an array?

# Example(Input --> Output)

# "apple ban" --> ["apple 5", "ban 3"]
# "you will win" -->["you 3", "will 4", "win 3"]
# Your task is to write a function that takes a String and returns an Array/list with the length of each word added to each element .

# Note: String will have at least one element; words will always be separated by a space.

def add_length(str_):
    words = str_.split()
    # O(n)
    return [word + " " + str(len(word)) for word in words]