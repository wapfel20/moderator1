import datetime

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe, SafeData, mark_for_escaping
from google_login.models import GoogleUserInfo

register = template.Library()


@register.filter
def dayssince(value):
    #"Returns number of days between today and value."
    today = datetime.date.today()
    diff  = today - value
    if diff.days >= 30:
        if int(diff.days/30)>1:
            return '%s months ago' % int(diff.days/30)
        else:
            return '%s month ago' % int(diff.days/30)
    if diff.days >= 7 and diff.days < 30:
        if int(diff.days/7)>1:
            return '%s weeks ago' % int(diff.days/7)
        else:
            return '%s week ago' % int(diff.days/7)
    if diff.days > 1 and diff.days < 7:
        return '%s days ago' % diff.days
    elif diff.days == 1:
        return 'yesterday'
    elif diff.days == 0:
        return 'today'
    else:
        # Date is in the future; return formatted date.
        return value.strftime("%B %d, %Y")



@register.filter
def subtract(startingValue, valueToSubtract):
    if (int(startingValue)- int(valueToSubtract)) < 0:
        return 0
    else:
        return int(startingValue)- int(valueToSubtract)
    

    
@register.filter
def possessivePronoun(name):
    if name[-1] == 's':
        return name+"'"
    else:
        return name+"'s"
    
    
@register.filter
def getAvatar(modUserList):
    if GoogleUserInfo.objects.filter(user=modUserList[0].user):
        return GoogleUserInfo.objects.get(user=modUserList[0].user).googleAvatar
    return False

@register.filter
def getName(modUserList):
    if GoogleUserInfo.objects.filter(user=modUserList[0].user):
        return GoogleUserInfo.objects.get(user=modUserList[0].user).user
    return False


