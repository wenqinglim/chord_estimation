# Chord Estimation

Identify chords based on chroma features, using a chord vocabulary of the root note, and major/minor.

## Environment setup
In a Python virtual environment:
```
pip install -r requirements.txt
```

## Models
1. Chroma Template-based Chord Identification

- What is it?: Each chord is assumed to be made up of a triad of 3 notes from its root pitch. The chroma energy for each chord is assumed to be highest for the 3 notes.

- Why it could work?: A simple chord recognition logic, since the 3 pitches are what defines a chord anyway.


2. Single Dense Layer Classifier
- What is it?: A neural network classifier with a single hidden layer takes in all 12 chroma features as input, and outputs 1 of 24 chords.

- Why it could work?: With only 12 chroma features, a deep network is not required. A NN might work better than the Template approach since it might account for energy in other chroma bands, other than the ones in the 3 pitches that make up a chord.


## Further Improvements
- Some common errors include the inability to distinguish between (i) Major/Minor versions of the same root note, and (ii) mistaking it for its 3rd, prossibly due to its 7th note added.

- (i) can be improved perhaps with more data for the minor chords, or with information about the chords preceeding chords in the piece
- (ii) can be improved by recognizing if there are 3 or 4 notes in a chord before making predictions
- Furthermore, a combination of both models can be used (e.g. voting classifier, or add similarity score from Template method as additional feature in NN)
- Maybe evaluate the label quality, and chroma feature settings?


## Notebooks
- `1_chroma_template_method.ipynb`: Notebook with initial data exploration, train-test split, and template-based chord identification
- `2_dense_layer.ipynb`: Notebook with dense layer implementation

