#
# Starting Point: 
#   http://stackoverflow.com/questions/15173225/how-to-calculate-cosine-similarity-given-2-sentence-strings-python
#   Answer by http://stackoverflow.com/users/1859772/vpekar
#

import re, math
from collections import Counter

WORD = re.compile(r'\w+')

LOWER_LIMIT = 1
UPPER_LIMIT = 15

def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)

texts = {}
vectors = {}
cosines = {}

for X in range(LOWER_LIMIT,UPPER_LIMIT+1):
    texts[X] = X
    print "Reading Chp0%d" % X
    with open ("../Job/Chp"+str(X)+".txt", "r") as myfile:
        texts[X]=myfile.read().replace('\n', '')
    vectors[X] = text_to_vector(texts[X])

for X in range(LOWER_LIMIT+1,UPPER_LIMIT+1):
    cosines[X] = get_cosine(vectors[X-1], vectors[X])
    print "Cosines["+str(X-1)+","+str(X)+"] = " + str(cosines[X])

for X in range(LOWER_LIMIT,((UPPER_LIMIT-LOWER_LIMIT+1)/2)+1):
    print str(X) + " to " + str(UPPER_LIMIT-X+1) + " = ",
    print str(get_cosine(vectors[X],vectors[UPPER_LIMIT-X+1]))

# print "Cosine[1,10] = " + str(get_cosine(vectors[1], vectors[10]))
