import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
#All penaltys are removed from pitstops eg 8s with 5s penalty -> 3s
baku={'circuit': ['Baku']*21,
        'pit_lane_length': [450]*21,
        'duration': [2.14, 2.19, 2.22, 2.24, 2.26, 2.3, 2.38, 2.46, 2.48, 2.5, 2.52, 2.56, 2.58, 2.68, 2.68, 2.68, 3.29, 3.34, 4.05, 4.13, 3.21],
        'team': ['RB', 'VCARB', 'RB', 'VCARB', 'FER', 'MERC', 'KICK', 'HAAS', 'WIL', 'HAAS', 'FER', 'KICK', 'WIL', 'WIL', 'ALP', 'MERC', 'ALP', 'HAAS', 'AM', 'MCL', 'AM'],
        'lap': [38, 20, 40, 29, 36, 39, 36, 2, 15, 1, 19, 26, 27, 1, 16, 18, 35, 28, 37, 37, 21]
        }
#Strolls 16.20 second pitstop has been excluded
monza= {'circuit': ['Monza']*18,
        'pit_lane_length': [620]*18,
        'duration': [1.91, 2.12, 2.18, 2.18, 2.19, 2.21, 2.22, 2.85, 2.85, 2.95, 2.96, 3.0, 3.22, 3.28, 3.29, 3.98, 5.87, 3.61],
        'team': ['MCL', 'FER', 'VCARB', 'FER', 'RB', 'RB', 'VCARB', 'ALP', 'ALP', 'MERC', 'MERC', 'WIL', 'WIL', 'AM', 'HAAS', 'KICK', 'MCL', 'HAAS'],
        'lap': [45, 33, 32, 38, 19, 37, 9, 33, 49, 28, 27, 30, 41, 20, 18, 20, 46, 51]
        }
#sainz 13.22 pitstop has been excluded
zandvoort = {
    'circuit': ['Zandvoort']*39,
    'team': [
        'FER', 'FER', 'VCARB', 'KICK', 'MERC', 'VCARB', 'MERC', 'MERC',
        'AM', 'WIL', 'AM', 'KICK', 'AM', 'MCL', 'VCARB', 'ALP',
        'KICK', 'HAAS', 'MCL', 'ALP', 'WIL', 'RB', 'RB', 'KICK',
        'RB', 'ALP', 'MERC', 'RB', 'AM', 'HAAS', 'MCL', 'WIL',
        'WIL', 'VCARB', 'ALP', 'MERC', 'MCL', 'VCARB', 'WIL'
    ],
    'duration': [
        2.10, 2.12, 2.28, 2.36, 2.44, 2.48, 2.50, 2.53,
        2.54, 2.56, 2.60, 2.62, 2.67, 2.69, 2.76, 2.76,
        2.80, 2.81, 2.83, 2.84, 2.96, 2.97, 2.99, 3.10,
        3.13, 3.17, 3.36, 3.37, 3.37, 3.64, 3.88, 3.97,
        4.19, 4.31, 4.32, 4.42, 4.83, 6.70, 5.31
    ],
    'lap': [
        22, 52, 23, 60, 53, 23, 23, 51,
        8, 23, 18, 19, 52, 23, 52, 53,
        22, 52, 23, 19, 53, 53, 53, 53,
        19, 65, 23, 23, 40, 53, 53, 65,
        23, 53, 23, 53, 53, 27, 51
    ],
    'pit_lane_length': [450]*39
}

