import pandas as pd
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
import pickle

train_df = pd.read_csv('D:/boku no projecto/python/image/cctv/datasets_an_biyan.csv')

dataset = train_df.to_numpy()
np.random.shuffle(dataset)



x_train = dataset[:300,:-1]/255.
y_train = dataset[:300,-1]
x_test = dataset[300:,:-1]/255.
y_test = dataset[300:,-1]

# 200,200,200,200,200,200,200,200,200,200
clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(50), random_state=1, max_iter = 1000)
clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)
print(y_test.shape)
print(y_pred.shape)

score = accuracy_score(y_test, y_pred)
print(score)

filename = 'D:/boku no projecto/python/image/cctv/model_mac_an_biyan.sav'
pickle.dump(clf, open(filename, 'wb'))
# print(dataset.shape)
