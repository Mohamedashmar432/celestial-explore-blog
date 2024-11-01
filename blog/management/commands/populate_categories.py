from typing import Any
from blog.models import Post, Category
from django.core.management.base import BaseCommand
import random

class Command(BaseCommand):
    help = "This commands inserts category data"

    def handle(self, *args: Any, **options: Any):
        # Delete existing data 
        Category.objects.all().delete()
        
        categories = [ "Astronomy", "Cosmology","Planetary Science","Space Exploration", "Astrobiology", "Galaxies and Nebulae","Black Holes and Dark Matter","Space Technology and Innovation", "Exoplanets and Habitable Worlds", "Rocket Science and Spacecraft"]
      

        for category_name in categories:
            Category.objects.create(name = category_name)

        self.stdout.write(self.style.SUCCESS("Completed inserting Data!")) 