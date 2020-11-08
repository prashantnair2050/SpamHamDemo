def textPreprocessor(featureRecord):
    #a.Remove Punctuation
    removePunctuation = [char for char in featureRecord if char not in string.punctuation]
    sentences = ''.join(removePunctuation)
    
    #b.Convert Sentences to Words
    words = sentences.split(" ")
    
    #c. Normalize
    wordNormalized = [word.lower() for word in words]
    
    #d. Remove Stopwords
    finalWords = [word for word in wordNormalized if word not in stopwords.words("english")]
    
    return finalWords
