import json

question_base = {}

with open("json_chords_base.json", "r") as f:
    jsonObject = json.loads(f.read())

    for key in jsonObject:
        question_base["correct"] = jsonObject[key]["image7"], jsonObject[key]["sound7"]
        question_base["correct"] = jsonObject[key]["image_dur"], jsonObject[key]["sound_dur"]
        question_base["correct"] = jsonObject[key]["image_mol"], jsonObject[key]["sound_mol"]

print(question_base)