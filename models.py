from dataclasses import dataclass


@dataclass
class Event:
    title: str
    organizer: str
    contacts: list
    venue_name: str
    venue_location: str
    url: str

    def to_tuple(self):
        return (
            self.title, self.organizer, self.contacts, self.venue_name, self.venue_location, self.url
        )
