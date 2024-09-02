from django import forms  

from .models import Task , TODO 



class CategoryForm(forms.ModelForm):
    class Meta:
        model = TODO
        fields = ['name' , 'description' , 'Deadline']

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'Deadline': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }






class TaskForm(forms.ModelForm):

    class Meta:
        model=Task 
        fields = ['title' , 'description' , 'status' ,'priority' ,  'due_date' , 'TODO']
    

        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.NumberInput(attrs={'class': 'form-control'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }