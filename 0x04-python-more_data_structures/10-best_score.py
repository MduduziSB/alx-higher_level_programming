#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None and len(a_dictionary) != 0:
        count = 0
        max_score = 0
        highest = ""
        for key, value in a_dictionary.items():
            if count == 0:
                max_score = value
                highest = key
            else:
                if value > max_score:
                    max_score = value
                    highest = key
            count += 1
        return highest
    return None
