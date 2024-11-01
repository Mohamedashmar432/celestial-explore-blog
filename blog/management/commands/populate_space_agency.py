from typing import Any
from blog.models import  space_agency
from django.core.management.base import BaseCommand
import random

class Command(BaseCommand):
    help = "This commands inserts category data"

    def handle(self, *args: Any, **options: Any):
        # Delete existing data 
        space_agency.objects.all().delete()
        
        space_agencies = [
          "NASA (National Aeronautics and Space Administration, USA)",
          "ESA (European Space Agency)",
          "Roscosmos (Russian Federal Space Agency)",
          "CNSA (China National Space Administration)",
          "ISRO (Indian Space Research Organisation)",
          "JAXA (Japan Aerospace Exploration Agency)",
          "DLR (German Aerospace Center)",
          "CSA (Canadian Space Agency)",
          "UKSA (United Kingdom Space Agency)",
          "CNES (National Centre for Space Studies, France)"
         ]

      

        for space_agents in space_agencies:
            space_agency.objects.create(name = space_agents)

        self.stdout.write(self.style.SUCCESS("Completed inserting Data!")) 
    