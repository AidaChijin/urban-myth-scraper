@echo off
conda activate mythscrape
python scrape_reddit.py
python translate_ja.py
python convert_to_tsv.py
python notion_push.py
pause
