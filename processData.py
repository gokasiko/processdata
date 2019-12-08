import json

a = dict()
a["test"] = "sdf"
a["test1"] = "sdf2"
fw = open('CSQA_DENOTATIONS_full_944K.json', 'w', encoding="UTF-8")
fw.writelines(json.dumps(a, indent=1, ensure_ascii=False))


