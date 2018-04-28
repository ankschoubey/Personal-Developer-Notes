import math
import sklearn.metrics.pairwise as sk

def sorted_arguments(vector,n):
    top_n = []

    sort = sorted(vector, reverse=True)
    length = len(vector)
    for i in range(0,n+1):
        if i >=length:
            continue

        if sort[i] is 0:
            break
        index = vector.index(sort[i])
        top_n.append(i)
    return top_n[1:]

def get_index_after_sorting(vector):
    indexes = []

    sort = sorted(vector, reverse=True)

    for i in sort:
        indexes.append(vector.index(i))
    return indexes


def generate_recommendations(user_to_recommend, user_rating, similar_users, similarity_vector):

    item_similarity = []
    for i in range(len(user_rating[user_to_recommend])):
        if user_rating[user_to_recommend][i] != 0:
            item_similarity.append(0)
            continue
        weightage_of_item = 0
        for k in similar_users:
            weightage_of_item+=user_rating[k][i]*similarity_vector[k]
        item_similarity.append(round(weightage_of_item,2))

    print('Item\'s weightage', item_similarity)

    return [i for i in get_index_after_sorting(item_similarity) if i !=0]


user_rating = [[4,3,0,0,5,0],[5,0,4,0,4,0],[4,0,5,3,4,0],[0,3,0,0,0,5],[0,4,0,0,0,4],[0,0,2,4,0,5]]

similarity_matrix = []

for i in user_rating:
    temp = []
    for j in user_rating:
        if i == j:
            continue
        temp.append(round(sk.cosine_similarity(i,j),1))
    similarity_matrix.append(temp)

print('Similarity Matrix')
for i in similarity_matrix:
    print(i)

user_to_recommend = 0
similar_users = sorted_arguments(similarity_matrix[user_to_recommend],2)
print("User's similar to user", user_to_recommend , 'are',similar_users)

recommendation = generate_recommendations(user_to_recommend, user_rating, similar_users, similarity_matrix[user_to_recommend])
print("The items user is most likely to purchase are")
for i in recommendation:
    print(i)
