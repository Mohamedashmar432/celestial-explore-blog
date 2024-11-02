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
            "Galactic Gazette: Latest News from the Cosmos — Dive into the Galactic Gazette for fresh updates on the universe's wonders! Covering everything from black holes and nebulae to new galaxies, we bring the marvels of space closer to you. With a focus on scientific breakthroughs, such as NASA's latest missions and discoveries from global observatories, we’re your trusted source for all things cosmic. Our articles are crafted for both science enthusiasts and curious readers, aiming to inspire wonder and knowledge in equal measure.",
            "Stellar Stories: Exploring the Universe Beyond Earth — Stellar Stories captures humanity's quest to understand the cosmos. Through this blog, readers can journey through fascinating content on celestial events, from meteor showers to solar eclipses, and learn about the technologies that help us observe the universe. We share insights on everything beyond our planet, celebrating astronomical wonders and offering deep-dives into ongoing research and the potential for human space exploration.",
            "Cosmic Chronicles: Updates on Space Discoveries — Cosmic Chronicles brings the latest in space science, from groundbreaking discoveries of new exoplanets to theories about dark matter and cosmic origins. This blog provides clear, concise insights into complex topics, offering readers an opportunity to stay updated on the major breakthroughs and innovations within astronomy and space exploration. Cosmic Chronicles makes it easy for enthusiasts to explore the science that shapes our understanding of the cosmos.",
            "Starbound Signals: Breaking News from Deep Space — Starbound Signals provides breaking news and updates from the far reaches of space. Discover new theories, recent observations, and the latest astronomical phenomena, brought directly to your screen. We cover everything from newly observed supernovae to intriguing developments in quantum physics, making it perfect for those who want to stay at the frontier of space science and cosmic events.",
            "Celestial Navigator: Your Guide to Astronomy Events — Celestial Navigator offers a comprehensive guide to upcoming astronomy events. From lunar eclipses to planetary alignments, we help you prepare for these events with explanations, viewing tips, and scientific background. Whether you're an avid stargazer or a beginner, this blog has something for everyone, making celestial phenomena accessible and enjoyable for all ages.",
            "Starbound Signals: Breaking News from Deep Space — Starbound Signals provides breaking news and updates from the far reaches of space. Discover new theories, recent observations, and the latest astronomical phenomena, brought directly to your screen. We cover everything from newly observed supernovae to intriguing developments in quantum physics, making it perfect for those who want to stay at the frontier of space science and cosmic events.",
            "The Astrophile’s Almanac: Space Observations and Tips — The Astrophile’s Almanac is tailored for the curious and passionate space lover. With in-depth posts on celestial observations and guides on how to get the best stargazing experience, this blog covers key aspects of amateur astronomy. We share tips, telescope recommendations, and insights into popular night sky events, helping you make the most of every opportunity to explore the cosmos.",
            "Celestial Navigator: Your Guide to Astronomy Events — Celestial Navigator offers a comprehensive guide to upcoming astronomy events. From lunar eclipses to planetary alignments, we help you prepare for these events with explanations, viewing tips, and scientific background. Whether you're an avid stargazer or a beginner, this blog has something for everyone, making celestial phenomena accessible and enjoyable for all ages..",
            "The Astrophile’s Almanac: Space Observations and Tips — The Astrophile’s Almanac is tailored for the curious and passionate space lover. With in-depth posts on celestial observations and guides on how to get the best stargazing experience, this blog covers key aspects of amateur astronomy. We share tips, telescope recommendations, and insights into popular night sky events, helping you make the most of every opportunity to explore the cosmos.",
            "Lunar Log: Updates on the Moon’s Mysteries — Lunar Log is dedicated to all things lunar! Our blog brings you updates on new discoveries about the Moon, as well as the latest in lunar exploration missions. From insights on lunar geology to upcoming plans for human settlement on the Moon, Lunar Log is your go-to source for staying informed on our closest celestial neighbor’s secrets.",
            "Nebulae Notes: Stories from the Interstellar Medium — Nebulae Notes dives into the colorful, gaseous regions of space known as nebulae. Explore fascinating facts about these cosmic nurseries where stars are born, along with stunning imagery and explanations of how they shape the universe. Our blog brings science and beauty together, showcasing the wonder of these interstellar marvels through detailed articles and visuals.",
            "Exoplanet Explorer: Discover Worlds Beyond Our Solar System — Exoplanet Explorer is dedicated to the search for worlds beyond our solar system. This blog provides insights into the latest findings about distant planets, their atmospheres, and potential for habitability. From super-Earths to gas giants, we keep you informed about the cutting-edge research and discoveries that bring us closer to understanding alien worlds..",
            "The Comet Chronicles: Tracking Cosmic Wanderers — The Comet Chronicles tracks the journeys of comets as they make their way through our solar system. Learn about their origins, unique compositions, and how scientists study these icy travelers. Each post explores historical records, recent sightings, and the science behind these enigmatic celestial bodies that offer clues about the early solar system",
            "The Sunspot Report: Solar Activity and Its Effects — The Sunspot Report provides up-to-date information on solar activity, including sunspots, solar flares, and their effects on Earth. With a focus on space weather, this blog helps readers understand how solar phenomena influence everything from communication systems to auroras. Stay informed on our Sun's dynamic behavior and its impacts on our planet.",
            "Galaxy Gazetteer: Insights on Our Galaxy and Beyond — Galaxy Gazetteer explores the intricacies of galaxies, both near and far. We take readers on a journey through the Milky Way and into distant galaxies, uncovering what makes them unique and how scientists study them. Whether it's exploring galactic collisions or star formation, this blog provides captivating insights into the vastness of the universe.",
            "Astrobiology Arena: The Search for Extraterrestrial Life — Astrobiology Arena is dedicated to exploring the scientific search for life beyond Earth. Discover the latest theories on how life might exist in extreme environments, recent findings from Mars, and the potential for life on exoplanets. Our blog is a gateway into the exciting field of astrobiology, inspiring readers with the possibility of discovering alien life.",
            "Martian Memo: Latest on Mars Exploration — Martian Memo focuses on the Red Planet, bringing you news on robotic missions, Martian geology, and potential for human exploration. We provide updates on NASA's rovers, Mars-based research, and the future of human settlement on Mars. Perfect for space fans and explorers at heart, Martian Memo keeps you informed on all things Mars.",
            "Quasar Quest: Exploring the Universe’s Brightest Objects — Quasar Quest takes readers to the far reaches of the universe to explore quasars, the brightest and most energetic objects known. We cover recent discoveries, theories about their formation, and what they reveal about black holes. This blog is for anyone fascinated by the universe's most powerful cosmic phenomena and the science that unravels their mysteries"
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
            "https://stsci-opo.org/STScI-01JBF254EKSDBD74M3GPKMRVDP.png",
            "https://stsci-opo.org/STScI-01J9S54QP90TATPE8Y7GCYW5KE.png",
            "https://stsci-opo.org/STScI-01J9256XQ1PPK12Y5BQF7GECRN.png",
            "https://stsci-opo.org/STScI-01J4SERT6S0KHKQZ64YWXPXY2Y.png",
            "https://stsci-opo.org/STScI-01HHJFKQG571ZRXMW8XKDJT90K.jpg",
            "https://stsci-opo.org/STScI-01HZ7KQC9J3EF1RVAVWMNXJBPH.png",
            "https://stsci-opo.org/STScI-01HHJFKQG571ZRXMW8XKDJT90K.jpg",
            "https://stsci-opo.org/STScI-01J5EMYVZX464YXYZP0QGJJFDV.png",
            "https://stsci-opo.org/STScI-01JBF254EKSDBD74M3GPKMRVDP.png",
            "https://stsci-opo.org/STScI-01J80BG3KYV0KBCXCB8NSPWWTW.png"
        ]

        categories = Category.objects.all()
        if categories.exists():
            for title, content, img_url in zip(titles, contents, img_urls):
                category = random.choice(categories)
                Post.objects.create(title=title, content=content, img_url=img_url, category=category)

            self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))
        else:
            self.stdout.write(self.style.ERROR("No categories found. Please add categories before running this command."))
