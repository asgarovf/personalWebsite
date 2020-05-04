from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
	full_name = forms.CharField(label="")
	email = forms.EmailField(label="")
	title = forms.CharField(label="")
	content = forms.CharField(label="", widget=forms.Textarea(attrs={'rows':10, 'cols': 28}))

	class Meta:
		model = Feedback
		fields = ['full_name', 'email', 'title','content']