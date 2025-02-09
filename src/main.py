from typing import List
import sys
import requests
import re
import os


def main():
    url = parse_args()
    print(f"Fetching content from: {url}...")
    main_page_content = requests.get(url).text
    links = get_stanford_links(main_page_content)

    sub_dirs = url.split("/")[3:]

    base_dir = "moss-archive/" + "/".join(sub_dirs)
    
    os.makedirs(base_dir, exist_ok=True)
    
    # remove stanford paths from all hyperlinks
    main_page_content = main_page_content.replace(url + "/", "", -1)

    with open(base_dir + "/index.html", "w+") as file:
        file.write(main_page_content)   
    
    # limit to only top 30 results to comply with stanfords rate limits
    # take top 30, every other link
    for i in range(0,60, 2):
        print(f"Archiving {links[i]}")
        download_match_page(links[i], base_dir)


def download_match_page(url: str, base_dir: str):
    """
    Downloads a match page from its url, including all sub pages
    
    url: the url of the match page
    base_dir: the base directory to download it to 
    """

    no_ext_link = url[:len(url) - 5]
    
    parts = no_ext_link.split("/")
    file_name = parts[len(parts) - 1]

    file_exts = ["-top.html", "-0.html", "-1.html", ".html"]
    
    for ext in file_exts:
        full_path = no_ext_link + ext
        with open(base_dir + "/" + file_name + ext, "w+") as file:
            file.write(requests.get(no_ext_link + ext).text)
            


def parse_args():
    """
    parses args from the archive.sh scripts
    """
    if len(sys.argv) != 2:
        sys.exit(1)
    return sys.argv[1]


def get_stanford_links(main_page_content: str) -> List[str]:
    """
    Gets the *stanford* links, not the local copies of those links
    """
    filter_out = get_ignorable_links()

    # ugly regex
    all_links = re.findall(r'HREF="([^"]*)"', main_page_content)

    cleaned_links = list(
        filter(lambda link: link not in filter_out, all_links))

    return cleaned_links


def get_ignorable_links() -> List[str]:
    """
    util for all the useless links on the index page
    """
    return ["http://moss.stanford.edu/general/format.html",
            "http://moss.stanford.edu/general/tips.html",
            "http://moss.stanford.edu/general/faq.html",
            "mailto:moss-request@cs.stanford.edu",
            "http://moss.stanford.edu/general/scripts.html",
            "http://moss.stanford.edu/general/credits.html"
            ]


if __name__ == "__main__":
    main()
