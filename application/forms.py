from django import forms
from .models import AdmissionForm, Status


class Form(forms.ModelForm):
    status = forms.CharField(label="status",  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':"status"}), required=False)
    childname = forms.CharField(label="child name",  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':"child's name"}), required=False)
    childsurname = forms.CharField(label="child surname",  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':"child's surname"}), required=False)
    grade = forms.CharField(label="grade",  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':"grade"}), required=False)
    parentname = forms.CharField(label="parent name",  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':"parent name"}), required=False)
    class Meta:
        model = AdmissionForm
        fields = ('__all__')
        exclude = ('schoolname', 'user')




class UpdateStatus(forms.ModelForm):
	status = forms.ChoiceField(
        label="Registering As ?",
        choices=Status.APPLICATION_STATUS,
        widget=forms.Select(attrs={'class': 'form-input'}),
        required=True
    )
	class Meta:
		model = AdmissionForm
		fields = ( 'status',)