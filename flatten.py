from json import loads
from json import dumps


def traverse(parent_key, o):
    if isinstance(o, dict):
        for key in o:
            if parent_key == "":
                traverse(key, o[key])
            else:
                traverse(parent_key + "_" + key, o[key])
    else:
        out_dict[parent_key] = o


with open("issues.json", "r") as in_file:
    with open("issues_flat.json", "w") as out_file:
        for line in in_file:
            out_dict = {}
            traverse("", loads(line))
            out_file.write("{}\n".format(dumps(out_dict)))
