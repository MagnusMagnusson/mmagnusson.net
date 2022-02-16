from django import forms

class ContactMeForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    your_email = forms.EmailField(label='Your email', max_length=100)
    message_title = forms.CharField(label='Message Title', max_length=100)
    your_message = forms.CharField(label='Your Message', max_length=1024, widget=forms.Textarea)
    my_name = forms.CharField(label='Human test: Please type in my given name.', max_length=100)