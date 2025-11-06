# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Get started with interactive Python!
# Supports Python Modules: builtins, math,pandas, scipy 
# matplotlib.pyplot, numpy, operator, processing, pygal, random, 
# re, string, time, turtle, urllib.request
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error as MSE
#singapore
italy_fp1 = {
    "FP1_POS": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    
    "NO": [44, 16, 55, 1, 12, 4, 23, 63, 14, 6,
           5, 27, 30, 22, 18, 89, 31, 10, 87, 61],
    
    "DRIVER": [
        "Lewis Hamilton", "Charles Leclerc", "Carlos Sainz", "Max Verstappen", "Kimi Antonelli",
        "Lando Norris", "Alexander Albon", "George Russell", "Fernando Alonso", "Isack Hadjar",
        "Gabriel Bortoleto", "Nico Hulkenberg", "Liam Lawson", "Yuki Tsunoda", "Lance Stroll",
        "Alexander Dunne", "Esteban Ocon", "Pierre Gasly", "Oliver Bearman", "Paul Aron"
    ],
    
    "TEAM": [
        "Ferrari", "Ferrari", "Williams", "Red Bull Racing", "Mercedes",
        "McLaren", "Williams", "Mercedes", "Aston Martin", "Racing Bulls",
        "Kick Sauber", "Kick Sauber", "Racing Bulls", "Red Bull Racing", "Aston Martin",
        "McLaren", "Haas", "Alpine", "Haas", "Alpine"
    ],
    
    "FP1_TIME/GAP": [
    0.0, 0.169, 0.533, 0.575, 0.823,
    0.904, 0.956, 0.993, 0.997, 1.041,
    1.055, 1.062, 1.084, 1.175, 1.178,
    1.489, 1.525, 1.536, 1.941, 2.036
]
,
    
    "FP1_LAPS": [
        20, 24, 25, 22, 25,
        28, 25, 20, 20, 25,
        24, 26, 27, 24, 26,
        26, 22, 26, 23, 23
    ]
}

italy_fp2 = {
    "FP2_POS": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    "NO": [4, 16, 55, 81, 44, 1, 23, 27, 22, 63, 6, 5, 18, 87, 14, 31, 30, 10, 12, 43],
    "DRIVER": [
        "Lando Norris", "Charles Leclerc", "Carlos Sainz", "Oscar Piastri", "Lewis Hamilton",
        "Max Verstappen", "Alexander Albon", "Nico Hulkenberg", "Yuki Tsunoda", "George Russell",
        "Isack Hadjar", "Gabriel Bortoleto", "Lance Stroll", "Oliver Bearman", "Fernando Alonso",
        "Esteban Ocon", "Liam Lawson", "Pierre Gasly", "Kimi Antonelli", "Franco Colapinto"
    ],
    "TEAM": [
        "McLaren", "Ferrari", "Williams", "McLaren", "Ferrari", "Red Bull Racing", "Williams",
        "Kick Sauber", "Red Bull Racing", "Mercedes", "Racing Bulls", "Kick Sauber", "Aston Martin",
        "Haas", "Aston Martin", "Haas", "Racing Bulls", "Alpine", "Mercedes", "Alpine"
    ],
    "FP2_TIME/GAP": [
        0, 0.083, 0.096, 0.181, 0.192, 0.199, 0.301, 0.363, 0.391, 0.398,
        0.505, 0.597, 0.650, 0.729, 0.767, 0.776, 0.933, 1.224, 1.489, 1.686
    ],
    "FP2_LAPS": [28, 29, 30, 29, 26, 27, 28, 27, 28, 29, 24, 25, 28, 29, 26, 29, 25, 30, 4, 30]
}

