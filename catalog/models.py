from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError

import re

# Create your models here.

def validate_asset_name(value):
    """ Custom validator """
    if re.match(r'^[A-Za-z0-9]+[A-Za-z0-9_-]*', value):
       if len(value) < 4:
           raise ValidationError(u'%s is not a valid value for title.' % value)
    else:
        raise ValidationError(u'%s is not a valid value for title. It should start with apla numeric characters' % value)


class AssetClass(models.Model):
    ASSET_CLASS_CHOICES = (('do', 'dove'), ('r', 'rapideye'), ('di', 'dish'), ('y', 'yagi'))
    acclass = models.CharField(max_length=15, primary_key=True, choices=ASSET_CLASS_CHOICES, default='do')
    acdetails = models.CharField(max_length=35)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return self.acclass

class Asset(models.Model):
    ASSET_TYPE_CHOICES = (('S','satellite'), ('A','antenna'))

    aname = models.CharField(max_length = 64, primary_key=True, validators=[validate_asset_name])
    atype = models.CharField(max_length=15, choices=ASSET_TYPE_CHOICES, default='S')
    aclass = models.ForeignKey(AssetClass, related_name='aclass')

    def save(self, *args, **kwargs):
        if (self.atype == "S"):
            if str(self.aclass) == 'dove' or str(self.aclass) == 'rapideye':
               super(Asset, self).save(*args, **kwargs)
            else:
                raise Exception, "Satellite object types can have only dove or rapideye as there class %s %s %s"%(args, kwargs, self.aclass)

        if(self.atype == "A"):
            if str(self.aclass) == 'dish' or str(self.aclass) == 'yagi':
                super(Asset, self).save(*args, **kwargs)
            else:
                raise Exception, "Antenna object types can have only dish or yagi as there class"

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return self.aname