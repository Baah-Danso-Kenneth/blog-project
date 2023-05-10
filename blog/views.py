from django.core.mail import send_mail
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EmailPostForm
def post_list(request):
    post_list = Post.objects.all()
    paginator=Paginator(post_list,3)
    page_number=request.GET.get('page',1)

    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/post_list.html', {'posts':posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, publish__year=year,publish__month=month,publish__day=day)
    return render(request, 'blog/post/detail.html', {"post": post})

def post_share(request,post_id):
    posts=get_object_or_404(Post,id=post_id)
    sent=False
    form = EmailPostForm()

    if request.method=='POST':
        form=EmailPostForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            post_uri=request.build_absolute_uri(posts.get_absolute_path())
            subject = f"{cd['name']} recommends you to read"\
                      f"{posts.title}"
            message = f"Read {posts.title} at {post_uri}\n\n"\
                      f"{cd['name']}\'s comments {cd['comments']}"
            send_mail(subject,message,'dansobaahkenneth@gmail.com',[cd['to']])
            sent = True
        else:
            form
    return render(request,'blog/post/share.html',{"posts":posts,"form":form,"sent":sent})