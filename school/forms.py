from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django import forms
from .models import School 


class SchoolInfo(forms.ModelForm):
	schoolname = forms.CharField(label="School name",  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'School name'}), required=False)
	telephone = forms.CharField(label="Telephone",  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'telephone/ phone'}), required=False)
	schoolemail = forms.CharField(label="School Email",  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'school email'}), required=False)
	schooladdress = forms.CharField(label="School Address",  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'full address'}), required=False)
	postal_address = forms.CharField(label="Postal Address",  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Postal address'}), required=False)
	website = forms.CharField(label="Website",  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'website'}), required=False)
	slogan = forms.CharField(label="Slogan",  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'slogan'}), required=False)
	type_of_school = forms.ChoiceField(
        label="School Type",
        choices=School.SCHOOL_SECTOR,
        widget=forms.Select(attrs={'class': 'form-input'}),
        required=True
    )
	umalusi = forms.ChoiceField(
        label="Umalusi",
        choices=School.UMALUSI,
        widget=forms.RadioSelect(attrs={'class': 'form-input'}),
        required=True
    )
	provinc = forms.ChoiceField(
        label="Province",
        choices=School.PROVINCE,
        widget=forms.Select(attrs={'class': 'input'}),
        required=True
    )
	district = forms.ChoiceField(
        label="District",
        choices=School.DISTRICT,
        widget=forms.Select(attrs={'class': 'form-input'}),
        required=True
    )
	circuit = forms.ChoiceField(
        label="Circuit",
        choices=School.CIRCUIT,
        widget=forms.Select(attrs={'class': 'form-input'}),
        required=True
    )
	curriculum = forms.ChoiceField(
        label="Curriculum",
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
        label="Section 21",
        choices=School.SECTION,
        widget=forms.Select(attrs={'class': 'form-input'}),
        required=True
    )
	school_fees = forms.CharField(label="School Fees",  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address1'}), required=False)
	quintile_Level = forms.ChoiceField(
        label="Quintile",
        choices=School.QUANTILE,
        widget=forms.Select(attrs={'class': 'form-input'}),
        required=True
    )
	image = forms.ImageField(
    label="Image",
    widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'Upload Image'}),
    required=False
    )
	image1 = forms.ImageField(
    label="Image",
    widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'Upload Image'}),
    required=False
    )
	
    
	history = forms.CharField(label="History",  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'school history'}), required=False)
	mission = forms.CharField(label="Mission",  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'school mission'}), required=False)

	class Meta:
		model = School
		fields = ('__all__')
		exclude = ('user',)