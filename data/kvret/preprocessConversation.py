
import json

filename = 'kvret_train_public.json'

#Read JSON data into the datastore variable
if filename:
    with open(filename, 'r') as f:
        datastore = json.load(f)
i = 0
#Use the new datastore datastructure
for dialogue in datastore:
    conversationIds = []
    for utterence in dialogue["dialogue"]:
        with open('kvret_train_lines.txt', 'a') as f:
            i = i+1
            conversationIds.append("'L{0}'".format(i))
            f.write('L{0}'.format(i)+' +++$+++ '+utterence['data']['utterance']+'\n')
            f.close()
    with open('kvret_train_conversations.txt', 'a') as c :
        c.write('['+', '.join(conversationIds)+']')
        c.write('\n')
        c.close()