italy_fp3 = {
    "FP3_POS": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    "NO": [4, 16, 81, 1, 63, 5, 44, 6, 12, 23, 27, 14, 55, 43, 22, 30, 87, 10, 18, 31],
    "DRIVER": [
        "Lando Norris", "Charles Leclerc", "Oscar Piastri", "Max Verstappen", "George Russell",
        "Gabriel Bortoleto", "Lewis Hamilton", "Isack Hadjar", "Kimi Antonelli", "Alexander Albon",
        "Nico Hulkenberg", "Fernando Alonso", "Carlos Sainz", "Franco Colapinto", "Yuki Tsunoda",
        "Liam Lawson", "Oliver Bearman", "Pierre Gasly", "Lance Stroll", "Esteban Ocon"
    ],
    "TEAM": [
        "McLaren", "Ferrari", "McLaren", "Red Bull Racing", "Mercedes",
        "Kick Sauber", "Ferrari", "Racing Bulls", "Mercedes", "Williams",
        "Kick Sauber", "Aston Martin", "Williams", "Alpine", "Red Bull Racing",
        "Racing Bulls", "Haas", "Alpine", "Aston Martin", "Haas"
    ],
    "FP3_TIME/GAP": [
        0, 0.021, 0.165, 0.167, 0.184, 0.227, 0.267, 0.272, 0.365, 0.389,
        0.406, 0.530, 0.576, 0.703, 0.728, 0.801, 0.878, 0.916, 0.916, 0.973
    ],
    "FP3_LAPS": [21, 24, 22, 18, 19, 18, 23, 20, 24, 23, 18, 19, 23, 22, 24, 14, 22, 23, 22, 20]
}

italy_quali = {
    "Quali_POS": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    "NO": [1, 4, 81, 16, 44, 63, 12, 5, 14, 22, 87, 27, 55, 23, 31, 6, 18, 43, 10, 30],
    "DRIVER": [
        "Max Verstappen", "Lando Norris", "Oscar Piastri", "Charles Leclerc", "Lewis Hamilton",
        "George Russell", "Kimi Antonelli", "Gabriel Bortoleto", "Fernando Alonso", "Yuki Tsunoda",
        "Oliver Bearman", "Nico Hulkenberg", "Carlos Sainz", "Alexander Albon", "Esteban Ocon",
        "Isack Hadjar", "Lance Stroll", "Franco Colapinto", "Pierre Gasly", "Liam Lawson"
    ],
    "TEAM": [
        "Red Bull Racing", "McLaren", "McLaren", "Ferrari", "Ferrari",
        "Mercedes", "Mercedes", "Kick Sauber", "Aston Martin", "Red Bull Racing",
        "Haas", "Kick Sauber", "Williams", "Williams", "Haas",
        "Racing Bulls", "Aston Martin", "Alpine", "Alpine", "Racing Bulls"
    ],
    ],
    "Quali Time": [
        0.000, 0.077, 0.190, 0.215, 0.332,
        0.365, 0.408, 0.598, 0.632, 0.727,
        0.654, 0.706, 0.736, 0.791, 0.915,
        1.125, 1.156, 1.200, 1.311, 1.487
    ]
}


baku_fp1 = {
    "FP1_POS": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    
    "NO": [4, 81, 16, 63, 23, 22, 1, 55, 30, 6,
           12, 27, 44, 5, 14, 87, 18, 31, 43, 10],
    
    "DRIVER": [
        "Lando Norris", "Oscar Piastri", "Charles Leclerc", "George Russell", "Alexander Albon",
        "Yuki Tsunoda", "Max Verstappen", "Carlos Sainz", "Liam Lawson", "Isack Hadjar",
        "Kimi Antonelli", "Nico Hulkenberg", "Lewis Hamilton", "Gabriel Bortoleto", "Fernando Alonso",
        "Oliver Bearman", "Lance Stroll", "Esteban Ocon", "Franco Colapinto", "Pierre Gasly"
    ],
    
    "TEAM": [
        "McLaren", "McLaren", "Ferrari", "Mercedes", "Williams",
        "Red Bull Racing", "Red Bull Racing", "Williams", "Racing Bulls", "Racing Bulls",
        "Mercedes", "Kick Sauber", "Ferrari", "Kick Sauber", "Aston Martin",
        "Haas", "Aston Martin", "Haas", "Alpine", "Alpine"
    ],
    
    "FP1_TIME/GAP": [
        0.000, 0.310, 0.552, 0.553, 0.859,
        1.034, 1.086, 1.155, 1.199, 1.271,
        1.281, 1.282, 1.383, 1.383, 1.435,
        1.447, 1.625, 1.735, 2.595, 2.714
    ],
    
    "FP1_LAPS": [
        19, 14, 17, 16, 17,
        16, 15, 17, 17, 17,
        17, 18, 14, 18, 15,
        17, 15, 15, 14, 17
    ]
}

