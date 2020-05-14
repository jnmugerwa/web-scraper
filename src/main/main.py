from sys import argv
from main.AirBnBScraper import AirBnBScraper

def main():
    scraper = AirBnBScraper()
    args = argv[1:]
    stays = scraper.scrape(*args)
    print(stays)

if __name__ == '__main__':
    main()