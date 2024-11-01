from typing import Any
from blog.models import Post, Category
from django.core.management.base import BaseCommand
import random

class Command(BaseCommand):
    help = "This command inserts post data"

    def handle(self, *args: Any, **options: Any):
        # Delete existing data 
        Post.objects.all().delete()

        titles = [
            "Galactic Gazette: Latest News from the Cosmos",
            "Stellar Stories: Exploring the Universe Beyond Earth",
            "Cosmic Chronicles: Updates on Space Discoveries",
            "Beyond the Blue Planet: Space News and Insights",
            "Orbit Observations: Today’s Space Highlights",
            "Nebula Narratives: Stories from the Depths of Space",
            "Celestial Update: Your Guide to the Stars",
            "Space Spectrum: Breaking News in Astronomy",
            "Planet Pulse: Daily News from the Solar System",
            "Voyager’s Voice: Discovering New Frontiers",
            "Infinite Insights: The Wonders of Space Explained",
            "The Astronomer’s Journal: Reports from the Galaxy",
            "Space Odyssey: Tracking Humanity’s Exploration Beyond",
            "Starburst News: Highlights in Space Research",
            "The Cosmic Current: Latest in Space Science",
            "Universe Unveiled: News on Stars, Planets, and Beyond",
            "Beyond the Horizon: Space Breakthroughs and Discoveries",
            "Deep Space Dispatch: Reports from Outer Space"
        ]

        contents = [
            "Galactic Gazette: Latest News from the Cosmos — Dive into the Galactic Gazette for fresh updates...",
            "Stellar Stories: Exploring the Universe Beyond Earth — Stellar Stories captures humanity's quest...",
            "Cosmic Chronicles: Updates on Space Discoveries — Cosmic Chronicles brings the latest in space science...",
            "Beyond the Blue Planet: Space News and Insights — Beyond the Blue Planet offers readers engaging insights...",
            "Orbit Observations: Today’s Space Highlights — Orbit Observations is your source for quick, insightful...",
            "Starbound Signals: Breaking News from Deep Space — Starbound Signals provides breaking news...",
            "Celestial Navigator: Your Guide to Astronomy Events — Celestial Navigator offers a comprehensive guide...",
            "The Astrophile’s Almanac: Space Observations and Tips — The Astrophile’s Almanac is tailored for...",
            "Lunar Log: Updates on the Moon’s Mysteries — Lunar Log is dedicated to all things lunar! Our blog brings...",
            "Nebulae Notes: Stories from the Interstellar Medium — Nebulae Notes dives into the colorful, gaseous...",
            "Exoplanet Explorer: Discover Worlds Beyond Our Solar System — Exoplanet Explorer is dedicated to...",
            "The Comet Chronicles: Tracking Cosmic Wanderers — The Comet Chronicles tracks the journeys of comets...",
            "The Sunspot Report: Solar Activity and Its Effects — The Sunspot Report provides up-to-date...",
            "Black Hole Bulletin: News from the Darkest Corners of Space — The Black Hole Bulletin delves into one...",
            "Galaxy Gazetteer: Insights on Our Galaxy and Beyond — Galaxy Gazetteer explores the intricacies...",
            "Astrobiology Arena: The Search for Extraterrestrial Life — Astrobiology Arena is dedicated to exploring...",
            "Martian Memo: Latest on Mars Exploration — Martian Memo focuses on the Red Planet, bringing you news...",
            "Quasar Quest: Exploring the Universe’s Brightest Objects — Quasar Quest takes readers to the far reaches..."
        ]

        img_urls = [
            "https://images-assets.nasa.gov/image/GSFC_20171208_Archive_e001738/GSFC_20171208_Archive_e001738~orig.jpg",
            "https://images-assets.nasa.gov/image/PIA09579/PIA09579~orig.jpg",
            "https://images-assets.nasa.gov/image/iss072e098102/iss072e098102~orig.jpg",
            "https://images-assets.nasa.gov/image/carina_nebula/carina_nebula~orig.png",
            "https://images-assets.nasa.gov/image/PIA04591/PIA04591~orig.jpg",
            "https://images-assets.nasa.gov/image/iss064e041512/iss064e041512~orig.jpg",
            "https://images-assets.nasa.gov/image/jsc2023e058643/jsc2023e058643~orig.jpg",
            "https://images-assets.nasa.gov/image/PIA26453/PIA26453~orig.jpg",
            "https://picsum.photos/200/300?random=1",
            "https://picsum.photos/200/300?random=2",
            "https://picsum.photos/200/300?random=3",
            "https://picsum.photos/200/300?random=4",
            "https://picsum.photos/200/300?random=5",
            "https://picsum.photos/200/300?random=55",
            "https://picsum.photos/200/300?random=33",
            "https://picsum.photos/200/300?random=22",
            "https://picsum.photos/200/300?random=11",
            "https://picsum.photos/200/300?random=7"
        ]

        categories = Category.objects.all()
        if categories.exists():
            for title, content, img_url in zip(titles, contents, img_urls):
                category = random.choice(categories)
                Post.objects.create(title=title, content=content, img_url=img_url, category=category)

            self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))
        else:
            self.stdout.write(self.style.ERROR("No categories found. Please add categories before running this command."))
