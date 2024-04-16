def counter(name):
    temp=""
    for ch in name:
        temp += ch
        yield temp

print(list(counter('pen')))