#colapintos 11.01 pitstop has been excluded
hungary = {'circuit': ['Hungary']*28,
           'pit_lane_length': [760]*28,
           'duration': [1.94, 1.94, 1.97, 2.04, 2.09, 2.12, 2.18, 2.22, 2.28, 2.37, 2.37, 2.37, 2.4, 2.49, 2.54, 2.65, 2.67, 2.75, 2.82, 2.9, 2.9, 2.91, 2.96, 3.12, 3.16, 3.8, 7.23, 4.68],
           'team': ['MCL', 'MCL', 'RB', 'FER', 'FER', 'MCL', 'RB', 'VCARB', 'RB', 'AM', 'FER', 'RB', 'ALP', 'WIL', 'KICK', 'KICK', 'WIL', 'HAAS', 'WIL', 'MERC', 'AM', 'MERC', 'VCARB', 'MERC', 'HAAS', 'WIL', 'ALP', 'KICK'],
           'lap': [31, 45, 20, 40, 19, 18, 48, 33, 17, 36,  42, 37, 32, 14, 5, 40, 51, 30, 15, 19, 39, 43, 40, 21, 14, 38, 35, 41]
           }
spa = {
    'circuit': ['Spa']*26,
    'pit_lane_length': [600]*26,
    'duration': [
        2.17, 2.21, 2.28, 2.28, 2.31, 2.44, 2.53, 2.53, 2.58, 2.61,
        2.62, 2.67, 2.67, 2.72, 2.73, 2.80, 2.85, 2.90, 2.94, 2.96,
        3.16, 3.27, 3.44, 3.57, 3.90, 4.69
    ],
    'team': [
        'RB', 'FER', 'RB', 'MERC', 'VCARB', 'AM', 'ALP', 'MERC', 'WIL', 'WIL',
        'FER', 'MERC', 'AM', 'HAAS', 'RB', 'ALP', 'RB', 'MCL', 'VCARB', 'WIL',
        'HAAS', 'AM', 'VCARB', 'MCL', 'ALP', 'RB'
    ],

    'lap': [
        13, 11, 12, 30, 12, 11, 12, 12, 12, 12,
        12, 12, 12, 13, 13, 28, 20, 12, 11, 26,
        12, 29, 32, 13, 11, 12
    ]
}
silverstone = {
    'circuit': ['Silverstone']*34,
    'pit_lane_length': [780]*34,
    'duration': [
        2.06, 2.21, 2.23, 2.23, 2.24, 2.35, 2.38, 2.39, 2.41, 2.44,
        2.52, 2.55, 2.56, 2.59, 2.60, 2.62, 2.69, 2.72, 2.72, 2.76,
        2.80, 2.89, 2.89, 3.09, 3.13, 3.13, 3.15, 3.22, 3.32, 3.72,
        3.76, 4.11, 4.64, 4.60
    ],
    'team': [
        'RB', 'MERC', 'RB', 'ALP', 'MERC', 'MERC', 'FER', 'MCL', 'ALP', 'MERC',
        'HAAS', 'RB', 'AM', 'WIL', 'AM', 'AM', 'FER', 'HAAS', 'WIL', 'AM',
        'HAAS', 'FER', 'AM', 'HAAS', 'MERC', 'FER', 'MCL', 'WIL', 'WIL', 'VCARB',
        'RB', 'VCARB', 'MCL', 'MCL'
    ],
    'lap': [
        11, 9, 11, 41, 2, 38, 11, 44, 11, 10,
        42, 10, 37, 12, 10, 41, 42, 18, 41, 6,
        10, 10, 11, 41, 20, 41, 11, 11, 42, 9,
        41, 42, 11, 43
    ]
}

#tsunodas 10.6 seconds pitstop has been ommited
red_bull_ring = {
    'circuit': ['Red Bull Ring']*31,
    'pit_lane_length': [359]*31,
    "team": ["MCL", "RB", "FER", "RB", "ALP", "FER", "KICK", "KICK", "KICK", "FER", "VCARB", "MERC", "KICK", "FER", "MCL", "WIL", "AM", "RB", "ALP", "AM", "ALP", "MERC", "HAAS", "HAAS", "MCL", "HAAS", "MCL", "AM", "ALP", "HAAS", "VCARB"],
    "duration": [2.10, 2.18, 2.18, 2.24, 2.24, 2.24, 2.29, 2.30, 2.31, 2.32, 2.35, 2.39, 2.44, 2.45, 2.50, 2.53, 2.55, 2.75, 2.77, 2.81, 2.92, 2.93, 3.00, 3.09, 3.15, 3.17, 3.45, 3.68, 3.95, 3.98, 3.68],
    "lap": [53, 32, 50, 2, 39, 26, 49, 12, 42, 25, 18, 18, 21, 49, 52, 13, 53, 28, 38, 33, 12, 45, 39, 50, 20, 11, 24, 26, 13, 19, 60],
    }

