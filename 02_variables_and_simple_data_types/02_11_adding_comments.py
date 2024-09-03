"""
Micki Eustache
Here's a new program made for this Try-It assignment.
"""

print("The homework so far has been pretty simple.")
message1 = "    Python is cool though.\n"
message2 = "    It reminds me of C++. \t "

'''
There seems to be unneeded whitespace in my messages!

Let's get rid of it but keep the whitespace to the right of message1
This can be done on the same line of code as it is printed.
We can even print both of my messages on one line.
'''

print(message1.lstrip(), message2.strip())

# All done!