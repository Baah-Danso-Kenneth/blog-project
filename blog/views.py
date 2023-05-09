from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    context={"posts":posts}
    return render(request,'blog/post/post_list.html',context)

def post_detail(request,id):
    # try:
    #     post = Post.objects.get(id=id)
    # except Post.DoesNotExit:
    #     raise Http404("No post found")
    # return render(request,'blog/post/detail.html',{"post":post})
    post=get_object_or_404(Post,id=id)
    return render(request,'blog/post/detail.html',{"post":post})
