def dietEntity(item) -> list:
    return {**{i: str(item[i]) for i in item if i=="_id"}, **{i: item[i] for i in item if i!="_id"}}

def dietsEntity(entity) -> list:
    return [dietEntity(a) for a in entity]


