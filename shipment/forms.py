from django import forms

from .models import Shipment, Package

class ShipmentCreateForm(forms.ModelForm):
    # comment = forms.CharField(
    #      widget=forms.Textarea(attrs={'rows':4, 'cols':15}),)

    class Meta:
        model = Shipment
        fields = '__all__'
        exclude = ['created', 'tracking_number']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['comment'].widget = forms.Textarea(attrs={'rows':4, 'cols':15})

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class ShipmentUpdateForm(forms.ModelForm):
   
    class Meta:
        model = Shipment
        fields = '__all__'
        exclude = ['created', 'tracking_number']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['comment'].widget = forms.Textarea(attrs={'rows':4, 'cols':15})

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class PackageCreateForm(forms.ModelForm):
    # comment = forms.CharField(
    #      widget=forms.Textarea(attrs={'rows':4, 'cols':15}),)

    class Meta:
        model = Package
        fields = '__all__'
        exclude = ['created', 'tracking_number']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['comment'].widget = forms.Textarea(attrs={'rows':4, 'cols':15})

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})



class PackageUpdateForm(forms.ModelForm):
   
    class Meta:
        model = Package
        fields = '__all__'
        exclude = ['created', 'tracking_number']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['comment'].widget = forms.Textarea(attrs={'rows':4, 'cols':15})

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})