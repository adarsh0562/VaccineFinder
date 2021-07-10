from django import forms

class loginForm(forms.Form):
    name = forms.CharField(label='Enter name',widget=forms.TextInput(attrs={'class':'input'}),error_messages={'required':'Name is required'})
    mobile = forms.IntegerField(label='Enter Mobile',widget=forms.NumberInput(attrs={'class':'input'}),error_messages={'required':'Mobile no is required'})
    otp = forms.IntegerField(label='Enter OTP',widget=forms.NumberInput(attrs={'class':'input'}),error_messages={'required':'Otp is required'})

    def clean(self):
        name = self.cleaned_data.get('name')
        mobile = self.cleaned_data.get('mobile')
        otp = self.cleaned_data.get('otp')
        if len(str(mobile)) != 10:
            self._errors['mobile'] = self.error_class([
                'Invali Mobile'])
        if len(str(otp)) != 6:
            self._errors['otp'] = self.error_class([
                'Invalid Otp'])
        return self.cleaned_data