from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class StudentRecords(models.Model):
    student_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    reg_no=models.CharField(max_length=100, unique=True)
    fee_payment_status=models.CharField(max_length=100)
    exam_performance=models.FloatField()
    reporting_status=models.CharField(max_length=100)
    needs_assistance=models.BooleanField(default=False)

    class Meta:
        db_table='student_records'

