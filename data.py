import pandas as pd
import random

names = ["John Doe", "Jane Smith", "Alice Brown", "Tom Johnson", "Linda Wilson", "Michael Davis", 
         "Emily Taylor", "Sarah Miller", "James Brown", "Laura White"]
fee_payment_status_options = ["Paid", "Partial", "Unpaid"]
reporting_status_options = ["Consistent", "Irregular", "Absent"]


data = []
for _ in range(100):
    record = {
        "name": random.choice(names),
        "fee_payment_status": random.choice(fee_payment_status_options),
        "exam_performance": round(random.uniform(30, 100), 1),  
        "reporting_status": random.choice(reporting_status_options)
    }
    data.append(record)


df = pd.DataFrame(data)
csv_path = "student_training_data.csv"
df.to_csv(csv_path, index=False)

csv_path
