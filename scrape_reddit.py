import praw, yaml, json, datetime, pathlib, sys
cfg = yaml.safe_load(open("config.yaml", encoding="utf-8"))
reddit = praw.Reddit(
    client_id=cfg["reddit_client"],
    client_secret=cfg["reddit_secret"],
    user_agent="mythScraper1.0"
)
SUBS = ["creepy", "nosleep"]
items = []
for sub in SUBS:
    for post in reddit.subreddit(sub).top(time_filter="week", limit=20):
        items.append({
            "sub": sub,
            "title": post.title,
            "url": post.url,
            "summary": post.selftext[:400].replace("\n"," "),
            "ts": int(post.created_utc)
        })
out = pathlib.Path("ideas_raw.json")
json.dump(items, open(out,"w",encoding="utf-8"), ensure_ascii=False, indent=2)
print(f"✅ scraped {len(items)} posts -> {out}")
