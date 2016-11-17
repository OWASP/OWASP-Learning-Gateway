from django.db import models
from django.contrib.auth.models import User


#class Course - these are full courses that are comprised of other elements
#class Chapter
#class Lesson

#tidbits - these are quick bite-sized learnings that will be under 1 minute (could just be links)

class Goal(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=255)
    progress = models.IntegerField(default=None)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.name

class Link(models.Model):
    goal = models.ForeignKey(Goal)
    sender = models.ForeignKey(User, related_name="sender")
    recipient = models.ForeignKey(User, related_name="recipient")
    link = models.URLField()
    clicked = models.DateTimeField(null=True, blank=True)
    learned = models.TextField(null=True, blank=True)
    completed = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.link

class Mentorship(models.Model):
    mentor = models.ForeignKey(User, related_name="mentor")
    mentee = models.ForeignKey(User, related_name="mentee")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.mentor + " mentoring " + mentee

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="userprofile")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def avatar(self, size=36):
        for account in self.user.socialaccount_set.all():
            if 'avatar_url' in account.extra_data:
                return account.extra_data['avatar_url']
            elif 'picture' in account.extra_data:
                return account.extra_data['picture']

        gravatar_url = "http://www.gravatar.com/avatar.php?"
        gravatar_url += urllib.urlencode({'gravatar_id': hashlib.md5(self.user.email.lower()).hexdigest(), 'default': 'retro', 'size': str(size)})
        return gravatar_url

    def avatar_large(self, size=200):
        return self.avatar(size=200)

    # def save(self, *args, **kwargs):
    #     if self.pk is None:
    #         action.send(self.user, verb='signed up')
    #         cache.clear()
    #     super(UserProfile, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.user.username



