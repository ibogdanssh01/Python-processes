def order_by_key(dictionary: dict) -> dict: # Ordered by key(process_id)
    myKeys = list(dictionary.keys())
    processDictOrdered = {i: dictionary[i] for i in myKeys}
    return processDictOrdered

def order_by_name(dictionary: dict) -> dict:
    processDictOrdered = {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1])}
    return processDictOrdered
