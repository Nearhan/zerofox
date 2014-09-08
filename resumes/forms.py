from django import forms
from django.contrib.auth.models import User
from resumes.models import Resume, Job


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if not password == confirm_password:
            raise forms.ValidationError("passwords don't match!!")
        return self.cleaned_data

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ('username', 'password', 'confirm_password')


class ResumeModelForm(forms.ModelForm):

    class Meta:
        model = Resume
        exclude = ['user']
        fields = ('first_name', 'last_name', 'objective', 'email',
                  'phone_number')


class JobModelForm(forms.ModelForm):

    class Meta:
        model = Job
        exclude = ['resume']
        fields = ('company', 'title', 'location', 'summary', 'start_date',
                  'end_date')