canada = {
    'circuit': ['Canada'] * 33,
    'pit_lane_length': [741] * 33,
    "team": ["FER", "RB", "FER", "MCL", "MCL", "MCL", "VCARB", "MERC", "FER", "FER", "KICK", "MERC", "KICK", "MCL", "MERC", "AM", "WIL", "VCARB", "AM", "AM", "HAAS", "RB", "ALP", "WIL", "HAAS", "RB", "AM", "MERC", "ALP", "VCARB", "MCL", "HAAS", "AM"],
    'duration': [
    2.08, 2.12, 2.12, 2.17, 2.22, 2.24, 2.25, 2.25,
    2.27, 2.37, 2.42, 2.47, 2.49, 2.49, 2.52, 2.60,
    2.61, 2.64, 2.65, 2.67, 2.81, 2.82, 2.96, 3.00,
    3.02, 3.11, 3.21, 3.38, 3.44, 3.78, 4.02, 7.20,
    3.37
],
    "lap": [45, 38, 53, 16, 45, 29, 37, 38, 28, 15, 19, 14, 49, 47, 13, 66, 57, 12, 50, 24, 18, 66, 53, 23, 57, 13, 15, 42, 14, 56, 67, 66, 51],
}
#sainz and albons 10.88 and 11.44 second pitstops have been ommitted
barcelona = {
    'circuit': ['Barcelona'] * 52,
    'pit_lane_length': [450] * 52,
    "team": [
        "KICK", "ALP", "FER", "MCL", "ALP", "FER", "MERC", "MCL", "VCARB", "MCL", "FER", "VCARB",
        "RB", "RB", "VCARB", "MERC", "VCARB", "VCARB", "ALP", "RB", "VCARB", "ALP", "VCARB", "MERC",
        "RB", "VCARB", "KICK", "RB", "HAAS", "AM", "KICK", "FER", "HAAS", "KICK", "WIL", "HAAS",
        "FER", "AM", "ALP", "MCL", "HAAS", "WIL", "ALP", "AM", "MCL", "KICK", "HAAS", "MERC",
        "MERC", "MCL", "FER", "WIL"
    ],
    "duration": [
        2.13, 2.15, 2.17, 2.23, 2.24, 2.25, 2.27, 2.27, 2.29, 2.29, 2.29, 2.31, 2.33, 2.34, 2.34, 2.36,
        2.37, 2.40, 2.41, 2.45, 2.46, 2.47, 2.50, 2.50, 2.50, 2.54, 2.56, 2.57, 2.67, 2.68, 2.71, 2.72,
        2.77, 2.79, 2.80, 2.81, 2.81, 2.83, 2.85, 2.96, 2.98, 3.01, 3.08, 3.12, 3.33, 3.45, 3.45, 3.53,
        3.83, 3.97, 4.96, 6.94
    ],
    "lap": [19, 31, 17, 49, 54, 16, 20, 22, 44, 48, 40, 29, 44, 48, 55, 41, 8, 47, 39, 19, 24, 10, 13, 21, 55, 54, 45, 18, 8, 54, 9, 55, 43, 56, 55, 20, 55, 42, 14, 21, 35, 34, 55, 15, 55, 49, 54, 55, 49, 55, 46, 26]
,
}
#Bearman and Bortolletos 14.64 and 28.5 second pitstops have been omitted
monaco = {
    'circuit': ['Monaco'] * 37,  # You can replace 'Unknown' with the actual circuit name
    'pit_lane_length': [510] * 37,  # Replace None with actual pit lane length if known
    "team": [
        "FER", "FER", "FER", "MCL", "RB", "MCL", "MERC", "RB", "KICK", "WIL", "KICK", "MERC", "ALP", "RB",
        "WIL", "RB", "RB", "MERC", "ALP", "AM", "RB", "FER", "AM", "RB", "RB", "ALP", "KICK", "MCL", "WIL",
        "HAAS", "KICK", "HAAS", "WIL", "HAAS", "MERC", "MCL", "AM"
    ],

    "duration": [
        2.00, 2.08, 2.19, 2.23, 2.27, 2.31, 2.38, 2.41, 2.42, 2.42, 2.43, 2.43, 2.44, 2.45, 2.48, 2.50,
        2.50, 2.54, 2.55, 2.56, 2.58, 2.59, 2.60, 2.67, 2.67, 2.72, 2.74, 2.75, 2.75, 2.80, 3.03, 3.13,
        3.17, 3.22, 3.74, 3.88, 4.22
    ],
    "lap": [
        22, 18, 49, 50, 77, 48, 71, 28, 35, 40, 12, 69, 1, 73, 32, 19, 40, 68, 13, 17, 31, 56, 16, 1, 14,
        26, 26, 19, 53, 28, 44, 16, 48, 17, 62, 20, 64
    ]
}
imola = {
    'circuit': ['Imola'] * 36,
    'pit_lane_length': [540] * 36,  # Add actual pitlane length if known
    "team": [
        "FER", "RB", "RB", "RB", "MCL", "FER", "FER", "RB", "KICK", "RB",
        "MERC", "RB", "MERC", "WIL", "HAAS", "KICK", "AM", "RB", "MERC", "FER",
        "ALP", "HAAS", "WIL", "WIL", "KICK", "AM", "ALP", "ALP", "MCL", "KICK",
        "WIL", "MCL", "AM", "ALP", "AM", "MCL"
    ],
    "duration": [
        2.04, 2.09, 2.11, 2.13, 2.18, 2.18, 2.35, 2.36, 2.37, 2.37,
        2.47, 2.50, 2.52, 2.58, 2.60, 2.62, 2.63, 2.66, 2.73, 2.81,
        2.88, 2.92, 2.97, 3.08, 3.14, 3.19, 3.22, 3.25, 3.32, 3.40,
        3.41, 3.65, 3.67, 3.71, 4.13, 4.46
    ],
    "lap": [10, 29, 46, 10, 28, 46, 29, 29, 46, 29, 11, 29, 29, 47, 1, 29, 12, 46, 29, 29, 22, 29, 29, 29, 29, 46, 46, 29, 30, 12, 11, 13, 14, 9, 46, 46],
}

