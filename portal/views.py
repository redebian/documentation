from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.views.generic.simple import direct_to_template

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.api import users
from google.appengine.api import mail

from portal.models import *
from portal.form import *

import datetime
from datetime import datetime

from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.base import RedirectView

class BaseAppListView(ListView):
    """ Base view for application lists on the main page. """
    
    template_name = "base.html"
    context_object_name = 'applications'
    
    def get_queryset(self):
        """
        Should be redefined by subclasses. 
        """
        return Categories.objects.all()

    def get_context_data(self, **kwargs):

        context = super(BaseAppListView, self).get_context_data(**kwargs)
        context['bloglink'] = Blogrol.objects.all()
        context['recent'] = Tutorial.objects.all().order_by('-created')[:6]
        return context


class ListTutorial(BaseAppListView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):

        context = super(ListTutorial, self).get_context_data(**kwargs)
        context['tutor'] = Tutorial.objects.Masukan()
        return context


class ViewPost(BaseAppListView):

    model = Tutorial
    template_name = "viewpost.html"

    def get_context_data(self, **kwargs):

        context = super(ViewPost, self).get_context_data(**kwargs)

        context['query'] = Tutorial.objects.filter(id=int(self.kwargs['pk']))
        context['coments'] = Comment.objects.filter(tutorial = int(self.kwargs['pk']))
        context['coment_form'] = CommentForm()

        return context

class CategoryList(BaseAppListView):

    def get_context_data(self, **kwargs):

        context = super(CategoryList, self).get_context_data(**kwargs)
        context['tutor'] = Tutorial.objects.filter(categories=int(self.kwargs['pk']))
        
        return context

class SearchView(BaseAppListView):

    def get_context_data(self, **kwargs):

        context = super(SearchView, self).get_context_data(**kwargs)
        keywords = self.request.GET.get("keyword", "")
        context['tutor'] = Tutorial.objects.filter(title__icontains=keywords)

        return context

class PostView(BaseAppListView):

    def get_context_data(self, **kwargs):

        context = super(PostView, self).get_context_data(**kwargs)
        context['tutor'] = self.request.GET.get("name","")

        return context

        


