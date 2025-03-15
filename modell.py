import numpy as np
from nltk import trigrams
from collections import defaultdict

class trigramModell:
    def __init__(self, file_):
        self._file = file_

    def generate(self):
        trigramtellinger = defaultdict(lambda: defaultdict(lambda: 0))
        trigrammodell = defaultdict(lambda: defaultdict(lambda: 0.0))

        fil = open(file=f"{self._file}.txt", mode="r", encoding="utf-8")

        # Teller antall ganger et ord kommer etter de to foregående.
        for setning in fil:
            setning = setning.split()
            
            for ord1, ord2, ord3 in trigrams(setning, pad_right=True, pad_left=True):
                trigramtellinger[(ord1, ord2)][ord3] += 1

        # Selve trigrammodellen, som skal fylle med sannsynlighetene for ord gitt de to foregående.
        for (ord1, ord2) in trigramtellinger:
            tellinger_totalt = sum(trigramtellinger[(ord1, ord2)].values())
            
            for ord3 in trigramtellinger[(ord1, ord2)]:
                trigrammodell[(ord1, ord2)][ord3] = trigramtellinger[(ord1, ord2)][ord3] / tellinger_totalt

        # Starter teksten med to tomme ord for trigramkontekst.
        tekst = [None, None]
        ferdig = False
        totalSannsynlighet = 1.0
        top_n = 5

        while not ferdig:
            nøkkel = tuple(tekst[-2:])  # Get the last two words

            if nøkkel not in trigrammodell: break

            sorted_words = sorted(trigrammodell[nøkkel].items(), key=lambda x: x[1], reverse=True)
            top_words = [word[0] for word in sorted_words[:top_n]]
            top_probs = [word[1] for word in sorted_words[:top_n]]

            top_probs_normalized = [prob / sum(top_probs) for prob in top_probs]
            neste_ord = np.random.choice(top_words, p=top_probs_normalized)
            tekst.append(neste_ord)

            totalSannsynlighet *= trigrammodell[nøkkel][neste_ord]

            if len(tekst) >= 52: 
                if neste_ord is None: 
                    ferdig = True

        return ' '.join([ord for ord in tekst if ord is not None]).strip()
        # print(f"\nTilfeldig generert tekst:\n<s>\n{output}\n</s>\n({len(tekst) - 2} ord)")  # Adjusted word count for trigram context
        # print(f"\nSannsynligheten for den genererte teksten: {totalSannsynlighet}")
