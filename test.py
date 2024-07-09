my_dict = {
    'name': 'dan',
     'gender': 'male',
     'birthdate': {'day': 16, 'month': 1, 'year': 1984},
     'weight': 94,
    #  'photos': {'initial_photo': 'AgACAgIAAxkBAAILCmaKmY9viV-oHpx14BpOd63ttj7cAAI02TEbvuJYSKj6N_LzUu-yAQADAgADbQADNQQ'}
     }


b = my_dict.get('photos')['initial_photo']

print(b)