miami = {
    'circuit': ['Miami'] * 18,  # Update circuit name if known
    'pit_lane_length': [375] * 18,  # Add actual pitlane length if known
    'team': [
        "KICK", "MCL", "ALP", "RB", "MCL", "RB", "FER", "WIL", "RB",
        "AM", "KICK", "RB", "WIL", "HAAS", "FER", "AM", "MERC", "MERC"
    ],
    'duration': [
        2.24, 2.25, 2.31, 2.33, 2.38, 2.39, 2.39, 2.52, 2.52, 2.54,
        2.57, 2.77, 2.98, 3.08, 3.47, 3.69, 4.40, 4.51
    ],
    'lap': [
        19, 29, 32, 27, 29, 22, 29, 26, 28, 20, 36, 26, 25, 23, 28, 28, 25, 29
    ],
}
jeddah = {
    'circuit': ['Jeddah'] * 19,
    'pit_lane_length': [420] * 19,  # Approximate length in meters
    'team': [
        "FER", "FER", "MERC", "KICK", "MERC", "ALP", "AM", "VCARB", "MCL",
        "VCARB", "HAAS", "KICK", "MCL", "ALP", "AM", "HAAS", "WIL", "WIL", "RB"
    ],
    'duration': [
        2.00, 2.07, 2.32, 2.36, 2.41, 2.47, 2.55, 2.57, 2.67,
        3.13, 3.14, 3.44, 3.49, 3.62, 3.91, 4.28, 4.44, 6.44, 3.32
    ],
    'lap': [
        29, 23, 19, 33, 20, 1, 39, 20, 34,
        34, 1, 1, 19, 32, 19, 18, 22, 21, 21
    ]
}
bahrain = {
    'circuit':['Bahrain']*42,
    'pit_lane_length': [420]*42,
    "team": ['FER', 'KICK', 'MERC', 'FER', 'KICK', 'KICK', 'RB', 'MCL', 'MCL', 'AM', 'RB', 'FER', 'MERC', 'MERC', 'HAAS', 'WIL', 'WIL', 'AM', 'FER', 'HAAS', 'AM', 'MERC', 'ALP', 'ALP', 'AM', 'ALP', 'HAAS', 'WIL', 'MERC', 'RB', 'MCL', 'RB', 'ALP', 'KICK', 'HAAS', 'RB', 'WIL', 'RB', 'RB', 'RB', 'MCL', 'WIL'],
    "duration": [
        2.16, 2.24, 2.27, 2.28, 2.29, 2.29, 2.31, 2.36, 2.38, 2.44,
        2.44, 2.47, 2.49, 2.50, 2.64, 2.64, 2.65, 2.67, 2.68, 2.70,
        2.79, 2.81, 2.82, 2.82, 2.84, 2.89, 2.90, 2.93, 2.93, 2.97,
        2.98, 3.10, 3.15, 3.31, 3.57, 3.58, 3.64, 4.26, 4.72, 6.27,
        7.75, 5.16
    ],
    "lap": [
        32, 13, 13, 17, 5, 27, 32, 14, 32, 12,
        32, 32, 32, 12, 8, 32, 32, 32, 17, 27,
        16, 27, 28, 9, 32, 10, 14, 14, 32, 28,
        32, 14, 28, 32, 32, 6, 16, 11, 10, 26,
        10, 44
    ]
}

