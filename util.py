import json
def name() -> str:
    with open("config.json","r") as config:
        x=config.read()
    data=json.loads(x)
    return data["name"]