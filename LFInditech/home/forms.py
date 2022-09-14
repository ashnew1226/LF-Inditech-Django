from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}), required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}),required=True)
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Subject'}), required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message', "rows":4, "cols":30}), required=True)
    class Meta:
        model= Contact
        fields= ["name", "email", "subject","message"]
    # widgets = {
    #         'message': forms.Textarea(attrs={"rows":4, "cols":30})
            
    #     }
    # def clean(self):
    #     cleaned_data = super(ContactForm, self).clean()
    #     name = cleaned_data['name']
    #     email = cleaned_data['email']
    #     subject = cleaned_data['subject']
    #     message = cleaned_data['message']
    #     if ContactForm.objects.filter(name==''):
    #         raise forms.ValidationError({"name":"name is required"})

    #     elif ContactForm.objects.filter(email==''):
    #         raise forms.ValidationError({"email":"email is required"})
        
    #     elif ContactForm.objects.filter(subject==''):
    #         raise forms.ValidationError({"subject":"subject is required"})

    #     elif ContactForm.objects.filter(message==''):
    #         raise forms.ValidationError({"message":"message is required"})