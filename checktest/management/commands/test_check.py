
from django.core.management.base import BaseCommand
from checktest.models import testmodel



class Command(BaseCommand):
    help = "test model check"

    def add_arguments(self, parser):
        parser.add_argument("--path", type=str)

    def handle(self, *args, **options):
        testmodel.objects.create(good='this is great')
        

        print("Successfully done")
