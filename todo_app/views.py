from multiprocessing import context

from django.shortcuts import render, redirect # redirect ইম্পোর্ট করলাম
from .models import Task
from .forms import TaskForm # আমাদের বানানো ফর্মটি আনলাম
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
    search_input = request.GET.get('search-area') or ''
    tasks = Task.objects.filter(user=request.user) # শুধু বর্তমান ইউজারের টাস্ক
    
    if search_input:
        tasks = tasks.filter(title__icontains=search_input)
        
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user # মালিকানা সেট করা
            task.save()
            return redirect('home')
    else:
        form = TaskForm()
        
    context = {
        'tasks': tasks,
        'form': form,
        'search_input': search_input,
    }
    return render(request, 'index.html', context)
    

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id) # আইডি দিয়ে নির্দিষ্ট টাস্কটি খুঁজে বের করা
    task.delete() # টাস্কটি ডাটাবেস থেকে মুছে ফেলা
    return redirect('home') # আবার হোম পেজে ফিরে যাওয়া

def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_completed = True # স্ট্যাটাস বদলে দেওয়া
    task.save() # পরিবর্তনটি সেভ করা
    return redirect('home')

def edit_task(request, task_id):
    task = Task.objects.get(id=task_id) # নির্দিষ্ট টাস্কটি খুঁজে বের করা
    
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task) # পুরনো ডেটা (instance) সহ নতুন ডেটা ধরা
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm(instance=task) # শুধু পুরনো ডেটা দিয়ে ফরমটি পূর্ণ করা
        
    return render(request, 'edit_task.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

class RegisterPage(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)