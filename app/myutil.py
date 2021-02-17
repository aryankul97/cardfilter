from rest_framework import status
from rest_framework.response import Response

def success_response(data):
	content={'status':True, 'status_code':200, 'data':data}
	return Response(content, status=status.HTTP_200_OK)

def failure_response(data):
	content={'status':False, 'status_code':500, 'data':data}
	return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)