import argparse
import csv

from scraper import EventbriteScraper


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Eventbrite scraper")
    parser.add_argument(
        "category",
        type=str,
        help="Select the type of events you'd like to find",
    )
    parser.add_argument(
        "city",
        help="Select the city e.g. Chicago.",
    )
    parser.add_argument(
        "state",
        help="Select the two letter state e.g. IL.",
    )
    parser.add_argument(
        "-n",
        "--number",
        default=10,
        type=int,
        help="Number of events you'd like to find, please specify in multiples of 10.",
    )
    parser.add_argument(
        "-d",
        "--database",
        default="sqlite",
        type=str,
        choices=["sqlite", "mysql"],
        help="Select either a sqlite or mysql database, by default sqlite is used."
    )

    args = parser.parse_args()

    events = EventbriteScraper.get_events(args.state, args.city, args.category, args.number)
    event_tuples = list(map(lambda e: e.to_tuple(), events))

    csv_file = f'data_{args.state}_{args.city}_{args.category}.csv'
    with open(csv_file, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['Title', 'Organizer', 'Organizer Contact', 'Venue Name', 'Venue Location', 'Event link'])
        writer.writerows(event_tuples)

    print(f'Data has been successfully written to {csv_file}.')
