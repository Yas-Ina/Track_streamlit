import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd 
# Titel
st.title("Mijn Dashboard")
st.header("Versie april 2025")
st.markdown("Welkom bij mijn donut.")
# Donutchart
labels = ['Categorie A', 'Categorie B', 'Categorie C']
sizes = [20, 30, 50]
colors = ['#FF9999', '#66B3FF', '#99FF99'] # Paars, Roze, Goud

# Plot
fig, ax = plt.subplots()
wedges, texts, autotexts = ax.pie(
    sizes,
    labels=labels,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    wedgeprops={'width': 0.2}
)
ax.axis('equal')  # Zorgt voor een ronde donut!

# Titel voor de grafiek
plt.title('Verdeling in procenten')

# Toon de grafiek in Streamlit
st.pyplot(fig)

# Titel van het dashboard
st.title("Schoenenverkoop Analyse")

# Laad de dataset
df = pd.read_csv('exclusieve_schoenen_verkoop_met_locatie.csv')

# Bekijk de eerste paar rijen van de dataset
st.write("Dataset preview:", df.head())

# Controleer of de kolom 'prijs' en 'land' bestaan
if 'prijs' in df.columns and 'land' in df.columns:
    # Bereken de gemiddelde prijs per land
    gemiddelde_prijs_per_land = df.groupby('land')['prijs'].mean()

    # Maak de grafiek
    fig, ax = plt.subplots()
    gemiddelde_prijs_per_land.plot(kind='bar', color='#800080', ax=ax)
    ax.set_title('Gemiddelde prijs per land')
    ax.set_xlabel('Land')
    ax.set_ylabel('Gemiddelde prijs')

    # Toon de grafiek in Streamlit
    st.pyplot(fig)

else:
    st.error("De dataset bevat geen 'prijs' of 'land' kolom. Controleer je bestand.")
