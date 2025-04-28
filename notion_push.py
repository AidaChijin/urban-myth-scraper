import csv, yaml, json, pathlib
from notion_client import Client
cfg = yaml.safe_load(open("config.yaml"))
notion = Client(auth=cfg["notion_token"])
DB = cfg["notion_db"]
for title, hook, url, fresh, visual in csv.reader(open("ideas.tsv",encoding="utf-8"), delimiter="\t"):
    notion.pages.create(
      parent={"database_id":DB},
      properties={
        "Title":{"title":[{"text":{"content":title}}]},
        "Hook":{"rich_text":[{"text":{"content":hook}}]},
        "URL":{"url":url},
        "Fresh":{"number":int(fresh)},
        "Visual":{"number":int(visual)},
        "Picked":{"checkbox":False}
      }
    )
print("✅ Notion updated")
