import random
lst = ['Abyss', 'Ample', 'Ankle', 'Aroma', 'Aural', 'Began', 'Blunt', 'Braid', 'Brisk', 'Bumpy', 'Chive', 'Clasp', 'Crave', 'Crest', 'Cumin', 'Drape', 'Dregs', 'Dumpy', 'Dusky', 'Dwell', 'Elite', 'Ember', 'Enact', 'Evade', 'Evoke', 'Fable', 'Flair', 'Fluke', 'Folly', 'Gauze', 'Giddy', 'Gloom', 'Gorge', 'Gusty', 'Haste', 'Hilly', 'Hippy', 'Hovel', 'Hunch', 'Icily', 'Inept', 'Inert', 'Irate', 'Ivory', 'Jaded', 'Jazzy', 'Jolly', 'Joust',
       'Jumpy', 'Kinky', 'Knack', 'Knave', 'Knead', 'Kudos', 'Lanky', 'Latch', 'Lolly', 'Lurid', 'Mirth', 'Moody', 'Mourn', 'Mower', 'Muggy', 'Nanny', 'Nappy', 'Nerve', 'Nifty', 'Nudge', 'Olive', 'Onset', 'Oomph', 'Ounce', 'Ovals', 'Peppy', 'Pious', 'Pique', 'Plush', 'Poise', 'Quail', 'Quake', 'Quell', 'Quill', 'Quirk', 'Ravel', 'Reedy', 'Ruddy', 'Runic', 'Sable', 'Spicy', 'Stilt', 'Swath', 'Swirl', 'Toast', 'Tonic', 'Triad', 'Tryst', 'Tweak']
a = random.randint(0, len(lst))
word = lst[a]
c = 0
while True:
    b = input('Guess : ')
    if len(b) == 5:
        if b == word:
            print('You won.')
            break
        else:
            c = c+1
            if c == 6:
                print('You lose.')
                break
            else:
                for x in range(5):
                    if b[x] == word[x]:
                        print(b[x], end='')
                    else:
                        print('_', end='')
                print()
    else:
        print('Length should be 5.')
