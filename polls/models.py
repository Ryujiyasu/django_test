from django.db import models




class Question(models.Model):
    class Meta:
        verbose_name_plural="質問"

    question_text = models.CharField(max_length=200)
    question_text2 = models.CharField(max_length=200)
    question_text3 = models.CharField(max_length=200)
    question_text44 = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text



class Choice(models.Model):
    class Meta:
        verbose_name_plural="選択肢"
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text