baku_fp2 = {
    "FP2_POS": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    
    "NO": [44, 16, 63, 12, 87, 1, 30, 31, 23, 4,
           55, 81, 6, 22, 5, 10, 18, 27, 14, 43],
    
    "DRIVER": [
        "Lewis Hamilton", "Charles Leclerc", "George Russell", "Kimi Antonelli", "Oliver Bearman",
        "Max Verstappen", "Liam Lawson", "Esteban Ocon", "Alexander Albon", "Lando Norris",
        "Carlos Sainz", "Oscar Piastri", "Isack Hadjar", "Yuki Tsunoda", "Gabriel Bortoleto",
        "Pierre Gasly", "Lance Stroll", "Nico Hulkenberg", "Fernando Alonso", "Franco Colapinto"
    ],
    
    "TEAM": [
        "Ferrari", "Ferrari", "Mercedes", "Mercedes", "Haas",
        "Red Bull Racing", "Racing Bulls", "Haas", "Williams", "McLaren",
        "Williams", "McLaren", "Racing Bulls", "Red Bull Racing", "Kick Sauber",
        "Alpine", "Aston Martin", "Kick Sauber", "Aston Martin", "Alpine"
    ],
    
    "FP2_TIME/GAP": [
        0.000, 0.074, 0.477, 0.486, 0.598,
        0.609, 0.696, 0.874, 0.884, 0.906,
        0.962, 1.002, 1.150, 1.151, 1.268,
        1.381, 1.478, 1.527, 1.674, 2.029
    ],
    
    "FP2_LAPS": [
        21, 23, 19, 22, 23,
        22, 22, 23, 24, 7,
        24, 23, 23, 22, 22,
        22, 24, 22, 24, 22
    ]
}

baku_fp3 = {
    "FP3_POS": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    
    "NO": [4, 1, 81, 44, 12, 63, 23, 87, 30, 16,
           6, 27, 55, 14, 43, 22, 31, 5, 10, 18],
    
    "DRIVER": [
        "Lando Norris", "Max Verstappen", "Oscar Piastri", "Lewis Hamilton", "Kimi Antonelli",
        "George Russell", "Alexander Albon", "Oliver Bearman", "Liam Lawson", "Charles Leclerc",
        "Isack Hadjar", "Nico Hulkenberg", "Carlos Sainz", "Fernando Alonso", "Franco Colapinto",
        "Yuki Tsunoda", "Esteban Ocon", "Gabriel Bortoleto", "Pierre Gasly", "Lance Stroll"
    ],
    
    "TEAM": [
        "McLaren", "Red Bull Racing", "McLaren", "Ferrari", "Mercedes",
        "Mercedes", "Williams", "Haas", "Racing Bulls", "Ferrari",
        "Racing Bulls", "Kick Sauber", "Williams", "Aston Martin", "Alpine",
        "Red Bull Racing", "Haas", "Kick Sauber", "Alpine", "Aston Martin"
    ],
    
    "FP3_TIME/GAP": [
        0.000, 0.222, 0.254, 0.276, 0.653,
        0.741, 0.760, 0.762, 0.923, 0.986,
        1.044, 1.205, 1.263, 1.368, 1.566,
        1.617, 1.645, 1.837, 2.099, 2.127
    ],
    
    "FP3_LAPS": [
        19, 19, 21, 18, 17,
        17, 19, 23, 21, 19,
        22, 17, 17, 17, 19,
        18, 20, 16, 21, 17
    ]
}