suzuka = {
    'circuit': ['Suzuka']*21,
    'pit_lane_length': [400]*21,
    "team": ["FER", "MCL", "MERC", "MCL", "FER", "RB", "ALP", "WIL", "AM", "KICK", "KICK", "WIL", "AM", "RB", "RB", "MERC", "RB", "HAAS", "HAAS", "AM", "ALP"],
    "duration": [2.18, 2.19, 2.26, 2.37, 2.40, 2.40, 2.56, 2.60, 2.63, 2.63, 2.64, 2.67, 2.73, 2.90, 2.93, 3.12, 3.32, 3.51, 3.95, 4.74, 4.80],
    "lap": [30, 20, 19, 21, 21, 25, 15, 24, 9, 31, 22, 33, 30, 23, 33, 31, 21, 32, 23, 24, 24],
    }
#tsunodas 16s pitstop has been removed
shanghai = {
    'circuit': ['Shanghai']*24,
    'pit_lane_length': [400]*24,
    "team": ["FER", "RB", "RB", "MCL", "RB", "FER", "RB", "FER", "MERC", "RB", "RB", "KICK", "MERC", "ALP", "WIL", "KICK", "HAAS", "HAAS", "RB", "ALP", "AM", "KICK", "WIL", "MCL"],
    "duration": [2.05, 2.08, 2.15, 2.27, 2.28, 2.35, 2.42, 2.43, 2.45, 2.52, 2.54, 2.69, 2.72, 2.79, 2.79, 2.79, 2.86, 2.92, 3.04, 3.13, 3.21, 3.33, 3.35, 3.83],
    "lap": [15, 11, 13, 15, 35, 37, 18, 13, 14, 30, 33, 26, 12, 11, 17, 20, 11, 26, 12, 10, 36, 1, 20, 14],
}
albert_park = {
    'circuit': ['Albert Park']*34,
    'pit_lane_length': [281]*34,
    "team": ["FER", "FER", "MERC", "RB", "HAAS", "HAAS", "FER", "RB", "RB", "RB",
             "HAAS", "MERC", "WIL", "MERC", "RB", "MCL", "HAAS", "HAAS", "AM", "AM",
             "RB", "MERC", "MCL", "FER", "ALP", "MCL", "WIL", "ALP", "MCL", "KICK",
             "HAAS", "KICK", "KICK", "KICK"],
    "duration": [2.32, 2.38, 2.43, 2.47, 2.49, 2.54, 2.55, 2.56, 2.58, 2.67, 2.69,
                   2.73, 2.75, 2.76, 2.77, 2.79, 2.80, 2.82, 2.82, 2.87, 2.94, 3.05,
                   3.19, 3.28, 3.32, 3.45, 3.54, 3.66, 3.72, 4.01, 4.95, 5.13, 5.59, 4.33],
    "lap": [34, 47, 34, 47, 4, 4, 33, 46, 4, 33, 46, 33, 33, 44, 34, 34, 44, 39, 44, 33,
            33, 44, 44, 47, 46, 44, 44, 33, 34, 44, 39, 33, 33, 44]
}



