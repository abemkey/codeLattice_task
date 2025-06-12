import requests
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from My_App.forms import Person_Form
from My_App.models import User
from My_App.serializers import PersonSerializer, UserSerializer


# Create your views here.
def home(request):
    return render(request,'home.html')



def add_person(request):
    form = Person_Form()
    if request.method == 'POST':
        form = Person_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')


    return render(request, 'person_form.html', {'form': form})

@api_view(['POST'])
def create_person(request):
    serializer = PersonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

def show_users(request):
    url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url)

    users = []
    if response.status_code == 200:
        users_data = response.json()
        users = users_data

        for user_data in users_data:

            if not User.objects.filter(username=user_data['username']).exists():
                User.objects.create(
                    name=user_data['name'],
                    username=user_data['username'],
                    email=user_data['email'],
                    phone=user_data['phone'],
                    website=user_data['website']
                )

    return render(request, 'view_users.html', {'users': users})


@api_view(['GET'])
def users_api(request):
    url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        for user_data in data:

            if not User.objects.filter(username=user_data['username']).exists():
                User.objects.create(
                    name=user_data['name'],
                    username=user_data['username'],
                    email=user_data['email'],
                    phone=user_data['phone'],
                    website=user_data['website']
                )

        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(
        {"error": "Failed to fetch data from external API"},
        status=status.HTTP_502_BAD_GATEWAY
    )