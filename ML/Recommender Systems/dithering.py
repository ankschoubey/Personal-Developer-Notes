
from numpy.random import normal
from math import log
def ditter(ranked_recommendations, ditter_value):
    result = []
    for i in ranked_recommendations:
        ditter_score = log(i+1) + normal(0, log(ditter_value))
        result.append(ditter_score)

    for i in range(len(result)):
        for j in range(len(result)-i-1):
            if result[j]>result[j+1]:
                result[j],result[j + 1]=result[j+1],result[j]
                ranked_recommendations[j], ranked_recommendations[j+1]= ranked_recommendations[j+1], ranked_recommendations[j]

    return ranked_recommendations

ranked_list = [i for i in range(1,100)]
dittered_list =  ditter(ranked_list[:],3)
for i,j in zip(ranked_list,dittered_list):
    print(i,j,abs(i-j))

print(ranked_list)
print(dittered_list)p