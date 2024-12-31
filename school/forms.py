from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django import forms
from .models import School 


class SchoolInfo(forms.ModelForm):
	schoolname = forms.CharField(label="School name",  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone number'}), required=False)
	telephone = forms.CharField(label="Address 1",  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address1'}), required=False)
	schoolemail = forms.CharField(label="address 2",  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address2'}), required=False)
	schooladdress = forms.CharField(label="City",  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'city'}), required=False)
	postal_address = forms.CharField(label="Province",  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'province'}), required=False)
	website = forms.CharField(label="zipcode",  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'zipcode'}), required=False)
	slogan = forms.CharField(label="Country",  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'country'}), required=False)
	type_of_school = forms.ChoiceField(
        label="Register as?",
        choices=School.SCHOOL_SECTOR,
        widget=forms.Select(attrs={'class': 'form-input'}),
        required=True
    )
	umalusi = forms.ChoiceField(
        label="Register as?",
        choices=School.UMALUSI,
        widget=forms.Select(attrs={'class': 'form-input'}),
        required=True
    )
	provinc = forms.ChoiceField(
        label="Register as?",
        choices=School.PROVINCE,
        widget=forms.Select(attrs={'class': 'input'}),
        required=True
    )
	district = forms.ChoiceField(
        label="Register as?",
        choices=School.DISTRICT,
        widget=forms.Select(attrs={'class': 'form-input'}),
        required=True
    )
	circuit = forms.ChoiceField(
        label="Register as?",
        choices=School.CIRCUIT,
        widget=forms.Select(attrs={'class': 'form-input'}),
        required=True
    )
	curriculum = forms.ChoiceField(
        label="Register as?",
        choices=School.CURRICULUM,
        widget=forms.Select(attrs={'class': 'form-input'}),
        required=True
    )
	grade_levels = forms.CharField(label="Province",  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'province'}), required=False)
	accreditation = forms.CharField(label="School name",  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone number'}), required=False)
	local_municipality = forms.CharField(label="Address 1",  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address1'}), required=False)
	urban_rural = forms.CharField(label="Address 1",  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address1'}), required=False)
	ward_id = forms.CharField(label="Address 1",  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address1'}), required=False)
	Eei_district = forms.CharField(label="Address 1",  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address1'}), required=False)
	emis_number = forms.CharField(label="Address 1",  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address1'}), required=False)
	examination_number = forms.CharField(label="Address 1",  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address1'}), required=False)
	examination_centre = forms.CharField(label="Address 1",  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address1'}), required=False)
	persal_paypoint_number = forms.CharField(label="Address 1",  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address1'}), required=False)
	persal_component_number = forms.CharField(label="Address 1",  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address1'}), required=False)
	name_of_principal = forms.CharField(label="Address 1",  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address1'}), required=False)
	number_of_teachers = forms.CharField(label="Address 1",  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address1'}), required=False)
	number_of_learners = forms.CharField(label="Address 1",  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address1'}), required=False)
	section_21 = forms.ChoiceField(
        label="Register as?",
        choices=School.SECTION,
        widget=forms.Select(attrs={'class': 'form-input'}),
        required=True
    )
	school_fees = forms.CharField(label="Address 1",  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address1'}), required=False)
	quintile_Level = forms.ChoiceField(
        label="Register as?",
        choices=School.QUANTILE,
        widget=forms.Select(attrs={'class': 'form-input'}),
        required=True
    )
	history = forms.CharField(label="Address 1",  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address1'}), required=False)
	mission = forms.CharField(label="Address 1",  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address1'}), required=False)

	class Meta:
		model = School
		fields = ('__all__')