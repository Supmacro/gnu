import re

regex = {
    'alphanum_underscore': re.compile(r'(\w+)$'),
    'many_punctuations': re.compile(r'([^():,\s]+)$'),
    'most_punctuations': re.compile(r'([^\.():,\s]+)$'),
    'all_punctuations': re.compile(r'([^\s]+)$')
}

def plast_word(text, ex='alphanum_underscore'):
    """
    Find the last word in a sentence
    """
    if not text or text[-1].isspace():
        return ''
    
    rule = regex[ex]
    word = rule.search(text)
    
    if word:
        return word.group(0)
    else:
        return ''        
