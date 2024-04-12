def sort_strings_by_length(strings):
    return sorted(strings, key=len) + sorted(strings, key=len, reverse=True)

# Пример использования:
strings = ["aaa", "bb", "c", "dddd", "eeeee"]
print(sort_strings_by_length(strings))
