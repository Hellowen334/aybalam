import os
from typing import List
import yaml
import config

languages = {}
languages_present = {}


def get_string(lang: str):
    return languages[lang]


# Load English first
languages["en"] = yaml.safe_load(
    open(r"./strings/langs/en.yml", encoding="utf8")
)
languages_present["en"] = languages["en"]["name"]

# Load other languages
for filename in os.listdir(r"./strings/langs/"):
    if filename.endswith(".yml"):
        language_name = filename[:-4]
        if language_name == "en":
            continue
        languages[language_name] = yaml.safe_load(
            open(r"./strings/langs/" + filename, encoding="utf8")
        )
        for item in languages["en"]:
            if item not in languages[language_name]:
                languages[language_name][item] = languages["en"][item]
        try:
            languages_present[language_name] = languages[language_name]["name"]
        except:
            print("There is some issue with the language file inside bot.")
            exit()

# Apply branding and configuration replacements dynamically
for lang_code in languages:
    for key, val in languages[lang_code].items():
        if isinstance(val, str):
            val = val.replace("https://t.me/riskyhater", f"https://t.me/{config.OWNER_USERNAME}")
            val = val.replace("https://t.me/aryaduyuru", config.SUPPORT_CHANNEL)
            val = val.replace("https://t.me/aryaduyuru", config.SUPPORT_CHAT)
            val = val.replace("@riskyhater", f"@{config.OWNER_USERNAME}")
            languages[lang_code][key] = val

