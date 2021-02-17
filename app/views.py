from django.views.decorators.csrf import *
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from app.myutil import *
from app.models import *
import pandas as pd
from django.core import serializers

@api_view(['POST'])
@csrf_exempt
def user(request):
	try:
		data=request.data
		username=data['username']
		usercsv=data['usercsv']
		u='USR'
		x=1
		uid=u+str(x)
		while UserData.objects.filter(user_id=uid).exists():
			x=x+1
			uid=u+str(x)
		UserData(
			user_id=uid,
			user_name=username,
			user_csv=usercsv
		).save()
		usercsv=UserData.objects.filter(user_id=uid)[0].user_csv.url
		df=pd.read_csv(usercsv[1:(len(usercsv)+1)])
		for x in range(0,len(df)):
			data=df.loc[x]
			CustomerData(
				user_id=uid,
				clientnum=data.CLIENTNUM,
				attrition_flag=data.Attrition_Flag,
				customer_age=data.Customer_Age,
				gender=data.Gender,
				dependent_count=data.Dependent_count,
				education_level=data.Education_Level,
				marital_status=data.Marital_Status,
				income_category=data.Income_Category,
				card_category=data.Card_Category,
				months_on_book=data.Months_on_book,
				total_relationship_count=data.Total_Relationship_Count,
				months_inactive_12_mon=data.Months_Inactive_12_mon,
				contacts_count_12_mon=data.Contacts_Count_12_mon,
				credit_limit=data.Credit_Limit,
				total_revolving_bal=data.Total_Revolving_Bal,
				avg_open_to_buy=data.Avg_Open_To_Buy,
				total_amt_chng_q4_q1=data.Total_Amt_Chng_Q4_Q1,
				total_trans_amt=data.Total_Trans_Amt,
				total_trans_ct=data.Total_Trans_Ct,
				total_ct_chng_q4_q1=data.Total_Ct_Chng_Q4_Q1,
				avg_utilization_ratio=data.Avg_Utilization_Ratio,
				naive_bayes_classifier_attrition_flag_card_category_contacts_count_12_mon_dependent_count_education_level_months_inactive_12_mon_1=data.Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1,
				naive_bayes_classifier_attrition_flag_card_category_contacts_count_12_mon_dependent_count_education_level_months_inactive_12_mon_2=data.Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2
			).save()
		data={'user_id':uid,'msg':'User created and CSV saved successfully.'}
		return success_response(data)
	except:
		data={'msg':'Some error occured.'}
		return failure_response(data)

@api_view(['GET'])
@csrf_exempt
def customers(request):
	try:
		data=request.data
		age=data['age']
		gender=data['gender']
		card_category=data['card_category']
		user_id=data['user_id']
		data=serializers.serialize('json', CustomerData.objects.filter(user_id=user_id, customer_age=age, gender=gender, card_category=card_category))
		return success_response(data)
	except:
		data={'msg':'Some error occured.'}
		return failure_response(data)