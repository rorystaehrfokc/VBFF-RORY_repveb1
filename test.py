import json, os
lang = {}
language = "en"
language_file = f"translated/about_{language}.json"
if os.path.exists(language_file):
    with open(language_file, "r") as fp:
        lang = json.load(fp)
else:
    with open(language_file, "w") as file:
        json.dump(lang, file, indent=4)

print(lang)

#MESSAGES_FILE = "messages.json"
#if os.path.exists(MESSAGES_FILE):
#    with open(MESSAGES_FILE, "r") as file:
#        messages = json.load(file)
#else:
#    messages = {}
#
#with open(MESSAGES_FILE, "w") as file:
#        json.dump(messages, file, indent=4)