all_material = {
    "铁块": {
        "合成时间": ["冶炼台", 1], "合成物品": ["铁矿", 1, ],
    },
}

res = {}


def dtool(material, total, res_back):
    if material in res_back:
        res_back[material] += total
    else:
        res_back[material] = total
    for sub_mate in all_material[material]["合成物品"]:
        dtool(sub_mate[0], sub_mate[1]*total, res_back)
