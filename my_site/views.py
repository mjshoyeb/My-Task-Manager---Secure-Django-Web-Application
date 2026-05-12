from django.shortcuts import render

def home(request):
    # আমরা একটি ডিকশনারি তৈরি করছি যাতে আমাদের ডেটা থাকবে
    context = {
        'name': 'MJ Shoyeb',
        'profession': 'Python Developer',
        'current_year': 2026,
        'is_expert': True,  # এটি একটি Boolean ভ্যালু
        'skills': ['Python', 'Django', 'HTML', 'CSS', 'Git' ,'Java', 'JavaScript' , 'C++'] # এটি একটি লিস্ট
    }
    return render(request, 'index.html', context) 
    
def about(request):
    context = {
        'my_self' : 'I am Rahul. I live in Delhi. I am a 7 years old boy. I have a sister, Arya. My family consists of four people - me, my sister, and my parents. We live very happily. I am in 2nd standard in City World School. My sister and I study in the same school. We go to school every day. I love my school. I have many friends in my school. I love my teachers and they teach us very kindly. My favourite subject is English. '
    }
    return render(request, 'about.html',context) 

def contact(request):
    context = {
        'email': 'contact@example.com',
        'phone': '+1234567890'
    }
    return render(request, 'contact.html', context)