baku_quali = {
    "Quali_POS": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            11, 12, 13, 14, 15, 16, 17, 18, 19],
    "NO": [1, 55, 30, 12, 63, 22, 4, 6, 81, 16, 14, 44, 5, 18, 87, 43, 27, 10, 23],
    
    "DRIVER": [
        "Max Verstappen", "Carlos Sainz", "Liam Lawson", "Kimi Antonelli", "George Russell",
        "Yuki Tsunoda", "Lando Norris", "Isack Hadjar", "Oscar Piastri", "Charles Leclerc",
        "Fernando Alonso", "Lewis Hamilton", "Gabriel Bortoleto", "Lance Stroll", "Oliver Bearman",
        "Franco Colapinto", "Nico Hulkenberg", "Pierre Gasly", "Alexander Albon"
    ],
    
    "TEAM": [
        "Red Bull Racing", "Williams", "Racing Bulls", "Mercedes", "Mercedes",
        "Red Bull Racing", "McLaren", "Racing Bulls", "McLaren", "Ferrari",
        "Aston Martin", "Ferrari", "Kick Sauber", "Aston Martin", "Haas",
        "Alpine", "Kick Sauber", "Alpine", "Williams"
    ],
    
    "Quali Time": [
        0.000,    # 101.117 - 101.117
        0.478,    # 101.595 - 101.117
        0.420,    # 101.537 - 101.117
        0.347,    # 101.464 - 101.117
        0.338,    # 101.455 - 101.117
        0.671,    # 101.788 - 101.117
        0.205,    # 101.322 - 101.117
        0.530,    # 101.647 - 101.117
        0.297,    # 101.414 - 101.117
        0.341,    # 101.458 - 101.117
        0.740,    # 101.857 - 101.117
        0.704,    # 101.821 - 101.117
        1.160,    # 102.277 - 101.117
        0.984,    # 102.101 - 101.117
        1.549,    # 102.666 - 101.117
        1.662,    # 102.779 - 101.117
        1.799,    # 102.916 - 101.117
        2.022,    # 103.139 - 101.117
        2.661 
    ]
}

singapore_fp1 = {
    "FP1_POS": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    
    "NO": [14, 16, 1, 44, 81, 4, 6, 55, 22, 31,
           63, 27, 10, 12, 30, 87, 5, 18, 43, 23],
    
    "DRIVER": [
        "Fernando Alonso", "Charles Leclerc", "Max Verstappen", "Lewis Hamilton", "Oscar Piastri",
        "Lando Norris", "Isack Hadjar", "Carlos Sainz", "Yuki Tsunoda", "Esteban Ocon",
        "George Russell", "Nico Hulkenberg", "Pierre Gasly", "Kimi Antonelli", "Liam Lawson",
        "Oliver Bearman", "Gabriel Bortoleto", "Lance Stroll", "Franco Colapinto", "Alexander Albon"
    ],
    
    "TEAM": [
        "Aston Martin", "Ferrari", "Red Bull Racing", "Ferrari", "McLaren",
        "McLaren", "Racing Bulls", "Williams", "Red Bull Racing", "Haas",
        "Mercedes", "Kick Sauber", "Alpine", "Mercedes", "Racing Bulls",
        "Haas", "Kick Sauber", "Aston Martin", "Alpine", "Williams"
    ],
    
    "FP1_TIME/GAP": [
    0.0, 0.150, 0.27, 0.364, 0.365,
    0.582, 0.639, 0.696, 0.744, 1.012,
    1.023, 1.199, 1.262, 1.283, 1.345,
    1.422, 1.495, 1.918, 2.208, 2.0
]
,
    
    "FP1_LAPS": [
        23, 25, 24, 23, 25,
        22, 28, 27, 25, 24,
        22, 29, 26, 24, 27,
        25, 27, 18, 26, None
    ]
}

singapore_fp2 = {
    "FP2_POS": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    
    "NO": [81, 6, 1, 14, 4, 18, 31, 55, 16, 44,
           22, 87, 23, 27, 5, 10, 30, 12, 43, 63],
    
    "DRIVER": [
        "Oscar Piastri", "Isack Hadjar", "Max Verstappen", "Fernando Alonso", "Lando Norris",
        "Lance Stroll", "Esteban Ocon", "Carlos Sainz", "Charles Leclerc", "Lewis Hamilton",
        "Yuki Tsunoda", "Oliver Bearman", "Alexander Albon", "Nico Hulkenberg", "Gabriel Bortoleto",
        "Pierre Gasly", "Liam Lawson", "Kimi Antonelli", "Franco Colapinto", "George Russell"
    ],
    
    "TEAM": [
        "McLaren", "Racing Bulls", "Red Bull Racing", "Aston Martin", "McLaren",
        "Aston Martin", "Haas", "Williams", "Ferrari", "Ferrari",
        "Red Bull Racing", "Haas", "Williams", "Kick Sauber", "Kick Sauber",
        "Alpine", "Racing Bulls", "Mercedes", "Alpine", "Mercedes"
    ],
    
    "FP2_TIME/GAP": [
    0.0, 0.132, 0.143, 0.163, 0.483,
    0.508, 0.584, 0.585, 0.752, 0.777,
    0.994, 0.997, 1.346, 1.355, 1.605,
    1.744, 1.931, 2.005, 2.425, 2.517
]
,
    
    "FP2_LAPS": [
        19, 19, 19, 19, 18,
        18, 19, 20, 18, 17,
        18, 18, 19, 19, 19,
        20, 10, 18, 20, 6
    ]
}

