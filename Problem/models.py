from django.db import models
from accounts.models import User
from exams.models import Assessment
class Question(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    score = models.PositiveIntegerField()
    assessment = models.ForeignKey(Assessment,on_delete=models.CASCADE)
    sample_input = models.TextField(null=True, blank=True)
    sample_output = models.TextField()
    question_no=models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):

        last_object=Question.objects.filter(assessment=self.assessment).last()
        if last_object:
            self.question_no=last_object.question_no+1
        else:
            self.question_no=1
        return super().save(*args,**kwargs)