# Since there is no "easy" way of defining notes mathematically (involving
# square roots and double imprecision), and  since there involves an unnecessary
# amount of edge cases in checking particular constraints for notes, we
# just use a note mapping for both frequency and for note checking

# For simplicity, we choose to interpret the frequencies as decimals
# rounded to two digit precision. In more scientific settings, more precise
# definitions would be desired
note_mappings = {"A0": 27.5, "A#0": 29.14, "Bb0": 29.14, "B0": 30.87,
                 "C1": 32.7, "C#1": 34.65, "Db1": 34.65, "D1": 36.71,
                 "D#1": 38.89, "Eb1": 38.89, "E1": 41.2, "F1": 43.65,
                 "F#1": 46.25, "Gb1": 46.25, "G1": 49, "G#1": 51.91,
                 "Ab1": 51.91, "A1": 55, "A#1": 58.27, "Bb1": 58.2,
                 "B1": 61.74, "C2": 65.41, "C#2": 69.3, "D2": 73.42,
                 "D#2": 77.78, "Eb2": 77.78, "E2": 82.41, "F2": 87.31,
                 "F#2": 92.5, "Gb2": 92.5, "G2": 98, "G#2": 103.83,
                 "Ab2": 103.83, "A2": 110, "A#2": 116.54, "Bb2": 116.54,
                 "B2": 123.81, "C3": 130.81, "C#3": 138.59, "Db3": 138.59,
                 "D3": 146.83, "D#3": 155.56, "Eb3": 155.56, "E3": 164.81,
                 "F3": 174.61, "F#3": 185, "Gb3": 185, "G3": 196, "G#3": 207.65,
                 "Ab3": 207.65, "A3": 220, "A#3": 233.08, "Bb3": 233.08,
                 "B3": 246.94, "C4": 261.63, "C#4": 277.18, "Db4": 277.18,
                 "D4": 293.66, "D#4": 311.13, "Eb4": 311.13, "E4": 329.63,
                 "F4": 349.23, "F#4": 370, "Gb4": 370, "G4": 392,
                 "G#4": 415.3, "Ab4": 415.3, "A4": 440, "A#4": 466.16,
                 "Bb4": 466.16, "B4": 493.88, "C5": 523.25, "C#5": 554.37,
                 "Db5": 554.37, }

class Note:
    """A Note is a simplified representation of a music note. Each note contains
    a pitch and a duration which is the recommended play time for the note. We
    choose arbitrary definitions of A0 and C8 to be the respective "min" and
    "max" values that notes can take, as they follow the range of an 88-key
     piano. Any notes above or below this range are invalid."""

    def __init__(self, pitch):
        """Creates a note to be used for the maze.

        Args:
            pitch(str): the note in string form. The note must be of the form
            "A5" or "A#2".
        Raises:
            ValueError: If the note is not within supported range or if it is
             an invalid format."""

class _NoteCollector:
    """This class serves the purpose of allowing for O(1) generation of notes,
    as well as O(1) generation of sharper or flatter notes. This class was
    designed as a memory tradeoff for creating these O(1) runtimes. The class
    itself should be not be exposed to the public, as this is an internal
    detail."""

    def __init__(self):
        self.pitch_mappings = {}
        self.list = None

    def add_node(self, pitch, name):
        """Adds another node to the note collector and connects the node to
        the previous last node."""
        pass

    def add_enharmonic_node(self, pitch, name, alt_name):
        """Adds another node to the note collect and connects the node to
        the previous last node. This is different from adding a normal node in
        that the alternative name for a node is also accounted for."""


class _MusicNode:
    """This class represents a node with information regarding the note's
    pitch and its name."""

    def __init__(self, pitch, name, alt_name=None):
        self.prev = None
        self.next = None
        self.pitch = pitch
        self.name = name
        self.alt_name = alt_name

    def add_next(self, node):
        """Connects the given node as this node's next node.

        Args:
            node(_MusicNode): the music node to be seen as the next"""
        self.next = node

    def add_prev(self, node):
        """Connects the given as this node's prev node.

        Args:
            node(_MusicNode): the music node to be seen as the prev"""
        self.prev = node


class _SentinelMusicNode:
    pass
