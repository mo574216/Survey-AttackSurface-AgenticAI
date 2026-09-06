import urllib.request
import json
import re

queries = [
    'container-title:"Transactions on Dependable and Secure Computing" "access control"',
    'container-title:"Transactions on Dependable and Secure Computing" "sandbox"',
    'container-title:"Transactions on Dependable and Secure Computing" "vulnerability"',
    'container-title:"Transactions on Dependable and Secure Computing" "provenance"',
    'container-title:"Transactions on Dependable and Secure Computing" "remote code execution"',
    'container-title:"Transactions on Dependable and Secure Computing" "cloud"',
    'container-title:"Transactions on Information Forensics and Security" "adversarial attack"',
    'container-title:"Transactions on Information Forensics and Security" "evasion"',
    'container-title:"Transactions on Information Forensics and Security" "backdoor"',
    'container-title:"Transactions on Information Forensics and Security" "poisoning"'
]

headers = {'User-Agent': 'SurveyGroundingBot/1.0 (mailto:scholar@ieee.org)'}

seen_dois = set()
with open("scratch/ieee_summary.json", "r", encoding="utf-8") as f:
    existing = json.load(f)
    for it in existing:
        seen_dois.add(it['doi'])

entries = []

for q in queries:
    url = f"https://api.crossref.org/works?query={urllib.parse.quote(q)}&rows=4&filter=type:journal-article"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            items = data.get('message', {}).get('items', [])
            for it in items:
                doi = it.get('DOI')
                if not doi or doi in seen_dois:
                    continue
                seen_dois.add(doi)
                
                title = it.get('title', [''])[0] if it.get('title') else ''
                authors = it.get('author', [])
                if not authors or not title:
                    continue
                
                author_str = " and ".join([
                    f"{a.get('given', '')} {a.get('family', '')}".strip()
                    for a in authors if 'family' in a
                ])
                if not author_str:
                    continue
                
                journal = it.get('container-title', [''])[0] if it.get('container-title') else ''
                if "Transactions on Dependable and Secure Computing" not in journal and "Transactions on Information Forensics and Security" not in journal:
                    continue
                    
                year = None
                if 'published-print' in it and 'date-parts' in it['published-print']:
                    year = it['published-print']['date-parts'][0][0]
                elif 'published-online' in it and 'date-parts' in it['published-online']:
                    year = it['published-online']['date-parts'][0][0]
                elif 'issued' in it and 'date-parts' in it['issued']:
                    year = it['issued']['date-parts'][0][0]
                
                if not year:
                    continue
                
                volume = it.get('volume', '')
                issue = it.get('issue', '')
                page = it.get('page', '')
                
                first_author = authors[0].get('family', 'Author').lower()
                first_author = re.sub(r'[^a-z]', '', first_author)
                clean_title_word = re.sub(r'[^a-z]', '', title.split()[0].lower()) if title.split() else 'paper'
                key = f"{first_author}{year}{clean_title_word}"
                
                # clean xml in title
                clean_title = re.sub(r'<[^>]+>', '', title)
                
                bib = f"@article{{{key},\n"
                bib += f"  author  = {{{author_str}}},\n"
                bib += f"  title   = {{{{{clean_title}}}}},\n"
                bib += f"  journal = {{{journal}}},\n"
                if volume:
                    bib += f"  volume  = {{{volume}}},\n"
                if issue:
                    bib += f"  number  = {{{issue}}},\n"
                if page:
                    bib += f"  pages   = {{{page}}},\n"
                bib += f"  year    = {{{year}}},\n"
                bib += f"  doi     = {{{doi}}}\n"
                bib += "}\n"
                entries.append((key, clean_title, journal, year, doi, bib))
    except Exception as e:
        print(f"Error fetching {q}: {e}")

print(f"Collected {len(entries)} additional verified TDSC/TIFS journal articles.")
with open("scratch/ieee_refs.bib", "a", encoding="utf-8") as f:
    for e in entries:
        f.write(e[5] + "\n")

with open("scratch/tdsc_tifs_summary.json", "w", encoding="utf-8") as f:
    json.dump([{"key": e[0], "title": e[1], "journal": e[2], "year": e[3], "doi": e[4]} for e in entries], f, indent=2)
