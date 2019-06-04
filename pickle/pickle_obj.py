import pickle
fruits = ["orange","Apple","Banana","mango"]
filename = "fruits"
f = open(filename, 'wb')
pickle.dump(fruits, f)
f.close()