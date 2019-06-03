from sklearn import datasets

iris=datasets.load_iris()

data=iris.data
target=iris.target

from sklearn.model_selection import train_test_split

train_data,test_data,train_target,test_target=train_test_split(data,target,test_size=0.1)

from sklearn import tree

clsfr=tree.DecisionTreeClassifier()

clsfr.fit(train_data,train_target)
results=clsfr.predict(test_data)

from sklearn import metrics

accuracy=metrics.accuracy_score(test_target,results)
print('Accuaracy:',accuracy)

