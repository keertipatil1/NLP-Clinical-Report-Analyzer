# Clinical Report Analyzer 🩺

A Streamlit-based NLP tool to extract medical entities from clinical reports using scispaCy.

## Features
- Upload `.txt` clinical reports
- Extract diseases, symptoms, medications, etc.
- Link terms to UMLS concepts

## Run Locally

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_md

