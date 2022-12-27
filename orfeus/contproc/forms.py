from crispy_forms.helper import FormHelper
from django import forms
from .models import busCoordinates

# forms:

class selectMapForm(forms.Form):
    maps = forms.ModelChoiceField(
        queryset=busCoordinates.objects.all().order_by('fname'),
        widget=forms.Select(attrs={'class':'select form-control'})
    )
    # helper = FormHelper()
    # helper.form_class = 'form-horizontal'
    # # helper.form_show_labels = False
    # # helper.field_class = 'select form-control'
    # helper.label_class = 'col-3 text-end'
    # helper.field_class = 'col'

# class selectMapForm(forms.ModelForm):
#     class Meta:
#         model = busCoordinates
#         fields = ['fname']
