import json, csv, openai, yaml, pathlib
cfg = yaml.safe_load(open("config.yaml"))
openai.api_key = cfg["openai_key"]
data = json.load(open("ideas_ja.json",encoding="utf-8"))
rows = []
for d in data:
    ask = f"本文: {d['summary_ja']}\n---\n1.15字フック\n2.新鮮度1-5\n3.映像化指数1-5\n日本語でTSV"
    r = openai.ChatCompletion.create(model="gpt-4o-mini",messages=[{"role":"user","content":ask}])
    hook,fresh,visual=*r.choices[0].message.content.split("\t"),
    rows.append([d["title"], hook, d["url"], fresh, visual])
with open("ideas.tsv","w",newline="",encoding="utf-8") as f:
    csv.writer(f, delimiter="\t").writerows(rows)
print("✅ TSv saved ideas.tsv")
