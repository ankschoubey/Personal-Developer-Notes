import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM

#fetch dataset and format

data = fetch_movielens(min_rating=4.0)

# print training and testing data

print(repr(data['train']))
print(repr(data['test']))

# create model

model = LightFM(loss='warp') #Weighted Approximate Rank Pairwise
model.fit(data['train'], epochs=30, num_threads=2)

def sample_recommendation(model, data, user_ids):
    n_users, n_items = data['train'].shape

    #generate recommendation for each user

    for user in user_ids:
        #compresses sparsed row format

        #movie they already like
        known_positives = data['item_labels'][data['train'].tocsr()[user].indices]

        # movie our model predicts that they like
        scores = model.predict(user, np.arange(n_items))

        # rank them in order of most liked
        top_items = data['item_labels'][np.argsort(-scores)]# will print in discending order because of -

        print('User %s' % user)

        print('Known positive')

        for i in known_positives[:3]:
            print('         %s' % i)

        print('Top 10 recommended movie')

        for i in top_items[:3]:
            print('         %s' %i)

sample_recommendation(model, data, [3,45,360])
