from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your models here.
class Worker(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    salary = models.IntegerField(default=0)
    note = models.TextField(blank=True, null=True)
    photo = models.ImageField(blank=True, null=True, upload_to='workers_photo/')

    def __str__(self):
        return f'({self.id}) Worker: {self.name}, {self.salary} $'


class Resume(models.Model):
    # worker = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name='resumes')  # worker.resumes
    worker = models.OneToOneField(Worker, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return f'Resume {self.worker.name}'


class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    text = models.TextField(null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.recipient.username}: {self.text[:20]}'
