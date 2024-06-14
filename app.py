##Creación de Entorno Virtual
##link:https://www.youtube.com/watch?v=TNtrAvNNxTY

import streamlit as st
import warnings
warnings.filterwarnings('ignore')


st.set_page_config(
    page_title = 'Análsis What If',
    page_icon = ':bar_chart:',
    layout = 'wide',
    initial_sidebar_state="collapsed"
)



def main():
    
    
    #st.sidebar.image("C:/OWOC910325/Herramienta_What_If/images/pwc_logo.jpg", use_column_width=True)
    #Inicio:Construcción del SideBar    
    #menu=["Riesgo Actuarial", "Riesgo de Crédito", "Riesgo Operativo"]
    #choice=st.sidebar.selectbox("Seleccione el Riesgo de Interés:",menu)
        #Fin:Construcción del SideBar


    # Datos económicos de ejemplo
    datos_economicos = [
        "PIB: 3.2%",
        "Inflación: 2.5%",
        "Tasa de desempleo: 8.1%",
        "Tasa de interés: 4.5%",
        "Deuda pública: 60% del PIB",
        "Balanza comercial: +$500 millones",
        "Gasto público: $200 mil millones",
        "Reservas internacionales: $100 mil millones",
        "Crecimiento del sector manufacturero: 5.2%",
        "Índice de confianza del consumidor: 70 puntos",
        "Crecimiento del mercado de valores: 12%",
        "Tipo de cambio: 1 dólar = 20 pesos",
        "Exportaciones: $300 mil millones",
        "Importaciones: $250 mil millones",
        "Tasa de ahorro: 15% del ingreso nacional",
        "Crecimiento del sector de servicios: 4.7%",
        "Tasa de inversión: 20% del PIB",
        "Déficit fiscal: 3% del PIB",
        "Crecimiento del sector agrícola: 2.8%",
        "Índice de precios de la vivienda: +2.1% en el último trimestre",
        "Tasa de cambio real: 110 puntos",
        "Consumo privado: +3.8% en el último año",
        "Gasto en investigación y desarrollo: 2% del PIB",
        "Crecimiento del sector turístico: 6.5%",
        "Expectativas de crecimiento económico: +4% para el próximo año",
        "Índice de Competitividad Global: 6 de 10",
        "Índice de Libertad Económica: 75 de 100",
        "Crecimiento del sector tecnológico: 8.3%",
        "Tasa de retorno de la inversión: 10%",
        "Tasa de crecimiento demográfico: 1.2% anual",
        "Índice de Producción Industrial: 105 puntos",
        "Evolución de la deuda externa: -$50 mil millones en el último trimestre",
        "Crecimiento del sector de la construcción: 7.2%",
        "Gasto en infraestructura: $150 mil millones",
        "Índice de Precios al Consumidor: +0.5% en el último mes",
        "Crecimiento del sector energético: 3.6%",
        "Gasto en educación: 5% del PIB",
        "Índice de Competitividad del Comercio: 80 de 100",
        "Expectativas de inflación: 3% para el próximo año",
        "Crecimiento del sector de transporte: 4.1%",
        "Índice de Competitividad Turística: 7 de 10",
        "Tasa de retorno sobre el capital invertido: 8%",
        "Crecimiento del sector de telecomunicaciones: 5.9%",
        "Tasa de crecimiento del crédito bancario: 6.8%",
        "Índice de Desarrollo Humano: 0.82",
        "Tasa de impuestos corporativos: 25%",
        "Índice de Innovación: 60 de 100",
        "Gasto en salud: 6.5% del PIB",
        "Tasa de crecimiento del consumo de energía: 2.3%",
        "Crecimiento del sector financiero: 5.4%",
        "Tasa de crecimiento de las exportaciones: 7.5%",
        "Crecimiento del sector minero: 4.8%",
        "Índice de Percepción de la Corrupción: 70 de 100",
        "Tasa de crecimiento de las importaciones: 6.2%",
        "Crecimiento del sector de seguros: 3.9%",
        "Tasa de crecimiento de las remesas: 5.7%",
        "Crecimiento del sector de bienes raíces: 6.3%",
        "Tasa de crecimiento del consumo privado: 3.5%",
        "Crecimiento del sector de alimentos y bebidas: 4.2%",
        "Tasa de crecimiento del consumo público: 2.8%",
        "Crecimiento del sector de la moda: 7.8%",
        "Tasa de crecimiento del sector automotriz: 5.1%",
        "Crecimiento del sector de la tecnología financiera: 8.7%",
        "Tasa de crecimiento del sector de la moda: 6.9%",
        "Crecimiento del sector de la biotecnología: 9.5%",
        "Tasa de crecimiento del sector de la construcción naval: 4.6%",
        "Crecimiento del sector de la inteligencia artificial: 10.2%",
        "Tasa de crecimiento del sector de la robótica: 8.9%",
        "Crecimiento del sector de la energía renovable: 7.3%",
        "Tasa de crecimiento del sector de la industria del entretenimiento: 6.5%",
        "Crecimiento del sector de la ciberseguridad: 9.8%"
    ]

    texto_economico = " ".join(datos_economicos)
    estilo_letra = """
        <style>
            .marquee-text {
                background-color: WHITE;
                font-family: Arial, sans-serif;
                font-size: 14px;
                color: #A32020;
                padding: 15px 0;
                font-weith: bold;
                border-radius: 10px;
            }
            .banner {
                background-color: #A32020;
                padding: 10px;
                border-radius: 10px;
                margin-bottom: 20px;
                font-weith: bold;
            }
            .banner h1 {
                color: white;
                text-align: center;
                font-size: 24px;
                margin: 0;
            }
        </style>
    """

    # HTML y CSS para el efecto de marquee
    html_marquee = f"""
        <div class="marquee-text" style="overflow: hidden; white-space: nowrap;">
            <marquee behavior="scroll" direction="left" scrollamount="10">
                {texto_economico}
            </marquee>
        </div>
    """

    # Mostrar el banner y el marquee en la aplicación Streamlit
    st.markdown(estilo_letra, unsafe_allow_html=True)
    st.markdown(f'<div class="banner"><h1>Variables Macroeconómicas en Colombia</h1></div>', unsafe_allow_html=True)
    st.markdown(html_marquee, unsafe_allow_html=True)


    st.title("Herramienta What If")
    st.markdown('''
    ## ¿Qué pasaría si...?            

    La aplicación "What If" te permite explorar diferentes escenarios y ver cómo podrían cambiar los resultados basados en diferentes entradas. Puedes ajustar los parámetros y ver instantáneamente cómo afectan al resultado final.

    ### Características:

    - **Interactividad**: Cambia los valores de entrada fácilmente y observa cómo cambian los resultados.
    - **Visualización dinámica**: Gráficos y tablas actualizadas en tiempo real para visualizar los resultados.
    - **Comparación de escenarios**: Compara múltiples escenarios lado a lado para tomar decisiones informadas.
    - **Personalización**: Adapta la aplicación según tus necesidades específicas mediante la configuración de parámetros.

    ¡Explora diferentes posibilidades y toma decisiones informadas con la aplicación "What If"!


                '''
                )
    
    
if __name__ == '__main__':
    main()
    


