import streamlit as st

st.set_page_config(page_title = "New Name")

st.title("Equipo de Desarrollo")
col1, col2= st.columns(2)
with col1:
    st.header("Lorena Barbosa Q.")
    with st.expander("Perfil"):
       st.markdown("Administradora de Empresas de la **Pontificia Universidad Javeriana** con experiencia en el sector financiero, sentido de responsabilidad, compromiso, honestidad y respeto. Competencias de trabajo en equipo, liderazgo y pensamiento analítico.")
with col2:
    st.header("Oscar W. Orozco C.")
    with st.expander("Perfil"):
        st.markdown("Profesional en Estadística con Maestría en Economía Aplicada de la **Universidad del Valle** y estudios de Especialización en Actuaría y Finanzas de la **Universidad Nacional de Colombia – Sede Manizales**. Mi experiencia relevante se centra en el desarrollo, diseño e implementación de modelos de gestión de riesgo crediticio de instrumentos financieros bajo IFRS 9, así como en procesos de revisoría fiscal y consultoría en riesgo de crédito. Cuento con experiencia en cálculo de reservas bajo IBNR. Además, poseo experiencia en el campo de la ciencia de datos, donde realizo análisis estadísticos, desde descriptivos hasta predictivos de tipo supervisado y no supervisado, utilizando lenguajes de programación como Python y R.")
