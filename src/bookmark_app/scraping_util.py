import sys
import re
from urllib.robotparser import RobotFileParser

import requests
from bs4 import BeautifulSoup


def get_root_url(url):
    pattern = r"(?P<root>https?://.*?)\/.*"
    result = re.match(pattern, url)
    if result is not None:
        return result.group("root")
    raise ValueError(f"Passed url is invalid: {url}")


def can_scrapping(url):
    # check robots.txt
    user_agent = "*"
    root_url = get_root_url(url)
    url = f"{root_url}/*"
    robots_txt_url = f"{root_url}/robots.txt"

    rp = RobotFileParser()
    rp.set_url(robots_txt_url)
    rp.read()
    return rp.can_fetch(user_agent, url)


def main():
    url = sys.argv[1]
    if can_scrapping(url):
        headers = {"User-Agent": ""}
        # TODO: If scraping is failed, retry with crawl deray.
        #       https://docs.python.org/ja/3/library/urllib.robotparser.html#urllib.robotparser.RobotFileParser.crawl_delay
        response = requests.get(url, headers=headers)
        content = BeautifulSoup(response.text, "html.parser").text
        print(content.strip())


if __name__ == "__main__":
    main()
