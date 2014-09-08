from django.views.generic import (
    TemplateView, FormView, ListView, CreateView, View, DetailView
)

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.http import HttpResponseRedirect

from resumes.forms import UserForm, ResumeModelForm, JobModelForm
from resumes.models import Resume, Job


class LoginRequiredMixin(object):

    @classmethod
    def as_view(cls):
        return login_required(super(LoginRequiredMixin, cls).as_view())


class WelcomeView(FormView):

    template_name = 'index.html'
    form_class = AuthenticationForm
    success_url = '/resume/'
    user_created = None

    def get(self, request, *args, **kwargs):
        if kwargs.get('created'):
            self.user_created = True
        return super(WelcomeView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super(WelcomeView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        if 'view' not in kwargs:
            kwargs['view'] = self
        if self.user_created:
            kwargs['user_created'] = self.user_created
        return kwargs


class CreateUserView(CreateView):
    """ This view handles creating a new user and createing a new Resume
    Instance """
    
    template_name = 'create_user.html'
    form_class = UserForm
    success_url = '/created=True'

    def create_resume(self, user=None):
        resume = Resume(user=user)
        resume.save()
        return True


class ResumeDetailView(LoginRequiredMixin, DetailView):

    template_name = 'resume.html'
    context_object_name = 'resume'

    def get_context_data(self, **kwargs):
        kwargs = super(ResumeDetailView, self).get_context_data(**kwargs)
        if hasattr(self.request.user, 'resume'):
            kwargs['jobs'] = self.object.job_set.all().order_by('-start_date')
        return kwargs

    def get_object(self):
        if hasattr(self.request.user, 'resume'):
            return self.request.user.resume
        return None


class ResumeCreateView(LoginRequiredMixin, CreateView):

    success_url = '/resume'
    template_name = 'create_resume.html'
    context_object_name = 'resume'
    form_class = ResumeModelForm

    def form_valid(self, form):
        kwargs = form.cleaned_data
        kwargs['user'] = self.request.user
        resume = Resume(**kwargs)
        self.object = resume.save()
        self.object = resume
        return HttpResponseRedirect(self.get_success_url())


class JobCreateView(LoginRequiredMixin, CreateView):

    success_url = '/resume'
    template_name = 'create_job.html'
    context_object_name = 'job'
    form_class = JobModelForm

    def form_valid(self, form):
        kwargs = form.cleaned_data
        kwargs['resume'] = self.request.user.resume
        job = Job(**kwargs)
        job.save()
        self.object = job
        return HttpResponseRedirect(self.get_success_url())


