import urllib.robotparser

def is_url_allowed(target_url, robots_txt_url):
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(robots_txt_url)
    rp.read()
    return rp.can_fetch("*", target_url)

# Example Usage
robots_url = "https://www.concordia.ca/robots.txt"
target_url = "https://www.concordia.ca/about.html"
if is_url_allowed(target_url, robots_url):
    print(f"Crawling is allowed for: {target_url}")
else:
    print(f"Crawling is disallowed for: {target_url}")
