from lightfm import LightFM
from lightfm.datasets import fetch_movielens
from lightfm.evaluation import precision_at_k

data = fetch_movielens(min_rating=5)

model = LightFM(loss='warp')
print(data)
model.fit(data['train'], epochs=30, num_threads=2)

test_precision = precision_at_k(model, data['test'],k=5).mean()
print(test_precision)
print(type(data['train']))