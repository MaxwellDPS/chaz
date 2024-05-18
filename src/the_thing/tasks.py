"""
 _________________ 
< Multitasking yo >
 ----------------- 
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
"""
from celery import shared_task

@shared_task(bind=True)
def a_task(self) -> None:
    """
    Celery Task to do something
    """
    # DO A THING
