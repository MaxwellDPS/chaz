from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Just Chaz Things"

    def add_arguments(self, parser):
        parser.add_argument('-f',"--force", action='store_true')

    def handle(self, *args, **options):
        force:bool = options["force"]
