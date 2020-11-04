import os

# Define the musical styles
genre = [
    'cluster_1',
    'cluster_2',
    'cluster_3',
    'cluster_4',
    'cluster_5',
]

styles = [
    [
        'data/cluster_1/Boisterous',
        'data/cluster_1/Confident',
        'data/cluster_1/Passionate',
        'data/cluster_1/Rousing',
        'data/cluster_1/Rowdy'
    ],
    [
        'data/cluster_2/Amiable_good_natured',
        'data/cluster_2/Cheerful',
        'data/cluster_2/Fun',
        'data/cluster_2/Rollicking',
        'data/cluster_2/Sweet'

    ],
    [
        'data/cluster_3/Autumnal',
        'data/cluster_3/Bittersweet',
        'data/cluster_3/Brooding',
        'data/cluster_3/Literate',
        'data/cluster_3/Poignant',
        'data/cluster_3/Wistful'
      
    ],
    [
        'data/cluster_4/Campy',
        'data/cluster_4/Humorous',
        'data/cluster_4/Silly',
        'data/cluster_4/whimsical',
        'data/cluster_4/Witty',
        'data/cluster_4/Wry'
      
    ],
    [
        'data/cluster_5/Agressive',
        'data/cluster_5/Fiery',
        'data/cluster_5/Intense',
        'data/cluster_5/Tense_Anxious',
        'data/cluster_5/Visceral',
        'data/cluster_5/Volatile'
      
    ]

]

NUM_STYLES = sum(len(s) for s in styles)

# MIDI Resolution
DEFAULT_RES = 96
MIDI_MAX_NOTES = 128
MAX_VELOCITY = 127

# Number of octaves supported
NUM_OCTAVES = 4
OCTAVE = 12

# Min and max note (in MIDI note number)
MIN_NOTE = 36
MAX_NOTE = MIN_NOTE + NUM_OCTAVES * OCTAVE
NUM_NOTES = MAX_NOTE - MIN_NOTE

# Number of beats in a bar
BEATS_PER_BAR = 4
# Notes per quarter note
NOTES_PER_BEAT = 4
# The quickest note is a half-note
NOTES_PER_BAR = NOTES_PER_BEAT * BEATS_PER_BAR

# Training parameters
BATCH_SIZE = 16
SEQ_LEN = 8 * NOTES_PER_BAR

# Hyper Parameters
OCTAVE_UNITS = 64
STYLE_UNITS = 64
NOTE_UNITS = 3
TIME_AXIS_UNITS = 256
NOTE_AXIS_UNITS = 128

TIME_AXIS_LAYERS = 2
NOTE_AXIS_LAYERS = 2

# Move file save location
OUT_DIR = 'out'
MODEL_DIR = os.path.join(OUT_DIR, 'models')
MODEL_FILE = os.path.join(OUT_DIR, 'model.h5')
SAMPLES_DIR = os.path.join(OUT_DIR, 'samples')
CACHE_DIR = os.path.join(OUT_DIR, 'cache')
