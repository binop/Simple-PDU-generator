from pdugen.models import SMSData
from django import forms


class SMSDataForm(forms.ModelForm):
    DRAFT_NAME = forms.CharField(max_length=20, required=False)
    save_draft_flag = forms.BooleanField(required=False)

    class Meta:
        model = SMSData
