from sklearn.feature_extraction.text import CountVectorizer
import pickle
import pandas as pd
f = open('model.pickle', 'rb')
model = pickle.load(f)
f.close()

f = open('x_train.pickle', 'rb')
x_train = pickle.load(f)
f.close()
v = CountVectorizer()

x_train_count = v.fit_transform(x_train.values)

x ='y'

while x == 'y':
    m = []
    m.append(input("\nEnter the Message you want to Check : \n"))
    m_count = v.transform(m)
    pred = model.predict(m_count)
    print("\n")
    print("Message is a spam \n") if pred[0] == 1 else print("Message is NOT a Spam \n")
    # print(str(pred))
    x =input("Want to continue [y/n]")
