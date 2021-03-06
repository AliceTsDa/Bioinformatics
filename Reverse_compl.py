# Input:  A string Pattern
# Output: The reverse of Pattern
def Reverse(Pattern):
    rev= '' #create an empty string
    for char in Pattern: #going over each character in the string
        rev = char + rev
    return rev

# Input:  A DNA string Pattern
# Output: The complementary string of Pattern (with every nucleotide replaced by its complement).
def Complement(Pattern):
    pairs={"A":"T", "G":"C", "T":"A", "C":"G"}
    complement=''
    for base in Pattern:
        complement += pairs.get(base)
    return complement


# Input:  A DNA string Pattern
# Output: The reverse complement of Pattern
def ReverseComplement(Pattern):
    Pattern = Reverse(Pattern) # reverse all letters in a string
    Pattern = Complement(Pattern) # complement each letter in a string
    return Pattern

def Reverse(Pattern):
    rev= '' #create an empty string
    for char in Pattern: #going over each character in the string
        rev = char + rev
    return rev

def Complement(Pattern):
    pairs={"A":"T", "G":"C", "T":"A", "C":"G"}
    complement=''
    for base in Pattern:
        complement += pairs.get(base)
    return complement

#adding data to test it
Pattern = [""]

RC=ReverseComplement(Pattern)
print (RC)
