#!/usr/bin/env python3
"""
this function creates and trains a genism fastText model
"""


from gensim.models import FastText

def fasttext_model(sentences, size=100, min_count=5, negative=5, window=5, cbow=True, iterations=5, seed=0, workers=1):
    """
    fasttext embedding model funct
    """
    model = FastText(
        sentences=sentences,
        vector_size=size,
        min_count=min_count,
        negative=negative,
        window=window,
        sg=0 if cbow else 1,  # sg=0 for CBOW, sg=1 for Skip-gram
        epochs=iterations,
        seed=seed,
        workers=workers
    )
    model.train(sentences, total_examples=model.corpus_count, epochs=model.epochs)
    return model
