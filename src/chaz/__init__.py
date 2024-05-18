"""
Package for chaz.
"""
from gevent import monkey
monkey.patch_all()

from .celery import the_thing 

__all__ = (
    'the_thing',
)
