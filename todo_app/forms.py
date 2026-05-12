from django import forms
from .models import Task

class TaskForm(forms.ModelForm): # আমরা ModelForm ব্যবহার করছি কারণ আমাদের ফর্মটি সরাসরি মডেল থেকে তৈরি হবে
    class Meta: #মেটা ক্লাসে (Configuration Class) আমরা আমাদের মডেল এবং ফিল্ড নির্ধারণ করছি
        model = Task # কোন মডেল থেকে ফর্ম তৈরি হবে তা নির্ধারণ করছি
        fields = ['title', 'description' , 'category'] # ফর্মে কোন কোন ফিল্ড থাকবে তা নির্ধারণ করছি
        
        # এখানে আমরা স্টাইল বা উইজেট যোগ করছি 
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'টাস্কের শিরোনাম লিখুন'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'বিস্তারিত লিখুন',
                'rows': 3  # বক্সের উচ্চতা কমিয়ে সুন্দর করা হলো
            }),
            'category': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'ক্যাটাগরি (যেমন: Work, Personal)'
            }),
        }
