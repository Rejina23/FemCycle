# myapp/views.py
from .Menstrual_test import predictor
from rest_framework import viewsets
from .models import UserData
from .serializers import UserDataSerializer, UserRegistrationSerializer, UserLoginSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.permissions import IsAuthenticated


class UserDataViewSet(viewsets.ModelViewSet):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        # You can customize the create method here
        # For example, you can perform additional actions before or after creating the object
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.validated_data)
            age = serializer.validated_data.get('age')
            length_of_cycle = serializer.validated_data.get('length_of_cycle')
            length_of_luteal = serializer.validated_data.get('length_of_luteal')
            total_num_of_high_days = serializer.validated_data.get('total_num_of_high_days')
            total_num_of_peak_days = serializer.validated_data.get('total_num_of_peak_days')
            total_days_of_fertility = serializer.validated_data.get('total_days_of_fertility')
            bmi = serializer.validated_data.get('bmi')
            total_fertility_formula = serializer.validated_data.get('total_fertility_formula')
            length_of_menses = serializer.validated_data.get('length_of_menses')

            # Add your custom response data if needed
            response_data = {
                "message": "User data created successfully",
                "data": predictor(age, length_of_cycle, length_of_luteal, total_num_of_high_days, total_num_of_peak_days, total_days_of_fertility, bmi, total_fertility_formula,length_of_menses)
            }

            return Response(response_data, status=201)
        return Response(serializer.errors, status=400)
    


class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            confirm_password = serializer.validated_data['confirm_password']

            if password != confirm_password:
                return Response({'error': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.create_user(username=username, email=email, password=password)
            return Response({
                'detail':"User created successfully"
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user:
                return Response({'detail': "Logged in successfully!"}, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid login credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]