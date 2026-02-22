import streamlit as st

playas = [
    {"nombre": "Geribá", "orientacion": "Sur", "tamaño": 3, "pierde_arena": False},
    {"nombre": "Ferradura", "orientacion": "Sur", "tamaño": 2, "pierde_arena": False},
    {"nombre": "João Fernandes", "orientacion": "Norte", "tamaño": 2, "pierde_arena": False},
    {"nombre": "João Fernandinho", "orientacion": "Norte", "tamaño": 1, "pierde_arena": True},
    {"nombre": "Tartaruga", "orientacion": "Norte", "tamaño": 2, "pierde_arena": False},
    {"nombre": "Azeda", "orientacion": "Norte", "tamaño": 1, "pierde_arena": True},
    {"nombre": "Azedinha", "orientacion": "Norte", "tamaño": 0, "pierde_arena": True},
    {"nombre": "Ossos", "orientacion": "Norte", "tamaño": 1, "pierde_arena": False},
    {"nombre": "Brava", "orientacion": "Este", "tamaño": 2, "pierde_arena": False},
    {"nombre": "Praia do Forno", "orientacion": "Sudeste", "tamaño": 1, "pierde_arena": False},
    {"nombre": "Ferradurinha", "orientacion": "Sur", "tamaño": 1, "pierde_arena": True},
    {"nombre": "Manguinhos", "orientacion": "Norte", "tamaño": 3, "pierde_arena": False},
    {"nombre": "Tucuns", "orientacion": "Sur", "tamaño": 3, "pierde_arena": False},
]

st.title("🏖️ Búzios Beach Master")

viento = st.sidebar.selectbox("Viento", ["Norte", "Sur", "Este", "Oeste"])
corriente = st.sidebar.selectbox("Corriente", ["Norte", "Sur"])
marea = st.sidebar.checkbox("Marea Alta")

ranking = []
for p in playas:
    pts = 0
    if viento == "Norte" and p["orientacion"] == "Sur": pts += 100
    elif viento == "Sur" and p["orientacion"] == "Norte": pts += 100
    if corriente == "Norte":
        pts += 50
        if p["orientacion"] == "Norte": pts += 25
    if marea and p["pierde_arena"]: pts -= 40
    pts += p["tamaño"]
    ranking.append({"Playa": p["nombre"], "Puntos": pts})

ranking_final = sorted(ranking, key=lambda x: x['Puntos'], reverse=True)

st.write("### 🏆 Ranking de hoy")
for i, playa in enumerate(ranking_final[:5], 1):
    st.write(f"**{i}° {playa['Playa']}**")
    
