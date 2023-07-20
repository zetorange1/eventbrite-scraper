import pathlib

from bs4 import BeautifulSoup
import requests

from models import Event

SCRIPT_DIR = pathlib.Path(__file__).parent.absolute()
EVENTBRITE_URL = 'https://www.eventbrite.com/d'


class EventbriteScraper:
    @classmethod
    def get_events(cls, state, city, category, number):
        page = requests.get(f'{EVENTBRITE_URL}/{state}--{city}/{category}')
        soup = BeautifulSoup(page.content, 'html.parser')

        event_elems = soup.find_all('li', class_='search-main-content__events-list-item')    

        for val in range(1, int(number / 20)):
            page = requests.get(f'{EVENTBRITE_URL}/{category}/?page={val+1}')
            soup = BeautifulSoup(page.content, 'html.parser')

            event_elems += soup.find_all('li', class_='search-main-content__events-list-item')

        return list(map(lambda e: EventbriteScraper.create_event(e), event_elems[:number]))

    @classmethod
    def create_event(cls, event):
        url = event.find('a', class_='event-card-link').attrs.get('href')
        title = event.find('a', class_='event-card-link').find('h2').text

        event_page = requests.get(url)
        event_soup = BeautifulSoup(event_page.content, 'html.parser')
        
        organizer = event_soup.find('strong', class_='simplified-organizer-info__name-link')
        organizer = organizer.text if organizer else ''
        organizer_contacts = event_soup.find(attrs={'data-testid': 'socialLinks'})
        organizer_contacts = [contact.attrs.get('href') for contact in organizer_contacts.find_all('a')] if organizer_contacts else []

        venue = event_soup.find(attrs={'aria-labelledby': 'location-heading'})
        venue_name = venue.find('strong').text if venue else ''
        venue_location = venue.find('p').text if venue else ''
        venue_location = venue_location.replace(venue_name, '').strip()

        print(f'Scraped information of event "{title}"')

        return Event(
            title=title,
            organizer=organizer,
            contacts=organizer_contacts,
            venue_name=venue_name,
            venue_location=venue_location,
            url=url
        )
