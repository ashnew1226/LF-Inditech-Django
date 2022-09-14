from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import ContactForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
 # Create your views here.
def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, "Your response has been saved successfully.")
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            form.save()
            html_content = render_to_string('home/email_template.html',
                                            {'name': name, 'email': email, 'subject': subject,
                                             'message': message})
            text_content = strip_tags(html_content)
            msg = EmailMultiAlternatives(subject, text_content, 'ashnew1226@gmail.com', ['ashnew1226@gmail.com','halsikaramit@gmail.com'])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
        else:
            messages.error(request, "Incorrect Details")
        return render(request, 'home/index.html', {'form': form})
    else:
        form = ContactForm()
        return render(request, 'home/index.html', {'form': form})
