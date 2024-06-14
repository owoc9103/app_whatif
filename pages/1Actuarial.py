import streamlit as st
import datetime
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from itertools import accumulate
st.set_page_config(page_title="Riesgo Actuarial", page_icon="🌍")

def main():
    st.title("Riesgo Actuarial")
    st.image("images/Actuary.jpg")
    st.write("El enfoque del siguiente riesgo está relacionado con todo lo que tiene que ver con la parte de la estimación de reservas en salud. Es decir que comprende las normas que le apliquen, como lo son las siguientes:")
    
    st.markdown("[Visita la documentación correspondiente](https://www.alcaldiabogota.gov.co/sisjur/normas/Norma1.jsp?i=82267&dt=S)")
    
    st.title("1. Cálculo de Reserva IBNR y Backtesting ")
    st.header("1.1 IBNR 📚")
    st.markdown("""El cálculo de **IBNR** (Incurred But Not Reported) es una técnica utilizada en seguros y gestión de riesgos para estimar la cantidad de reclamaciones que han ocurrido durante un período determinado pero que aún no han sido reportadas a la compañía de seguros. En términos generales, IBNR representa las reclamaciones que ya han ocurrido, pero que aún no se han registrado en los libros contables de la compañía de seguros porque aún no se han reportado formalmente. Esto puede ocurrir debido a demoras en el proceso de presentación de reclamaciones por parte de los asegurados o a demoras en la notificación de las reclamaciones por parte de los intermediarios o agentes de seguros.\\
    El cálculo de IBNR generalmente implica el uso de técnicas estadísticas y modelos matemáticos para estimar la cantidad de reclamaciones no reportadas. Estos modelos pueden basarse en el análisis de datos históricos de reclamaciones, considerando factores como la frecuencia y la gravedad de las reclamaciones, así como las tendencias observadas en el comportamiento de los asegurados.\
    La estimación precisa de **IBNR** es crucial para las compañías de seguros, ya que afecta directamente a la reserva de pérdidas que deben mantener para cubrir reclamaciones futuras. Una estimación incorrecta de IBNR puede tener consecuencias financieras significativas para la compañía, ya sea en forma de reservas insuficientes o excesivas. Por lo tanto, los actuarios y analistas de riesgos dedican una atención considerable al desarrollo de métodos precisos para calcular el IBNR. """)

    st.header("1.2 Backtestig 🧠 ")
    
    with st.expander("Definicion 1"):
        st.latex(r'''
                 \small
                Actual_{i}(\$) = (C_{i,n}^{Actual}-C_{i,n}^{Anterior})
                    ''')
            
        st.latex(r'''
                 \small
                    Expected_{i}(\$)=  \left( \frac{\% dev_{i}^{Actual}- \% dev_{i}^{Anterior}}{1-\%dev_{i}^{Anterior}} \right) * (UPE_{i}^{Anterior}-C_{i,n}^{Anterior})
                    ''')
            
        st.latex(r'''
                 \small
                    AvE_{i}(\$)=  Actual_{i}(\$) - Expected_{i} (\$)
                    ''')
        
        st.latex(r'''
                 \small
                    AvE_{i}(\%) = \left( \frac{AvE_{i}(\$)}{UPE_{i}^{Anterior}-C_{i,n}^{Anterior}} \right)
                 ''')

    with st.expander("Definicion 2"):
        st.latex(r'''
                 \small
                AvE_{i}(\$)=(C_{i,n}^{Actual}-C_{i,n}^{Anterior}) - \left( \frac{\% dev_{i}^{Actual}- \% dev_{i}^{Anterior}}{1-\%dev_{i}^{Anterior}} \right) * (UPE_{i}^{Anterior}-C_{i,n}^{Anterior})
                 
                 ''')
        
        st.latex(r'''
                 \small
                AvE_{i}(\%)= \frac{AvE_{i}(\$)}{UPE_{i}^{Anterior}-C_{i,n}^{Anterior}}
                 ''')
    st.header("1.3  Escenario What IF 📈💰📊")

    col1, col2 = st.columns(2)
    with col1:
        fecha_pronostico_1= st.date_input("Fecha Inicial Evaluacion :calendar:",min_value= datetime.date(2023, 1, 1),max_value=datetime.date(2023, 12, 31))
    with col2: 
        fecha_pronostico_2= st.date_input("Fecha Final Evaluacion :calendar:",min_value= datetime.date(2024, 1, 1),max_value=datetime.date(2024, 12, 31))

    st.subheader("Base")

    col1_b,col2_b= st.columns(2)

    with col1_b:
        V_Incurrido_b = st.slider('Incremento Costos Servicios B', -0.30, 0.3, 0.025)
        st.write("Inc. Porc. Incurrido:", V_Incurrido_b)
    with col2_b:
        probabilidad_pandemia_b = st.number_input('Probabilidad de Pandemia',min_value=0.0,max_value=0.99,step=0.005)
        st.write('Prob (%)', np.round(probabilidad_pandemia_b,3),"%")
    

    st.subheader("Positivo")

    col_p1,col_p2= st.columns(2)
    
    with col_p1:
        V_Incurrido_p = st.slider('Incremento Costos Servicios P', -0.3, 0.3, 0.025)
        st.write("Inc. Porc. Incurrido:", V_Incurrido_p)
    with col_p2:
        probabilidad_pandemia_p = st.number_input('Probabilidad de Pandemia P',min_value=0.0,max_value=0.99,step=0.005)
        st.write('Prob (%)', np.round(probabilidad_pandemia_p,3),"%")
    

    st.subheader("Negativo")

    col_n1,col_n2= st.columns(2)
    
    with col_n1:
        V_Incurrido_n = st.slider('Incremento Costos Servicios N', -0.30, 0.3, 0.025)
        st.write("Inc. Porc. Incurrido:", V_Incurrido_n)
    with col_n2:
        probabilidad_pandemia_n = st.number_input('Probabilidad de Pandemia N',min_value=0.0,max_value=0.99,step=0.005)
        st.write('Prob (%)', np.round(probabilidad_pandemia_n,3),"%")
        
    st.header("1.4 Pesos Escenarios")
    with st.container():
        with st.form("escenarios_form"):
            st.write("Introduce los porcentajes para cada escenario:")
            negativo = st.number_input("Escenario Negativo (%)", min_value=0, max_value=100, step=5)
            base = st.number_input("Escenario Base (%)", min_value=0, max_value=100, step=5)
            positivo = st.number_input("Escenario Positivo (%)", min_value=0, max_value=100, step=5)
            
            # Validar que la suma de los porcentajes sea 100
            if st.form_submit_button("Guardar"):
                total = negativo + base + positivo
                if total != 100:
                    st.error("La suma de los porcentajes debe ser 100. ☹️")
                else:
                    st.success("Porcentajes guardados correctamente. 😁")


    st.header("1.5 Ejecucion de Escenario")
    with st.expander("Escenario actual"):
        def calcular_ibnr(dataframe):
            # Calcular Ultimate para cada período de desarrollo
            dataframe['Ultimate'] = dataframe['Incurrido'] * dataframe['FD Acumulado']
            # Calcular IBNR para cada período de desarrollo
            dataframe['IBNR'] = dataframe['Ultimate'] - dataframe['Incurrido']
            # Calcular la reserva IBNR total
            reserva_ibnr_total = dataframe['IBNR'].sum()
            return dataframe, reserva_ibnr_total

        # Función principal de la aplicación
        # Simular DataFrame
        df_data = {
                'Incurrido': [1000000000 + i * 1000000000 for i in range(10)],
                'FD': [1 + i * 0.05 for i in range(10)],
                'FD Acumulado': list(accumulate([1 + i * 0.05 for i in range(10)], lambda x, y: x * y))
            }
        df = pd.DataFrame(df_data)

            # Calcular IBNR
        df, reserva_ibnr_total = calcular_ibnr(df)

            # Mostrar tabla con resultados
        st.subheader('Tabla de Resultados')
        st.dataframe(df)
        
        factores_desarrollo = {
            'Año': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
            'Factor de Desarrollo': list(accumulate([1 + i * 0.05 for i in range(10)], lambda x, y: x * y))
        }

        # Crear DataFrame
        df = pd.DataFrame(factores_desarrollo)

        # Crear gráfico de líneas
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['Año'], y=df['Factor de Desarrollo'], mode='lines+markers', name='Factor de Desarrollo'))

        # Configurar diseño del gráfico
        fig.update_layout(title='Factores de Desarrollo a lo largo del tiempo',
                        xaxis_title='Año',
                        yaxis_title='Factor de Desarrollo')

    # Mostrar gráfico en Streamlit
        st.plotly_chart(fig)
        # Mostrar reserva IBNR total
        st.subheader('Reserva IBNR Total')
        st.write(reserva_ibnr_total)
        reserva_original=reserva_ibnr_total/1.42
        st.subheader('Backtesting Reserva')
        st.write(reserva_ibnr_total/(reserva_original))
        


        #if st.button("Guarda Escenario What IF"):
        #   for i in range(10):
        #        st.write(i)

    with st.expander("Esceario Estresado"):
        def calcular_ibnr(dataframe):
            
             # Calcular Ultimate para cada período de desarrollo
            dataframe['Ultimate'] = dataframe['Incurrido'] * dataframe['FD Acumulado']
            # Calcular IBNR para cada período de desarrollo
            dataframe['IBNR'] = dataframe['Ultimate'] - dataframe['Incurrido']
            # Calcular la reserva IBNR total
            reserva_ibnr_total = dataframe['IBNR'].sum()
            return dataframe, reserva_ibnr_total

        # Función principal de la aplicación
        st.title('Cálculo de Reserva IBNR')

            # Selección del escenario base
            # Simular DataFrame
        df_data_estresado = {
                'Incurrido': [1000000000 + i * 1000000000 for i in range(10)],
                #'FD': [(1 + i * 0.05)*(1+V_Incurrido_b)*(1+probabilidad_pandemia_b) * (base/100) + (1 + i * 0.05)*(1+V_Incurrido_n)*(1+probabilidad_pandemia_n) * (negativo/100) + (1 + i * 0.05)*(1+V_Incurrido_p)*(1+probabilidad_pandemia_p) * (positivo/100) for i in range(10)],    
                'FD': [1] + [(1 + i * 0.05)*(1+V_Incurrido_b)*(1+probabilidad_pandemia_b) * (base/100) + (1 + i * 0.05)*(1+V_Incurrido_n)*(1+probabilidad_pandemia_n) * (negativo/100) + (1 + i * 0.05)*(1+V_Incurrido_p)*(1+probabilidad_pandemia_p) * (positivo/100) for i in range(1, 10)]
            }
  
        df_data_estresado["FD Acumulado"]= list(accumulate(df_data_estresado["FD"], lambda x, y: x * y))

        df = pd.DataFrame(df_data_estresado)

        # Calcular IBNR
        df, reserva_ibnr_total = calcular_ibnr(df)

        # Mostrar tabla con resultados
        st.subheader('Tabla de Resultados')
        st.dataframe(df)

        # Mostrar reserva IBNR total y backtesting
        st.subheader('Reserva IBNR Total')
        st.write(reserva_ibnr_total)
        st.subheader('Backtesting Reserva')
        st.write(reserva_ibnr_total / (reserva_original))

            # Mostrar gráfico de factores de desarrollo
        factores_desarrollo = {
                'Año': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
                'Factor de Desarrollo': list(accumulate(df_data_estresado["FD"], lambda x, y: x * y))
        }

        # Crear DataFrame
        df_fd = pd.DataFrame(factores_desarrollo)

        # Crear gráfico de líneas
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df_fd['Año'], y=df_fd['Factor de Desarrollo'], mode='lines+markers', name='Factor de Desarrollo'))
        # Configurar diseño del gráfico
        fig.update_layout(title='Factores de Desarrollo a lo largo del tiempo',
                            xaxis_title='Año',
                            yaxis_title='Factor de Desarrollo')

        # Mostrar gráfico en Streamlit
        st.plotly_chart(fig)        


        
if __name__ == '__main__':
    main()
    
