import urllib.robotparser

def fetch_and_save_robots_info(robots_txt_url, output_file):
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(robots_txt_url)
    rp.read()

    with open(output_file, 'w') as file:
        file.write(f"Fetching {robots_txt_url}...\n")

        file.write("\nDisallowed Paths:\n")
        for rule in rp.default_entry.rulelines:
            if not rule.allowance:
                file.write(f"{rule.path}\n")
