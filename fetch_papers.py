import requests
import feedparser
from pprint import pprint


def get_pdf_link(links):
    for link in links:
        if link["type"] == "application/pdf":
            return link["href"]


if __name__ == "__main__":
    trending_endpoint = "https://trendingpapers.com/api/papers"
    params = {
        "p": 1,
        "o": "pagerank_growth",
        "pd": "Since beginning",
        "cc": "Cited and uncited",
        "c": "Computer Science - Computation and Language" 
    }
        
    r = requests.get(trending_endpoint, params=params)
    if not r.ok:
        raise Exception(f"Fetch to retrieve trending papers: {r.status_code}")

    papers = r.json()
    paper_links = [paper["arxiv_id"] for paper in papers["data"]]
    arxiv_xml_metadata_endpoint = "https://export.arxiv.org/api/query"
    params = {
            "id_list": ','.join(paper_links)
    }
    r = requests.get(arxiv_xml_metadata_endpoint, params=params)

    if r.ok:
       feed = feedparser.parse(r.content)
       pdf_links = [get_pdf_link(entry["links"]) for entry in feed["entries"]]
       pprint(len(pdf_links))

