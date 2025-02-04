from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import UserSerializer

@api_view(['POST'])
def add_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User added successfully!", "data": serializer.data}, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def receive_survey(request):
    try:
       
        data = request.data  
    
        survey = Survey(
            Question_1=data.get('Question_1'),
            Question_2=data.get('Question_2'),
            Question_3=data.get('Question_3')
        )
        survey.save() 
        return Response({"message": "Survey data inserted successfully!"}, status=201)

    except Exception as e:
        return Response({"error": str(e)}, status=400)

@api_view(['GET'])
def home(request):
    return Response({"message": "Hello, Django Server is Running!"})
