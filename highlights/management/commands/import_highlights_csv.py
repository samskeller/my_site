from django.core.management.base import BaseCommand, CommandError
import csv

from highlights.models import Book, Highlight

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('csv', nargs='+', type=str)

    def handle(self, *args, **options):
        with open(options['csv'][0], 'r' ) as opened_file:
            reader = csv.DictReader(opened_file)
            for line in reader:
                title = line['TITLE']
                author = line['AUTHOR']
                text = line['TEXT']
                try:
                    book = Book.objects.get(title=title, author=author)
                except Book.DoesNotExist:
                    print('Can\'t find book {} by {}'.format(title, author))
                    continue
                highlight = Highlight(book=book, text=text)
                highlight.save()
