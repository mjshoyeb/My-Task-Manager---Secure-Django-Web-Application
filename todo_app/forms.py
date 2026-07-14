# forms.py (অথবা যেখানে আপনার TaskForm ক্লাসটি ডিফাইন করা আছে)
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'category', 'description', 'due_date'] # আপনার প্রোজেক্টের ফিল্ডের সাথে মিলিয়ে নিন
        
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter task title...',
                'class': 'w-full bg-slate-950/50 border border-slate-800 focus:border-emerald-500/60 rounded-xl px-4 py-3 text-sm text-white focus:outline-none focus:ring-1 focus:ring-emerald-500/30 transition-all duration-200'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Write detailed description or notes here...',
                'rows': 4,
                'class': 'w-full bg-slate-950/50 border border-slate-800 focus:border-emerald-500/60 rounded-xl px-4 py-3 text-sm text-white focus:outline-none focus:ring-1 focus:ring-emerald-500/30 transition-all duration-200'
            }),
            'category': forms.TextInput(attrs={
                'placeholder': 'Enter category (e.g. Work, Sports, Personal)...',
                'class': 'w-full bg-slate-950/50 border border-slate-800 focus:border-emerald-500/60 rounded-xl px-4 py-3 text-sm text-white focus:outline-none focus:ring-1 focus:ring-emerald-500/30 transition-all duration-200'
            }),
        }