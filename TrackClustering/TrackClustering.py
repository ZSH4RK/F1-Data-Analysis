import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import seaborn as sns

url = 'https://raw.githubusercontent.com/toUpperCase78/formula1-datasets/master/Formula1_2024season_calendar.csv'
df = pd.read_csv(url)
df['Lap Record'] = df['Lap Record'].apply(lambda t: int(t.split(':')[0]) * 60 + float(t.split(':')[1]))

features = ['Circuit Length(km)', 'Turns', 'DRS Zones']
X = df[features].copy()
X = X.dropna()


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Elbow Method to find optimal k
inertia = []
K_range = range(1, 10)
for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(K_range, inertia, 'bo-')
plt.xlabel('Number of clusters k')
plt.ylabel('Inertia (Distortion)')
plt.title('Elbow Method for Optimal k')
plt.grid(True)
#plt.show()

k_final = 4
kmeans = KMeans(n_clusters=k_final, random_state=42)
df['cluster'] = kmeans.fit_predict(X_scaled)

plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df, x='Circuit Length(km)', y='Turns',
    hue='cluster', palette='Set2', s=100
)
plt.title('F1 Tracks Clustered by Length and Turns')
plt.xlabel('Track Length (km)')
plt.ylabel('Number of Turns')
plt.legend(title='Cluster')
plt.show()


for c in range(k_final):
    print(f"\nCluster {c} examples:")
    print(df[df['cluster'] == c][['Circuit Name', 'City', 'Country', 'Circuit Length(km)', 'Turns', 'DRS Zones']].head(3))
