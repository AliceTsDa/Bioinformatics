# Input:  A String Genome
# Output: The skew array of Genome as a list.
def SkewArray(Genome):
    Skew=[0]
    for i in range (len(Genome)):
        if Genome[i] == 'C':
            Skew.append(Skew[i] - 1)
        elif Genome[i] == 'G':
            Skew.append(Skew[i] + 1)
        else:
            Skew.append(Skew[i])
    return Skew
#.................................................
# Input:  A DNA string Genome
# Output: A list containing all integers i minimizing Skew(Prefix_i(Text)) over all values of i (from 0 to |Genome|)
def MinimumSkew(Genome):
   positions = [] # output variable
   temp=SkewArray(Genome)
   minimum=min(temp)
   for i in range (len(temp)):
       if (temp[i]==minimum):
        positions.append(i)
   return positions


# Input:  A String Genome
# Output: SkewArray(Genome)
# HINT:   This code should be taken from the last Code Challenge.
def SkewArray(Genome):
    Skew=[0]
    for i in range (len(Genome)):
        if Genome[i] == 'C':
            Skew.append(Skew[i] - 1)
        elif Genome[i] == 'G':
            Skew.append(Skew[i] + 1)
        else:
            Skew.append(Skew[i])
    return Skew
