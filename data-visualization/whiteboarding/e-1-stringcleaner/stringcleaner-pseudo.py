# You just invested in some optical character recognition software, but you saved on the budget and the software isn't that great.

# You quickly realize that the software inserts some unnecessary numerical characters.

# Your job is to write a function that takes these strings as inputs, and cleans out the numeric characters and return a string with special characters and spacing all intact.

# For example:
# string_clean('Thi3s looks65 awesom4e!') == 'This looks great!'

# Special characters include: ~#$%^&!@*():;"'.,?

# input number params: n>=0 && n<=arr.length


def string_clean(string):
    # loop through the string and if if the index/iterator  is in the range of 0 through 10
    
    # if it is, replace with nothing ''
    
    # return the string

print(string_clean('Thi3s looks65 awesom4e!'));
