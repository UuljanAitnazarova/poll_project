from django.db import models


class Poll(models.Model):
    question = models.CharField(max_length=250, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question


class Choice(models.Model):
    option = models.CharField(max_length=300, null=False, blank=False)
    poll = models.ForeignKey('poll_app.Poll', related_name='choices', on_delete=models.CASCADE)

    def __str__(self):
        return self.option

