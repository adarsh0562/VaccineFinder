from django import forms

class loginForm(forms.Form):
    name = forms.CharField(label='Enter name',widget=forms.TextInput(attrs={'class':'input'}),error_messages={'required':'Name is required'})
    mobile = forms.IntegerField(label='Enter Mobile',widget=forms.NumberInput(attrs={'class':'input'}),error_messages={'required':'Mobile no is required'})
    otp = forms.IntegerField(label='Enter OTP',widget=forms.NumberInput(attrs={'class':'input'}),error_messages={'required':'Otp is required'})

