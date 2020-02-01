from django.shortcuts import render


items = [
        {"User": "John", 
        "Item": "Dog", 
        "Condition":"bad bro"
        },

        {"User": "Nancy", 
        "Item": "flashlight", 
        "Condition":"Great"}

]

def home(request):
    return render(request, 'marketplace/home.html', {'items': items})


# Create your views he