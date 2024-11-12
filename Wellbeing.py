import pickle
import pandas as pd
from sqlalchemy import create_engine, text
from sklearn.preprocessing import LabelEncoder

DATABASE_URL="postgresql://root:password@localhost:5432/university_db"

engine=create_engine(DATABASE_URL)

query="SELECT * FROM student_records; "

data=pd.read_sql(query,engine)

# print(data)


le_payment=LabelEncoder().fit(['Paid','Partial','Unpaid'])
le_reporting=LabelEncoder().fit(['Consistent','Irregular','Absent'])

data['name']=LabelEncoder().fit_transform(data['name'])
data['fee_payment_status']=le_payment.transform(data['fee_payment_status'])
data['reporting_status']=le_reporting.transform(data['reporting_status'])

# print(data)

with open('Student_Wellbeing_Model.pkl','rb') as file:
    model=pickle.load(file)

x=data[['name','fee_payment_status','exam_performance','reporting_status']]
data['needs_assistance']=model.predict(x)

stu_needing_assistance=data[data['needs_assistance']==1]

print('Students needing assistance: \n',stu_needing_assistance[['student_id','needs_assistance']])



for _, row in stu_needing_assistance.iterrows():
    update_query= text("""
    UPDATE student_records
    SET needs_assistance = :needs_assistance
    WHERE student_id= :student_id;
                      """)

    with engine.connect() as connection:
        with connection.begin():
             connection.execute(update_query,{'needs_assistance':True,'student_id':row['student_id']})
  

