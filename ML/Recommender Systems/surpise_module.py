from surprise import SVD
from surprise import Dataset
from surprise import evaluate, print_perf


data = Dataset.load_builtin('ml-100k')
data.split(n_folds=3)

algo = SVD()

perf = evaluate(algo, data, measures=['RMSE','MAE'])

print_perf(perf)