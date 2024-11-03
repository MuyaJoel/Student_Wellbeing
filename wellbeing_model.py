import pickle
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report

data=pd.read_csv('student_training_data.csv')

print(data)

LabelEncoder=LabelEncoder()
data['name']=LabelEncoder.fit_transform(data['name'])
data['fee_payment_status']=LabelEncoder.fit_transform(data['fee_payment_status'])
data['reporting_status']=LabelEncoder.fit_transform(data['reporting_status'])


#features x and target y
x=data[['name','fee_payment_status','exam_performance','reporting_status']]
y=data['needs_assistance']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)

model = DecisionTreeClassifier()
model.fit(x_train,y_train)

y_pred=model.predict(x_test)

report=classification_report(y_test,y_pred)
print("Classification Report : \n", report)


filename="Student_Wellbeing_Model.pkl"

with open(filename,'wb') as file:
    pickle.dump(model, file)

print("Model Saved as:", filename)