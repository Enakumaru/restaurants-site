from django.db.models import fields
from django.db.models.base import Model
from django.http import request
from django.shortcuts import render
from django.views.generic.base import TemplateView 
from django.views.generic import ListView 
from core.models import *
from django.views.generic import CreateView , UpdateView , DeleteView
from .forms import blogForm,EditblogForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import Http404, HttpResponseBadRequest, HttpResponseNotFound
# Create your views here.


class hello(ListView):
    queryset = blog.objects.all()
    template_name='blogs/test.html'
    fields='__all__'
class P_blog(CreateView,LoginRequiredMixin,):
    model=blog
    form_class= blogForm
    template_name= 'blogs/P-blog.html'
    print(form_class.errors)
    #fields='__all__'
    #def form_valid(self, form_class):
        #form_class.author = self.request.user
        #return super().form_valid(form_class)
    
class P_updateblog(UpdateView):
    model=blog
    form_class= EditblogForm
    template_name= 'blogs/P-updateblog.html'
    #fields=['title','header_image','title_tag','body','category','snippet',]
    
class deleteblog(DeleteView):
    model=blog
    template_name= 'blogs/deleteblog.html'
    success_url=reverse_lazy('blogs:testt')

def categoryview(request,cats):
    cattis=Category.objects.filter( name=cats).values_list('id', flat=True)
    if len(cattis)==0:
        return HttpResponseNotFound("does not exist")  
    else:
        product=blog.objects.filter(category=cattis[0])
        context={
            'products':product,
        }
        return render (request,'blogs/blog_catView.html',context)

def test(request):
    form=EditblogForm
    return render(request,'blogs/hh.html',context={'form':form})


#<div class="col-md-4">
       # <h4><label for="id_author" class="form-label text-warning">Author</label></h4>
       # {{form.author}}
      #</div> 