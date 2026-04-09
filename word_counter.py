text ="""Accordingly we went with Polemarchus to his house; and there we found his brothers Lysias
and Euthydemus, and with them Thrasymachus the Chalcedonian, Charmantides the Paeanian,
and Cleitophon the son of Aristonymus. There too was Cephalus the father of Polemarchus,
whom I had not seen for a long time, and I thought him very much aged. He was seated on a
cushioned chair, and had a garland on his head, for he had been sacrificing in the court; and
there were some other chairs in the room arranged in a semicircle, upon which we sat down by
him. He saluted me eagerly,"""

def clean_text(text):
    text = text.lower()
    for ch in ".,!?:;\"'()":
        text = text.replace(ch,"")
    
    return text

def word_freqency(text):
    words = clean_text(text).split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    
    return freq


def remove_stopwords(freq_dict):
    stop = {"a","an","the","is","in","it","of","and","to","was","that","for","on","are","with"}

    return {w: c for w, c in freq_dict.items() if w not in stop}


#reurning top 5 words
def top_n(freq_dict, n=5):
    return sorted(freq_dict.items(), key = lambda x : x[1], reverse = True)[:n]



freq = word_freqency(text)
clean = remove_stopwords(freq)
top = top_n(clean)

print("Top 5 words : ")
for word, count in top:
    print(f'{word:15} -> {count} times')

#unique words count

unique = set(clean_text(text).split())
print(f'\nTotal unique words : {len(unique)}')

#search 
search = input('\n search for a word : ').lower()

if search in freq:
    print(f"'{search}' appears {freq[search]} times")
else:
    print(f"'{search}' not found")