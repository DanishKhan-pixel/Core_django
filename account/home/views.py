from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    # dynamic data pass at html page     
    people=[
        {'name':'ali khan', 'age': 23},
        {'name':'ali ', 'age': 12},
        {'name':'ali bab ', 'age': 22},
        {'name':'ali  khan bab', 'age': 22},
        {'name':'ali ahamad', 'age': 22},
        {'name':'ali muhammad', 'age': 22},
    ]
    cars=['car1','car2','car3']    # for people in people: # for checking data pass or not 
    print(people)
    return render(request, 'home/index.html', context={'people':people, 'cars':cars})





