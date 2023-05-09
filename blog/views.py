from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator
def post_list(request):
    post_list = Post.objects.all()
    paginator=Paginator(post_list,3)
    page_number=request.GET.get('page',1)
    posts= paginator.page(page_number)
    context = {"posts": posts}
    return render(request, 'blog/post/post_list.html', context)

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, publish__year=year,publish__month=month,publish__day=day)
    return render(request, 'blog/post/detail.html', {"post": post})
