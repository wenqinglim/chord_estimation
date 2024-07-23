import numpy as np
from constants import chord_majmin_map


def convert_label_to_idx(chord_idx, majmin_idx):
    """
    Convert chord label to index version

    Parameters
    ----------
    chord_idx : int
        Index of chord in chroma space
    majmin_idx : int
        Index of major or minor chord
    """
    label = chord_idx * 2 + majmin_idx
    return label


def evaluate(y_true, y_pred):
    """
    Evaluate the accuracy and pitch accuracy of the model,
    where pitch accuracy is the accuracy of the chord without
    considering the major or minor.

    Parameters
    ----------
    y_true : list
        True labels
    y_pred : list
        Predicted labels
    """
    acc = np.mean(y_true == y_pred)
    pitch_acc = np.mean(y_true//2 == y_pred//2)
    return acc, pitch_acc


def evaluate_by_chord(y_true, y_pred):
    """
    Evaluate the accuracy and pitch accuracy of the model by chord.
    
    Parameters
    ----------
    y_true : pd.Series
        True labels
    y_pred : pd.Series
        Predicted labels
    """
    accuracies = []
    pitch_accuracies = []
    for i in range(24):
        acc, pitch_acc = evaluate(y_true[y_true==i], y_pred[y_true==i])

        print(f"Chord {i} - Accuracy: {acc}, Pitch accuracy: {pitch_acc}")
        accuracies.append(acc)
        pitch_accuracies.append(pitch_acc)
    return accuracies, pitch_accuracies


def get_chord_error(chord_idx, y_pred_idx, y_true_idx):
    """
    Get the chords that are mistaken for a specific chord.
    Determine the most confused chord.
    
    
    Parameters
    ----------
    chord_idx : int
        Index of chord in chroma space
    y_pred_idx : pd.Series
        Predicted labels
    y_true_idx : pd.Series
        True labels
    """
    print(f"Chord : {chord_majmin_map[chord_idx]}")
    val_counts = y_pred_idx[y_true_idx==chord_idx].value_counts(normalize=True)
    print(val_counts)
    most_confused = val_counts.index[1] # Assume most confused chord is the second most common
    print(f"Chord {chord_majmin_map[chord_idx]} is most confused with {chord_majmin_map[most_confused]}.")
    print("=====================================")