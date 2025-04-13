import streamlit as st
import json

st.title("🧵 La Tradición Sikuani")
st.markdown("Una aplicación educativa para preservar, enseñar y compartir la lengua y la cultura del pueblo Sikuani.")

# Aventura narrativa (módulo expandido con más mitos, sonido e imágenes)
with st.expander("🌿 Explorar mitos Sikuani - Aventuras interactivas"):
    st.subheader("🧙‍♂️ Elige un mito para explorar")

    if "mito_seleccionado" not in st.session_state:
        st.session_state.mito_seleccionado = "El origen del fuego"
        st.session_state.aventura_paso = 0

    # Cargar mitos desde un archivo JSON externo
    try:
        with open("relatos_sikuani_interactivos.json", "r", encoding="utf-8") as f:
            mitos = json.load(f)
    except FileNotFoundError:
        st.error("❌ No se encontró el archivo 'relatos_sikuani_interactivos.json'")
        mitos = {}

    if mitos:
        st.session_state.mito_seleccionado = st.selectbox(
            "📜 Selecciona un mito:", list(mitos.keys()), index=list(mitos.keys()).index(st.session_state.mito_seleccionado))
        historia = mitos[st.session_state.mito_seleccionado]
        paso = st.session_state.aventura_paso
        paso_data = historia[paso]

        st.markdown(f"**{paso_data['texto']}**")

        if "img" in paso_data:
            st.image(paso_data["img"], use_column_width=True)
        if "audio" in paso_data:
            st.audio(paso_data["audio"])

        for i, opcion in enumerate(paso_data["opciones"]):
            if st.button(opcion, key=f"{st.session_state.mito_seleccionado}_op_{paso}_{i}"):
                if opcion == "Terminar la historia":
                    st.session_state.aventura_paso = 0
                else:
                    st.session_state.aventura_paso = min(paso + 1, len(historia) - 1)
    else:
        st.info("Carga relatos en formato JSON para comenzar a explorar.")
