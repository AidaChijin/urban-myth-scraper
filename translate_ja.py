import json, yaml, openai, pathlib
cfg = yaml.safe_load(open("config.yaml"))
openai.api_key = cfg["openai_key"]
raw = json.load(open("ideas_raw.json",encoding="utf-8"))
out_list = []
for it in raw:
    resp = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
          {"role":"system","content":"Translate the following text into natural Japanese."},
          {"role":"user","content":it["summary"]}
        ]
    )
    it["summary_ja"] = resp.choices[0].message.content.strip()
    out_list.append(it)
path = pathlib.Path("ideas_ja.json")
json.dump(out_list, open(path,"w",encoding="utf-8"), ensure_ascii=False, indent=2)
print(f"✅ translated -> {path}")
