import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np


data_dict = pickle.load(open('./data.pickle', 'rb'))
# print(data_dict)

data = data_dict['data']
# print(type(data))
labels = data_dict['labels']
# print(labels)

# print(data[0:3])

# print(dbeyfg)

dummy = []
for x in data:

    dummy.append(np.array(x))
data = dummy

for i in range(0, len(data)):
    if i < len(data) and data[i].shape[0] != data[0].shape[0]:
        print(i)
        data.pop(i)
        labels.pop(i)


x_train, x_test, y_train, y_test = train_test_split(
    data, labels, test_size=0.2, shuffle=True, stratify=labels)
l1 = []
l2 = []
for i in y_test:
    l2.append(int(i))
for i in y_train:
    l1.append(int(i))

y_train = l1
y_test = l2

print(len(x_train))
model = RandomForestClassifier()

model.fit(x_train, y_train)

y_predict = model.predict(x_test)

score = accuracy_score(y_predict, y_test)

print('{}% of samples were classified correctly !'.format(score * 100))

f = open('model.p', 'wb')
pickle.dump({'model': model}, f)
f.close()
