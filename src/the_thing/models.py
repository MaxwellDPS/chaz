"""
 __________________________________ 
< ALL THAT JUNK IN THE ~TRUNK~ ORM >
 ---------------------------------- 
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
"""
import uuid

from django.db import models
from django.dispatch import receiver
from django.db.models import signals

class AThing(models.Model):
    """
    Tracked CIDRs
    """
    uuid = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4)

    def __str__(self):
        return str(self.uuid)

# pylint: disable=unused-argument
@receiver(signals.post_save, sender=AThing)
def _its_a_whole_thing(sender, instance: AThing, created: bool, **kwargs):
    """
    Validates the IP version and assigns it to the model
    """
    if created:
        signals.post_save.disconnect(_its_a_whole_thing, sender=AThing)
        # DO A THING
        signals.post_save.connect(_its_a_whole_thing, sender=AThing)
