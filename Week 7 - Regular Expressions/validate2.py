# we will improve our design incrementally
import re

email = input("What's your email? ").strip()

"""
# Inefficeint code --> we need more vocabulary to become more proficient
if re.search("@", email): # "if re.search() contains "@" in 'email' then..."
    print("Valid")
else:
    print("Invalid")
"""

# it's not enough only checking the "@" sign, we need to also check to the left and to the right
# How to represent it? 
# Use single periot '.' --> indicates any character except for a new line
# But, we do not only want a single character (expressing any character), 
# what we want is multiple characters expressing any character
# So then, we can do '.*' --> any character, except new lines (blank line), with 0 or more repetitions 

"""
if re.search(".*@.*", email):
    print("Valid")
else:
    print("Invalid")
"""

# Recall "*" indicates 0 or more repetitions
# since '.*' indicates any character, except new lines (white lines), with 0 or more repetitions
# when the user inputs something like 'jcb6609@' it counts as Valid since the repetition of any character ('.') is indeed zero (zero repetitions), which holds for '*'
# we will need to instead use '+', which accepts 1 or more repetitions

"""
if re.search(".+@.+", email):
    print("Valid")
else:
    print("Invalid")
"""

# We could also use '*' to solve this problem, if we do:
# '..*' --> any character with any character with 0 or more repetitions

"""
if re.search("..*@..*", email):
    print("Valid")
else:
    print("Invalid")
"""

# -> Recall when you pass this argument, let's say '.*@.*', to the re.search() function,
# it is going to read it from left to right and then use it to try to match against the second argument-input 'email' in this case that the user typed-in

# Now, how is the computer, how is re.search going to keep track of whether or not the user's 'email' our patterns?
# Answ: Machine of sorts --> finite-state machine (nondeterministic finite automaton)

# For our '.*@.*' pattern:
"""
             .                 .
            //                //
           ____              ____
          |    |     @      |    |
start --> | q1 | ---------> | q2 |
          |____|            |____|

"""

# four our '.+@.+' pattern:
"""
                               .                                    .
                              //                                   //
           ____              ____              ____               ____
          |    |     .      |    |     @      |    |      .      |    |
start --> | q1 | ---------> | q2 | ---------> | q3 | ----------> | q4 |
          |____|            |____|            |____|             |____|

"""