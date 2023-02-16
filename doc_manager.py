from flask import send_file
from config import config
import os
from os import path
from pathlib import Path
import pandas as pd
import threading
import time

doc_config = config['doc_manager']
doc_index = pd.DataFrame(columns=doc_config['DOC_INDEX_HEADERS'])


def match_term_to_doc(term: str):
    print(f"Searching for {term} in {doc_index['DOCTAG'].values}")
    if term in doc_index['DOCTAG'].values:
        doc = doc_index.loc[doc_index['DOCTAG'] == term].iloc[0]
        return send_file(doc['DOCUMENT_PATH'])
    else:
        return None


def update_doc_index():
    # print("Updating index from `docs` folder")
    in_docs_files = [Path(path.join(doc_config['AUTO_ADD_DOCS_DIR'], f))
                     for f in os.listdir(doc_config['AUTO_ADD_DOCS_DIR'])]
    doctags = [f.stem for f in in_docs_files]
    files = [f.absolute().as_posix() for f in in_docs_files]
    doc_index['DOCTAG'] = doctags
    doc_index['DOCUMENT_PATH'] = files


update_doc_index()
