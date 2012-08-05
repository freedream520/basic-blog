from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from forms import PostForm
from models import Post

@login_required
def new_post(request):
    form = PostForm()
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        
        if form.is_valid():
            form.save(request.user)
            return HttpResponseRedirect(reverse('blog.views.list_posts'))
            
    return render_to_response('blog/new_post.html',
            locals(), context_instance=RequestContext(request)
    )


def list_posts(request):
    posts = Post.objects.all()
    
    return render_to_response('blog/list_posts.html',
            locals(), context_instance=RequestContext(request)
    )
    
def display_post(request, post_url):
    p = get_object_or_404(Post, url=post_url)
    return render_to_response('blog/display_post.html', {'post': p}, 
                                  context_instance=RequestContext(request))