from django import forms

class CommentForm(forms.Form):
	name = forms.CharField(max_length = 30, label='Name', error_messages={'required': 'Please enter your name'}, widget=forms.TextInput(attrs={'class':'form-control'}))
	email = forms.EmailField(label='Email', error_messages={'required': 'Please enter valid email'}, widget=forms.TextInput(attrs={'class':'form-control'}))
	website = forms.URLField(label='Website', max_length = 30, required = False, initial='http://', widget=forms.TextInput(attrs={'class':'form-control'}))
	comment = forms.CharField(label='Comment', widget=forms.Textarea(attrs={'class':'form-control'}), max_length = 100)

class ContactForm(forms.Form):
	name = forms.CharField(max_length = 30, error_messages={'required': 'Please enter your name'})
	email = forms.EmailField(error_messages={'required': 'Please enter valid email'})
	message = forms.CharField(widget=forms.Textarea, max_length = 100)

class LoginForm(forms.Form):
	username = forms.CharField(max_length = 20, error_messages={'required': 'Please enter username'})
	password = forms.CharField(max_length = 20, error_messages={'required': 'Please enter password'}, widget=forms.PasswordInput)