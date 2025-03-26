import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB                       

data = pd.read_csv("D:\CV Projects\Email-Spam-Detection\spam.csv")

data.drop_duplicates(inplace=True)
data['Category'] = data['Category'].replace(['ham','spam'],['Not Spam' ,'Spam'])

mess = data['Message']
cat = data['Category']
(mess_train,mess_test,cat_train,cat_test) = train_test_split(mess ,cat ,test_size=0.2)
cv = CountVectorizer(stop_words='english')
cv.fit_transform(mess_train)
featuers = cv.fit_transform(mess_train)

#creating model

model = MultinomialNB()
model.fit(featuers, cat_train)

#test our model
featuers_test = cv.transform(mess_test)
print(model.score(featuers_test, cat_test))
