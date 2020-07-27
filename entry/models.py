from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class MstPlace(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Entry(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    entry_date = models.DateTimeField('入室日時', default=timezone.now())
    entry_place = models.ForeignKey(MstPlace, verbose_name="入室場所", on_delete=models.CASCADE, related_name="entry_place", null=True, blank=True)
    exit_date = models.DateTimeField('退室日時', null=True, blank=True)
    exit_place = models.ForeignKey(MstPlace, verbose_name="退室場所", on_delete=models.CASCADE, related_name="exit_place", null=True, blank=True)
    update_date = models.DateTimeField('更新時間', default=timezone.now())

    def __str__(self):
        return "入室場所：" + str(self.entry_place) + "、退室場所：" + str(self.exit_place)
