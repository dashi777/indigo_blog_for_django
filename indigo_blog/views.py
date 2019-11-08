from django.shortcuts import render,get_object_or_404
from .models import Post,Tag,Project
import markdown
# Create your views here.
def index(request):
    return render(request,'index.html') 

def blog_index(request):
    post_list = Post.objects.all().order_by('created_time')
    return render(request,'blog_index.html',context ={'post_list':post_list})

def project_index(request):
    project_list = Project.objects.all().order_by('created_time')
    return render(request,'project_index.html',context ={'project_list':project_list})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    #tag_list = Tag.objects.all()
    #tag_list = Tag.objects.filter(tags)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render(request, 'blog_post.html', context={'post': post,
                                                      })

def project_post(request,pk):
    project = get_object_or_404(Project, pk=pk)
    project.body = markdown.markdown(project.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render(request, 'project_post.html', context={'project': project,
                                                      })



