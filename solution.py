def solution(x, y):
    additional_ids_x = []
    additional_ids_y = []

    for i in y:
        if i not in x:
            additional_ids_x.append(i)
        else:
            additional_ids_x.append(None)

    for i in x:
        if i not in y:
            additional_ids_y.append(i)
        else:
            additional_ids_y.append(None)

    result = []

    if not any(additional_ids_x):
        for i in additional_ids_y:
            if i is not None:
                result.append(i)
    else:
        for i in additional_ids_x:
            if i is not None:
                result.append(i)

    return result[0]
