from django import forms

class ReviewForms(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=30)
    last_name = forms.CharField(label='Last Name', max_length=30)
    email = forms.EmailField(label='Email')
    review = forms.CharField(label='Please write your review here. Thanks.',widget= forms.Textarea(attrs={'class':'myform'}))