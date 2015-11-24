from nltk.corpus import wordnet

print wordnet.synsets('thick')

for ss in wordnet.synsets('thick'):
    print(ss)
    for sim in ss.similar_tos():
        print('    {}'.format(sim))
