from lexicon.lexicon import LEXICON_COMMANDS

res = tuple([(k, v) for k, v in LEXICON_COMMANDS.items()])

print(type(res))
print(res)
