# map index to chord
chords = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
chord_map = {i: chord for i, chord in enumerate(chords)}
majmin_map = {0: 'maj', 1: 'min'}
chord_majmin_map = {i: chord_map[i // 2] + majmin_map[i % 2] for i in range(24)}