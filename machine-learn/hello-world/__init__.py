from sklearn import  tree
print "machine-learn"

'''
features = [[140, "smooth"], [130, "smooth"], [150, "bumpy"], [170, "bumpy"]]
labels = ["apple", "apple", "orange", "orange"]
'''
features = [[140, 1], [130, 1], [150, 0], [170, 0]]
labels = [1, 1, 0, 0]

print features
print labels

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print clf.predict([[160, 0]])