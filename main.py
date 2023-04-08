import json
from os import getenv
from pyairtable.api import Api, Table
from eagle_cool_client import EagleCoolClient
from tqdm import tqdm


airtable_token = getenv("AIRTABLE_TOKEN", "none")
api = Api(airtable_token)
airtable_base = api.get_base(getenv("AIRTABLE_BASE_ID", "none"))
generations: Table = airtable_base.get_table("generations")
eagle = EagleCoolClient()
all_gens = generations.all()

indexes = {
    "gen_id": {item["fields"]["gid"]: item["fields"] for item in all_gens},
    "gen_id+seed": {
        f"{item['fields']['gid']}-{item['fields']['seed']}": item["fields"]
        for item in all_gens
    },
    "seed": {f"{item['fields']['seed']}": item["fields"] for item in all_gens},
}

folders = eagle.list_folders()

name = "stash"


def find_folder(folders, name):
    stash_folders = []
    for folder in folders:
        if name in folder["name"]:
            stash_folders.append(folder)
        if "children" in folder:
            stash_folders.extend(find_folder(folder["children"], name))
    return stash_folders


stash_folders = find_folder(folders["data"], name)

images = eagle.list_items(folders=",".join([x["id"] for x in stash_folders]))["data"]
for image in tqdm(images):
    name = image["name"]
    tags = image["tags"]
    if "has_prompt" not in tags:
        for _, index in indexes.items():
            if name in index:
                gen_data = index[name]
                tags.append("has_prompt")
                result = eagle.update_item(
                    id=image["id"],
                    annotation=json.dumps(gen_data, ensure_ascii=False),
                    tags=tags,
                )
print(stash_folders)
