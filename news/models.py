from autoslug import AutoSlugField
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError
from django.db import models
from django.template.loader import render_to_string


class Membership(models.Model):
    """Application objects link Users to :class:`Event` objects and provide additional
    information"""

    class Meta:
        unique_together = (('user', 'team'),)

    user = models.ForeignKey('account.Eestecer', editable=False)
    team = models.ForeignKey('teams.Team', editable=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    privileged = models.BooleanField(default=False)
    board = models.BooleanField(default=False)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.privileged:
            self.user.is_staff = True
            self.user.save()
            self.user.groups.add(Group.objects.get(name='Local Admins'))

    def __unicode__(self):
        return self.user.get_full_name()


class Entry(models.Model):
    class Meta:
        verbose_name_plural = "entries"

    author = models.ManyToManyField('teams.Team')
    """ The :class:`Members <teams.models.Team>` authoring the news"""
    headline = models.CharField(max_length=50, unique=True)
    """ The headline"""
    slug = AutoSlugField(populate_from='headline')
    content = models.TextField()
    """The Content of the message"""
    pub_date = models.DateTimeField(auto_now_add=True)
    """ The publication date"""
    entry_image = models.ImageField(upload_to="entryimages")
    """ Optionally, an image to add"""

    def as_html(self):
        return render_to_string('news/entry.html', {'object': self})

    def __unicode__(self):
        return self.headline
    def clean(self):
        if not len(self.headline.strip()):
            raise ValidationError("Headline may not be empty.")

# Create your models here.
