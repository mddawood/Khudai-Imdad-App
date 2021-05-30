from django import forms
from . models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['pic', 'name', 'designation', 'twitter', 'facebook', 'linkedin']

    def __init__(self, *args, **kwargs):
        super(MemberForm, self).__init__(*args, **kwargs)
        self.fields['twitter'].required = False
        self.fields['facebook'].required = False
        self.fields['linkedin'].required = False
