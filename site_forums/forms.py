from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import LoginUser, Claim

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))


	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

	def clean_username(self):
		username = self.cleaned_data.get('username')
		if username in []:
			raise forms.ValidationError("This username is not allowed!")
		return username

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

class LoginForm(forms.ModelForm):
	username = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Username", "class":"form-control"}), label="")
	password = forms.CharField(required=True, widget=forms.widgets.PasswordInput(attrs={"placeholder":"Password", "class":"form-control"}), label="")

	class Meta:
		model = LoginUser
		exclude = ("user",)

class CreateClaim(forms.ModelForm):
	claim_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Name of the claim", "class":"form-control"}), label="")
	claimed_for = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Country claimed for", "class":"form-control"}), label="")
	claim_gen_loc = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"The general location of the claim", "class":"form-control"}), label="")
	claim_desc = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={"placeholder":"A short description of what the claim is like", "class":"form-control"}), label="")

	class Meta:
		model = Claim
		exclude = ("username",)