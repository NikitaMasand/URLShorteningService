from django.core.management.base import BaseCommand, CommandError
from shortener.models import KirrURL


class Command(BaseCommand):
    help = 'Refreshes all KirrURL shortcodes'

    def add_arguments(self, parser):
        # -- before items makes it optional
        parser.add_argument('--items', type=int)
        #items: number of shortcodes that we want to refresh

    def handle(self, *args, **options):
        return KirrURL.objects.refresh_shortcodes(items=options['items'])
