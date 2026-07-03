from glob import glob
import sys
import os
import bibtexparser
from bibtexparser import middlewares as mw
from tqdm import tqdm
import re

# Map BibTeX types → RIS TY tags
TYPE_MAP = {
    'article': 'JOUR',
    'book': 'BOOK',
    'inproceedings': 'CONF',
    'incollection': 'CHAP',
    'phdthesis': 'THES',
    'mastersthesis': 'THES',
    'techreport': 'RPRT',
    'misc': 'GEN',
}

# Field → RIS tag
FIELD_MAP = {
    'author': 'AU', 'editor': 'A2', 'title': 'TI',
    'journal': 'JF', 'booktitle': 'T2', 'year': 'PY',
    'volume': 'VL', 'number': 'IS', 'pages': ('SP','EP'),
    'publisher': 'PB', 'address': 'AD', 'doi': 'DO',
    'url': 'UR', 'abstract': 'N2', 'keywords': 'KW',
}


def bib_to_ris_entries(bib_path):
    """Convert a .bib file to list of RIS dicts using bibtexparser v2."""
    # Correct middleware usage
    layers = [
        mw.LatexDecodingMiddleware(),
        mw.MonthIntMiddleware(),
        mw.SeparateCoAuthors(),
        # mw.SplitNameParts(),  # optional if you need first/last name structure
    ]
    bib_db = bibtexparser.parse_file(
        bib_path,
        append_middleware=layers
    )
    ris_entries = []
    for entry in bib_db.entries:
        ris = {}

        # Ensure TY exists
        ris['TY'] = TYPE_MAP.get(entry.entry_type.lower(), 'GEN')
        # print(entry.entry_type)
        # print(ris['TY'])
        # input()

        # Extract fields
        for bibf, field in entry.fields_dict.items():
            val = field.value  # Extract actual string :contentReference[oaicite:1]{index=1}
            tag = FIELD_MAP.get(bibf.lower())
            if tag == 'A2':
                continue
            # print(tag)
            # print(field)
            # print(field)
            if not tag:
                continue
            if isinstance(tag, tuple):
                sp, ep = (val.split('--')[0], val.split('--')[1]) if '--' in val else (val, '')
                ris[tag[0]] = sp
                if ep:
                    ris[tag[1]] = ep
            else:
                if tag in ('AU', 'A2'):
                    # print(val)
                    ris[tag] = [a.strip() for a in val]
                elif tag == 'KW':
                    ris[tag] = [k.strip() for k in val]
                else:
                    ris[tag] = val
        # print(ris)

        # input()
        ris_entries.append(ris)

    return ris_entries

def combine_bib_to_ris(bib_paths, out_ris):
    all_entries = []
    for bib in tqdm(bib_paths):
        # print(f"→ Converting '{bib}'...")
        all_entries.extend(bib_to_ris_entries(bib))
    print(all_entries)
    write_ris(all_entries, out_ris)
    # input()
    # with open(out_ris, 'w', encoding='utf-8') as rf:
    #     rispy.dump(
    #         all_entries,
    #         rf,
    #         skip_unknown_tags=False,
    #         list_tags=['AU', 'A2', 'KW']
    #     )
    # print(all_entries)
    # print(f"✅ Wrote {len(all_entries)} total entries to '{out_ris}'")
def write_ris(entries: list[dict], out_path: str):
    """
    entries: list of dicts where keys are RIS tags (like 'TY', 'TI', 'AU', 'SP', etc.)
    Each dict must include:
      - 'TY' (record type)
      - other tags e.g., 'AU', 'A2', 'TI', 'T2', 'PY', 'SP', 'EP', 'AD', 'PB', 'DO', 'UR'
    """
    list_fields = {'AU', 'A2', 'KW'}

    with open(out_path, 'w', encoding='utf-8', newline='\n') as f:
        for entry in entries:
            ty = entry.get('TY', 'GEN').strip()
            f.write(f"TY  - {ty}\n")
            for tag, val in entry.items():
                if tag.upper() == 'TY':
                    continue
                if tag in list_fields and isinstance(val, list):
                    for item in val:
                        f.write(f"{tag}  - {item}\n")
                else:
                    f.write(f"{tag}  - {val}\n")
            f.write("ER  - \n")

if __name__ == "__main__":
    os.makedirs('ris', exist_ok=True)
    combine_bib_to_ris(glob('bibtex/*.bib'), 'ris/combined.ris')
