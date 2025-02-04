from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'user'  

class Survey(models.Model):
    Question_1 = models.CharField(max_length=100)
    Question_2 = models.CharField(max_length=100)
    Question_3 = models.CharField(max_length=100)

    class Meta:
        db_table = 'survey'  

    def __str__(self):
        return f"Survey {self.id}: Q1={self.Question_1}, Q2={self.Question_2}, Q3={self.Question_3}"
