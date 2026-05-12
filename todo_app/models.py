from django.db import models
from django.contrib.auth.models import User

class Task(models.Model): # আমাদের টাস্ক মডেল, যা টাস্কের তথ্য সংরক্ষণ করবে
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) # এই লাইনটি যোগ করো
    title = models.CharField(max_length=200) # টাস্কের নাম
    description = models.TextField()           # বিস্তারিত
    category = models.CharField(max_length=20, default='General') # টাস্কের ক্যাটাগরি, ডিফল্ট মান 'General'
    is_completed = models.BooleanField(default=False) # সম্পন্ন হয়েছে কি না
    created_at = models.DateTimeField(auto_now_add=True) # তৈরির সময়

    def __str__(self):
        return self.title
