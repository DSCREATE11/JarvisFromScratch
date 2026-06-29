import embeddingMatrix as emb

def extract_vocab_from_corpus(corpus_file_path, target_vocab_path="vocabulary.txt"):
    unique_tokens = set()
    
    # 1. Parse the text corpus line by line
    with open(corpus_file_path, "r", encoding="utf-8") as f:
        for line in f:
            # Squeeze it through your exact regex/lowercase tokenizer
            tokens = emb.tokenize(line)
            for token in tokens:
                unique_tokens.add(token)
                
    # 2. Sort to guarantee index alignment across training sessions
    sorted_vocab = sorted(list(unique_tokens))
    
    # 3. Save out
    with open(target_vocab_path, "w", encoding="utf-8") as f:
        for word in sorted_vocab:
            f.write(f"{word}\n")
            
    print(f"Extracted {len(sorted_vocab)} unique tokens from corpus.")
    print(len(sorted_vocab))
    print(sorted_vocab[1:50])
extract_vocab_from_corpus("BNCCorpus.txt")
