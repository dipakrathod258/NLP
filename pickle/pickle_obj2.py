import pickle
filename = "fruits"
f = open(filename, 'rb')
x = pickle.load(f)
print(x)