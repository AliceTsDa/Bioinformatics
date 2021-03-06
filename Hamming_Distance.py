# Input:  Two strings p and q
# Output: An integer value representing the Hamming Distance between p and q.
def HammingDistance(p, q):
    distance=0
    for i in range(len(p)):
       if (p[i]!=q[i]) :
        distance+=1

    return distance

#...............................................
# Input:  Strings Pattern and Text along with an integer d
# Output: A list containing all starting positions where Pattern appears
# as a substring of Text with at most d mismatches
def ApproximatePatternMatching(Text, Pattern, d):
    positions = [] # initializing list of positions
    for i in range (len(Text)-len(Pattern)+1):
        hd=HammingDistance(Text[i:i+len(Pattern)], Pattern)
        if (hd<=d):
            positions.append(i)
    return positions


def HammingDistance(p, q):
    distance=0
    for i in range(len(p)):
       if (p[i]!=q[i]) :
        distance+=1

    return distance
 #.....................................................
 # Input:  Strings Pattern and Text, and an integer d
# Output: The number of times Pattern appears in Text with at most d mismatches
def ApproximatePatternCount(Pattern, Text, d):
    count = 0 # initialize count variable
    for i in range (len(Text)-len(Pattern)+1):
        hd=HammingDistance(Text[i:i+len(Pattern)], Pattern)
        if (hd<=d):
            count+=1
    return count


def HammingDistance(p, q):
    distance=0
    for i in range(len(p)):
       if (p[i]!=q[i]) :
        distance+=1

    return distance


### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
lines = sys.stdin.read().splitlines()
print(ApproximatePatternCount(lines[0],lines[1],int(lines[2])))
