# You will have to figure out what parameters to include
#  All functions must use recursion

# This function returns an array of all possible outcomes from flipping a coin N times.
# Input type: Integer 
# H stands for Heads and T stands for tails
# Represent the two outcomes of each flip as "H" or "T"

def coin_flips(n):
    # Write code here
    def push_results(n, array, string):
        if (n == 1): 
            array.append(string + 'H')
            array.append(string + 'T')
        else:
            push_results(n - 1, array, string + 'H')
            push_results(n - 1, array, string + 'T')
    resultArray = []
    push_results(n, resultArray, '')
    return resultArray


    

print(coin_flips(3)) 
# => ["HH", "HT", "TH", "TT"]