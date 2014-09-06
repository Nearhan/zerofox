from django.views.generic import TemplateView, FormView, CreateView, UpdateView
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import login


from resumes.forms import UserForm, ResumeModelForm
from resumes.models import Resume


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

    def form_valid(self, form):
        self.object = form.save()
        self.create_resume(user=self.object)
        return HttpResponseRedirect(self.get_success_url())

    def create_resume(self, user=None):
        resume = Resume(user=user)
        resume.save()
        return True


class ResumeView(FormView):

    template_name = 'resume.html'
    context_object_name = 'resume'
    form_class = ResumeModelForm

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(request=request)
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_object(self, request=None):
        print 'here i am ', request.user
        resume = Resume.objects.get(user=request.user.id)
        return resume



class JobView(TemplateView):
    pass