pitstops = {key: albert_park[key] + shanghai[key]+ suzuka[key] + bahrain[key] + jeddah[key] + miami[key] + imola[key] + monaco[key] + barcelona[key] + canada[key] + red_bull_ring[key]+ silverstone[key] + spa[key] + hungary[key] + zandvoort[key] + monza[key]  + baku[key] for key in baku.keys()}
for key in baku.keys():
    print(key, len(pitstops[key]))

circuits = {
    "bahrain": bahrain, "jeddah": jeddah, "miami": miami, "imola": imola,
    "monaco": monaco, "barcelona": barcelona, "canada": canada,
    "Red Bull Ring": red_bull_ring, "silverstone": silverstone, "spa": spa,
    "hungary": hungary, "zandvoort": zandvoort, "monza": monza, "baku": baku
}

for name, data in circuits.items():
    lengths = {k: len(v) for k, v in data.items()}
    print(name, lengths)
    if len(set(lengths.values())) != 1:
        print(f"⚠️  Mismatch in {name}: {lengths}")


pitstops_df = pd.DataFrame(pitstops)

palette = {
    'MCL': '#FF8000',   # bright orange
    'FER': '#FF1A1A',   # bright red
    'MERC': '#00CED1',  # bright cyan
    'RB': '#00008B',    # dark blue
    'WIL': '#0072B2',   # colorblind blue
    'AM': '#006400',    # dark green
    'KICK':'#90EE90',   # light green
    'VCARB': '#FFD700', # bright yellow
    'HAAS': '#555555',  # deep grey
    'ALP': '#FF69B4'    # bright pink
}
corr = pitstops_df['pit_lane_length'].corr(pitstops_df['duration'])
# Mean duration and pit lane length per team
team_means = pitstops_df.groupby("team")[["duration"]].mean().round(3).sort_values('duration')
team_max = pitstops_df.groupby("team")[["duration"]].max().round(3).sort_values('duration')
team_min = pitstops_df.groupby("team")[["duration"]].min().round(3).sort_values('duration')
team_std = pitstops_df.groupby("team")[["duration"]].std().round(3).sort_values('duration')
print('mean', team_means)
print('max', team_max)
print('min', team_min)
print('std', team_std)

print(f'Correlation: {corr}')
plt.figure(figsize=(20, 10))
sns.lineplot(data=pitstops_df, x='circuit', y='duration', hue='team', palette=palette, marker="o", ci=None, )
plt.title("Pit Stop Durations by Circuit")

plt.figure(figsize=(40, 40))
sns.displot(data=pitstops_df, x='duration', binwidth=0.5, hue='team', palette=palette, multiple = 'stack')
plt.show()
