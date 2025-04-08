import streamlit as st
import matplotlib as plt
# Titel
st.title("Mijn Dashboard")
st.header("Versie april 2025")
st.markdown("Welkom bij mijn dashboard.")
# Donutchart
labels = ['Categorie A', 'Categorie B', 'Categorie C']
sizes = [20, 30, 50]
colors = ['#FF9999', '#66B3FF', '#99FF99']

'''
# Plot
fig, ax = plt.subplots()
wedges, texts, autotexts = ax.pie(
    sizes,
    labels=labels,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    wedgeprops={'width': 0.4}
)
ax.axis('equal')  # Zorgt voor een ronde donut!

# Titel voor de grafiek
plt.title('Verdeling in procenten')

# Toon de grafiek in Streamlit
st.pyplot(fig)
'''
