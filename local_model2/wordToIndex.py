STOP_WORDS = {
    # Articles & Demonstratives
    "a", "an", "the", "this", "that", "these", "those",
    
    # Prepositions
    "in", "on", "at", "to", "from", "by", "for", "with", "about", "into", 
    "through", "over", "under", "above", "below", "of", "off", "out",
    
    # Pronouns & Possessives
    "i", "me", "my", "myself", "you", "your", "yours", "yourself", "yourselves",
    "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", 
    "itself", "they", "them", "their", "theirs", "themselves", "we", "us", "our", 
    "ours", "ourselves", "who", "whom", "whose", "which", "what",
    
    # Conjunctions
    "and", "but", "or", "nor", "so", "yet", "as", "if", "while", "because", "until",
    
    # Helper Verbs / Copulas (Be, Do, Have)
    "is", "am", "are", "was", "were", "be", "been", "being",
    "do", "does", "did", "doing", "done",
    "have", "has", "had", "having",
    
    # Polite Filler Words / Conversational Padding
    "please", "could", "would", "should", "kindly", "mind", "ahead", "hey", "hello"
}

def build_vocabulary(filename):
    with open( filename, "r") as fp:
        words = []
        for line in fp:
            tokens = line.split()
            if tokens:
                words.append(tokens[0].lower())
        fp.close()

    words_to_index = {}
    for index, word in enumerate(words):
        words_to_index[word] = index
    return (words, words_to_index)


