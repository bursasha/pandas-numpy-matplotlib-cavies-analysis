# Configuration for specific topic-related parameters.
topic_config = {
    # Integer representing a specific day, used in various calculations.
    'BIRTH_DAY': 3,

    # Length of the specified surname, used in calculations.
    'SURNAME_LEN': len('Burakov')
}

# Configuration for dataset-related parameters.
dataset_config = {
    # Relative path to the dataset file.
    'PATH': '../dataset/cavy-dataset.csv',

    # Separator used in the CSV file (e.g., comma, semicolon).
    'SEP': ';'
}

# Configuration for histogram appearance in plots.
histogram_config = {
    # Number of bins in the histogram.
    'BINS': 65,

    # Boolean indicating whether to normalize histogram (True) or not (False).
    'DENSITY': True,

    # Alpha (transparency) level of the histogram bars.
    'ALPHA': 0.3,

    # Color of the histogram bars.
    'COLOR': 'green',

    # Color of the edges of the histogram bars.
    'EDGE_COLOR': 'black'
}

# Configuration for Empirical Distribution Function (EDF) appearance in plots.
edf_config = {
    # Color of the EDF line.
    'COLOR': 'gold',

    # Width of the EDF line.
    'LINE_WIDTH': 3
}

# Configuration for distribution line appearance in comparison plots.
distribution_config = {
    # Color of the distribution line.
    'COLOR': 'red',

    # Width of the distribution line.
    'LINE_WIDTH': 3
}
