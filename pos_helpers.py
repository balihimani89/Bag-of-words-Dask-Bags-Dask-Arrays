from nltk import pos_tag
from nltk.corpus import wordnet as wn

def get_wnet_pos_tag(treebank_tag):
    if not isinstance(treebank_tag, tuple) or len(treebank_tag) < 2:
        return ("", wn.NOUN)
    if treebank_tag[1].startswith('J'):
        return (treebank_tag[0], wn.ADJ)
    elif treebank_tag[1].startswith('V'):
        return (treebank_tag[0], wn.VERB)
    elif treebank_tag[1].startswith('N'):
        return (treebank_tag[0], wn.NOUN)
    elif treebank_tag[1].startswith('R'):
        return (treebank_tag[0], wn.ADV)
    else:
        return (treebank_tag[0], wn.NOUN)

def tag_tokens(tokens):
    try:
        if isinstance(tokens, list) and all(isinstance(t, str) for t in tokens):
            clean_tokens = [t for t in tokens if t.isalpha()]
            if clean_tokens:
                tagged = pos_tag(clean_tokens)
                return [get_wnet_pos_tag(t) for t in tagged]
    except:
        pass
    return []

def process_partition(partition_series):
    return partition_series.map(tag_tokens)
