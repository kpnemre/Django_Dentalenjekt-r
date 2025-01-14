from django import forms
from .models import ContactInfo
from crispy_forms.helper import FormHelper

class ContactForm(forms.ModelForm):
	class Meta:
		model = ContactInfo
		fields = ('name', 'email', 'message')
		
		
	# def __init__(self, *args, **kwargs):
	# 	super().__init__(*args, **kwargs)
	# 	self.fields['name'].widget.attrs['placeholder']= "İsminiz"
	# 	self.fields['name'].widget.attrs['class']= "form-control-sm"
	# 	self.fields['email'].widget.attrs['placeholder']= "Email adresiniz"
	# 	self.fields['email'].widget.attrs['class']= "form-control-sm"
	# 	self.fields['message'].widget.attrs['class']= "form-control-sm"
	# 	self.fields['message'].widget.attrs['placeholder']= "Mesajınız"
	# 	self.helper = FormHelper()
	# 	self.helper.form_show_labels = False 