singapore_fp3 = {
    "FP3_POS": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    
    "NO": [1, 81, 63, 12, 4, 55, 6, 44, 27, 16,
            23, 5, 31, 87, 14, 43, 18, 22, 10, 30],
    
    "DRIVER": [
        "Max Verstappen", "Oscar Piastri", "George Russell", "Kimi Antonelli", "Lando Norris",
        "Carlos Sainz", "Isack Hadjar", "Lewis Hamilton", "Nico Hulkenberg", "Charles Leclerc",
        "Alexander Albon", "Gabriel Bortoleto", "Esteban Ocon", "Oliver Bearman", "Fernando Alonso",
        "Franco Colapinto", "Lance Stroll", "Yuki Tsunoda", "Pierre Gasly", "Liam Lawson"
    ],
    
    "TEAM": [
        "Red Bull Racing", "McLaren", "Mercedes", "Mercedes", "McLaren",
        "Williams", "Racing Bulls", "Ferrari", "Kick Sauber", "Ferrari",
        "Williams", "Kick Sauber", "Haas", "Haas", "Aston Martin",
        "Alpine", "Aston Martin", "Red Bull Racing", "Alpine", "Racing Bulls"
    ],
    
    "FP3_TIME/GAP": [0.0, 0.017, 0.049, 0.089, 0.089, 0.244, 0.341, 0.411, 0.489, 0.503,
 0.52, 0.549, 0.636, 0.651, 0.775, 0.899, 1.112, 1.292, 1.495, 3.48],
    
    "FP3_LAPS": [15, 25, 17, 18, 25, 22, 24, 22, 22, 22,
             23, 24, 23, 24, 21, 22, 23, 24, 22, 7]
}






fp1 = {key: italy_fp1[key] + baku_fp1[key] for key in italy_fp1.keys()}
fp2 = {key: italy_fp2[key] + baku_fp2[key] for key in italy_fp2.keys()}
fp3 = {key: italy_fp3[key] + baku_fp3[key] for key in italy_fp3.keys()}
quali = {key: italy_quali[key] + baku_quali[key] for key in italy_quali.keys()}
 


X = results_df[['FP1_LAPS', 'FP1_TIME/GAP', 'FP2_LAPS', 'FP2_TIME/GAP', 'FP3_LAPS', 'FP3_TIME/GAP']]
y = results_df['Quali Time']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=1)


lr = LinearRegression()

lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)
r2 = r2_score(y_test, y_pred)
print(f'r2 score: {r2}')



#Exploritary Data Analysis
corr = results_df['FP1_TIME/GAP'].corr(results_df['FP1_LAPS'])

print(f'correlation: {corr}')

palette = {
    'McLaren': '#FF8000',   # bright orange
    'Ferrari': '#FF1A1A',   # bright red
    'Mercedes': '#00CED1',  # bright cyan
    'Red Bull Racing': '#00008B',    # dark blue
    'Williams': '#0072B2',   # colorblind blue
    'Aston Martin': '#006400',    # dark green
    'Kick Sauber':'#90EE90',   # light green
    'Racing Bulls': '#FFD700', # bright yellow
    'Haas': '#555555',  # deep grey
    'Alpine': '#FF69B4'    # bright pink
}


plt.figure(figsize=(10, 6))
sns.scatterplot(
    x='FP1_TIME/GAP',
    y='FP1_LAPS',
    data=results_df,
    hue='TEAM',              # Color points by TEAM
    palette=palette,         # Choose a color palette
    s=100                    # Increase point size for clarity
)


sns.regplot(
    x='FP1_TIME/GAP',
    y='FP1_LAPS',
    data=results_df,
    scatter=False,           # Only show the line
    color='black'            # Line color
)

plt.title('Laps vs Time Gap by Team')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')  # Move legend outside plot
plt.tight_layout()
plt.show()
