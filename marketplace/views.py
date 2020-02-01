from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import ItemPost
from django.db.models import Q


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

class SearchResultsView(ListView):
    model = ItemPost
    template_name = 'marketplace/search_result.html'
    def get_queryset(self):

        query = self.request.GET.get('q')
        if query:
            object_list = ItemPost.objects.filter(
                Q(title__icontains=query) 
                )
            return object_list




class PostListView(ListView): 
    model = ItemPost
    template_name = 'marketplace/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView): 
    model = ItemPost



# Create your views he