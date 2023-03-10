
list_st = [{"name": "Bob","score": [1,2,3,4]},
           {"name": "Sasha","score": [7,7,3,10]},
           {"name": "Marla","score": [1,3,6,8]}]


def bigger_score(list_bigger):
    name = ""
    max_score = 0
    for studetns in list_bigger:
        score = studetns.get("score")
        avg_score = sum(score)/len(score)
        if avg_score > max_score:
            max_score = avg_score
            name = studetns.get("name")
    return name


def awg_score(list_bigger):
    name_max = ""
    name_min = ""
    max_score = 0
    min_score = 100
    for studetns in list_bigger:
        score = studetns.get("score")
        avg_score = sum(score)/len(score)
        if avg_score > max_score:
            max_score = avg_score
            name_max = studetns.get("name")
        if avg_score < min_score:
            min_score = avg_score
            name_min = studetns.get("name")
    return name_max, name_min


s_max, s_min = (awg_score(list_st))
print(s_max)
print(s_min)
