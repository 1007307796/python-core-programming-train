from django.shortcuts import render
from blog.models import BlogPost,BlogPostForm
from datetime import datetime
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
# Create your views here.


class HomePageView(TemplateView):

    template_name = 'archive.html'
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['posts']=BlogPost.objects.all().order_by('-timestamp')[:5]
        context['form']=BlogPostForm()
        return context
def archive(request):
    posts = BlogPost.objects.all().order_by('-timestamp')[:10]
    context = {'posts':posts,'form':BlogPostForm()}
    return render(request,'archive.html',context)

def create_blogpost(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.timestamp=datetime.now()
            post.save()
    return HttpResponseRedirect('/blog/')