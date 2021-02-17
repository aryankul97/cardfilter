from django.db import models
from datetime import date
from django.conf import settings

#Model to save user details who will use the tool
class UserData(models.Model):
	created_date=models.DateTimeField(auto_now=True)
	user_id=models.CharField(max_length=50, primary_key=True)
	user_name=models.CharField(max_length=100)
	user_csv=models.FileField(upload_to='user_csv/')
	status=models.CharField(max_length=100, default='1')#For Soft Delete Function
	class Meta:
		db_table="UserData"

class CustomerData(models.Model):
	user_id=models.CharField(max_length=50)
	clientnum=models.CharField(max_length=25)
	attrition_flag=models.CharField(max_length=50)
	customer_age=models.CharField(max_length=5)
	gender=models.CharField(max_length=5)
	dependent_count=models.CharField(max_length=5)
	education_level=models.CharField(max_length=25)
	marital_status=models.CharField(max_length=20)
	income_category=models.CharField(max_length=50)
	card_category=models.CharField(max_length=20)
	months_on_book=models.CharField(max_length=10)
	total_relationship_count=models.CharField(max_length=10)
	months_inactive_12_mon=models.CharField(max_length=5)
	contacts_count_12_mon=models.CharField(max_length=5)
	credit_limit=models.CharField(max_length=10)
	total_revolving_bal=models.CharField(max_length=15)
	avg_open_to_buy=models.CharField(max_length=15)
	total_amt_chng_q4_q1=models.CharField(max_length=15)
	total_trans_amt=models.CharField(max_length=15)
	total_trans_ct=models.CharField(max_length=15)
	total_ct_chng_q4_q1=models.CharField(max_length=15)
	avg_utilization_ratio=models.CharField(max_length=20)
	naive_bayes_classifier_attrition_flag_card_category_contacts_count_12_mon_dependent_count_education_level_months_inactive_12_mon_1=models.CharField(max_length=100)
	naive_bayes_classifier_attrition_flag_card_category_contacts_count_12_mon_dependent_count_education_level_months_inactive_12_mon_2=models.CharField(max_length=100)
	class Meta:
		db_table="CustomerData"