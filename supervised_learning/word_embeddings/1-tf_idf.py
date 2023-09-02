#!/usr/bin/env python3
"""
this function creates a TF-IDF embedding
"""


import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


def tf_idf(sentences, vocab=None):
    """
    tf idf embedding function
    """
    if vocab is None:
        vectorizer = TfidfVectorizer()
    else:
        vectorizer = TfidfVectorizer(vocabulary=vocab)

    embeddings = vectorizer.fit_transform(sentences).toarray()
    features = vectorizer.get_feature_names_out()

    return embeddings, features
