from django import forms
from .models import CaseTitle, CaseContent


class CaseTitleForm(forms.ModelForm):

    class Meta:
        model = CaseTitle
        # user = request
        # fields = ('user', 'title',)
        fields = ('caseType', 'title')


class CaseContentForm(forms.ModelForm):
    class Meta:
        model = CaseContent
        fields = ('Contents',)
