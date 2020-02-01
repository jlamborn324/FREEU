from django.shortcuts import render
from .models import ItemPost


# items = [
#         {"User": "John", 
#         "Item": "Dog", 
#         "Condition":"bad bro"
#         },

#         {"User": "Nancy", 
#         "Item": "flashlight", 
#         "Condition":"Great"}

# ]

def home(request):

    context = {
        'posts': ItemPost.objects.all()
    }
    return render(request, 'marketplace/home.html', context)


# Create your views he