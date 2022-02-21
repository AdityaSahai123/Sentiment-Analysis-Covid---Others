import pickle

# pickling the vectorizer
pickle.dump(vectorizer, open('models/vectorizer.sav', 'wb'))
# pickling the model
# noinspection PyUnresolvedReferences
pickle.dump(classifier_linear, open('models/classifier.sav', 'wb'))

print('Both vectorizer and classifier has been pickled. Check "classifier_flask" to load and use in flask app')