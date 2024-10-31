from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=255)  # Змінено max_length на 255
    description = models.TextField()
    completed = models.BooleanField(default=False)  # Додано поле для статусу завершення
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # Власник завдання

    def __str__(self):
        return self.title

class SubTask(models.Model):
    title = models.CharField(max_length=255)  # Змінено max_length на 255
    description = models.TextField()
    completed = models.BooleanField(default=False)  # Додано поле для статусу завершення
    task = models.ForeignKey(Task, related_name='subtasks', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # Власник підзавдання

    def __str__(self):
        return self.title
