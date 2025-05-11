from django.db import models

class BusinessProfile(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class FAQ(models.Model):
    business = models.ForeignKey(BusinessProfile, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return f"Q: {self.question}"
