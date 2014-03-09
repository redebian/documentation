from django import forms

class CommentForm(forms.Form):
	name = forms.CharField(max_length = 30, error_messages={'required': 'Please enter your name'})
	email = forms.EmailField(error_messages={'required': 'Please enter valid email'})
	website = forms.URLField(max_length = 30, required = False, initial='http://')
	comment = forms.CharField(widget=forms.Textarea, max_length = 100)

class ContactForm(forms.Form):
	name = forms.CharField(max_length = 30, error_messages={'required': 'Please enter your name'})
	email = forms.EmailField(error_messages={'required': 'Please enter valid email'})
	message = forms.CharField(widget=forms.Textarea, max_length = 100)

class LoginForm(forms.Form):
	username = forms.CharField(max_length = 20, error_messages={'required': 'Please enter username'})
	password = forms.CharField(max_length = 20, error_messages={'required': 'Please enter password'}, widget=forms.PasswordInput)