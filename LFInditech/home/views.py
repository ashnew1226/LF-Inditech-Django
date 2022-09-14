from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import ContactForm
 # Create your views here.
def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, "Your response has been saved successfully.")
            form.save()
        #  return render(request, self.template_name)
        else:
            form = ContactForm()
            messages.error(request, "Please fill all the details.")

    return render(request, 'home/index.html',{'form':ContactForm})
