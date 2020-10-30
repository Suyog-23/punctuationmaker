def sentence_maker(phrase):
    capitalized = phrase.capitalize()
    intero = ("how", "why", "when", "where", "is", "who")
    if phrase.startswith(intero):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

results = []

while True:
    a = input("Enter your msgs: ")
    if a == "/stop":
        break
    else:
        results.append(sentence_maker(a))

print(" ".join(results))
