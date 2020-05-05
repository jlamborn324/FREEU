from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, 
DetailView, 
CreateView,
UpdateView,  
DeleteView, 
)
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import ItemPost
from django.db.models import Q


def home(request):

    context = {
        'posts': ItemPost.objects.all()
    }

    return render(request, 'marketplace/home.html', context)


class SearchResultsView(ListView):
    model = ItemPost
    template_name = 'marketplace/search_result.html'
    paginate_by = 2
    def get_queryset(self):

        query = self.request.GET.get('q')
        if query:
            object_list = ItemPost.objects.filter(
                Q(title__icontains=query) 
                )
            return object_list

    #         posts_list = Post.objects.all()
    # query = request.GET.get('q')
    # if query:
    #     posts_list = Post.objects.filter(
    #         Q(title__icontains=query) | Q(content__icontains=query) |
    #         Q(user__first_name__icontains=query) | Q(user__last_name__icontains=query)
    #     ).distinct()
    # paginator = Paginator(posts_list, 6) # 6 posts per page
    # page = request.GET.get('page')

    # try:
    #     posts = paginator.page(page)
    # except PageNotAnInteger:
    #     posts = paginator.page(1)
    # except EmptyPage:
    #     posts = paginator.page(paginator.num_pages)

    # context = {
    #     'posts': posts
    # }
    # return render(request, "post-list.html", context)



class PostListView(ListView): 
    model = ItemPost
    template_name = 'marketplace/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10


class PostDetailView(DetailView): 
    model = ItemPost

    template_name = 'marketplace/ItemPost_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView): 
    model = ItemPost
    fields = ['title', 'condition', 'item_image']
    template_name = 'marketplace/ItemPost_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ItemPost
    fields = ['title', 'condition']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        ItemPost = self.get_object()
        if self.request.user == ItemPost.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ItemPost
    success_url = '/'
    template_name = 'marketplace/ItemPost_confirm_delete.html'

    def test_func(self):
        ItemPost = self.get_object()
        if self.request.user == ItemPost.author:
            return True
        return False
