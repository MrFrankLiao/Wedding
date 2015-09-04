
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile
from member import choices
# Create your models here.

# class UserProfile(models):
class UserProfile(UserenaBaseProfile):
    user = models.OneToOneField(User, unique=True, verbose_name=_('user'), related_name='user_profile')
    nickname = models.CharField(max_length=30, verbose_name=u'暱稱', default='')
    sex = models.SmallIntegerField(choices=choices.SEX_CHOICES, verbose_name=u'性別', default=0)
    blood = models.SmallIntegerField(choices=choices.BLOOD_CHOICES, verbose_name=u'血型', default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    enable = models.BooleanField(u'啟用', default=True)

    def __unicode__(self):
        nickname = self.nickname or ''
        return nickname + ' (' + self.user.username + ')'

    class Meta:
        verbose_name = '會員基本資料'
        ordering = ['create_time']