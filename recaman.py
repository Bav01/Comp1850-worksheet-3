L = int(input("Length of sequence: ")) # this should be your only input

sequence = [0]

# Your code for the Recaman Sequence

for k in range(1, L):
        prev = sequence[-1]
        next_val = prev - k
        if next_val > 0 and next_val not in sequence:
            sequence.append(next_val)
        else:
            sequence.append(prev + k)

# You should stire the sequence in an appropriate data structure named 'sequence'

# You may wish to use further output for testing purposes while you develop your code

# Please remove any extra output before submitting to Gradescope
    

# your only output for submission should be the final sequence

[ print(item) for item in sequence ]    

# this method is reasonably independent of the choice of data structure
