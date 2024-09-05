import streamlit as st
import random
import matplotlib.pyplot as plt
import numpy as np

# Función para simular el juego de la perinola
def jugar_perinola(jugadores, juegos, dinero_inicial):
    resultados = {i: {'billetera': dinero_inicial, 'historia': [dinero_inicial]} for i in range(jugadores)}
    pozo_comun = 0
    jugador_ganador = None
    
    for juego in range(juegos):
        for jugador in resultados:
            if resultados[jugador]['billetera'] <= 0:
                continue
            
            resultado = random.choice(['Pon 1', 'Pon 2', 'Toma 1', 'Toma 2', 'Toma todo', 'Todos ponen'])
            if resultado == 'Pon 1':
                if resultados[jugador]['billetera'] >= 1:
                    resultados[jugador]['billetera'] -= 1
                    pozo_comun += 1
            elif resultado == 'Pon 2':
                if resultados[jugador]['billetera'] >= 2:
                    resultados[jugador]['billetera'] -= 2
                    pozo_comun += 2
            elif resultado == 'Toma 1':
                if pozo_comun >= 1:
                    resultados[jugador]['billetera'] += 1
                    pozo_comun -= 1
            elif resultado == 'Toma 2':
                if pozo_comun >= 2:
                    resultados[jugador]['billetera'] += 2
                    pozo_comun -= 2
            elif resultado == 'Toma todo':
                resultados[jugador]['billetera'] += pozo_comun
                pozo_comun = 0
            elif resultado == 'Todos ponen':
                for j in resultados:
                    if resultados[j]['billetera'] > 0:
                        resultados[j]['billetera'] -= 1
                        pozo_comun += 1

            resultados[jugador]['historia'].append(resultados[jugador]['billetera'])
        
        jugadores_con_dinero = [j for j, datos in resultados.items() if datos['billetera'] > 0]
        if len(jugadores_con_dinero) == 1:
            jugador_ganador = jugadores_con_dinero[0]
            break

    return resultados, pozo_comun, juego + 1, jugador_ganador

def graficar_resultados(resultados):
    fig, ax = plt.subplots()
    
    for jugador, datos in resultados.items():
        ax.plot(datos['historia'], label=f'Jugador {jugador}')
    
    ax.set_xlabel('Número de juegos')
    ax.set_ylabel('Dinero en billetera')
    ax.set_title('Ganancias y pérdidas por jugador durante la simulación')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

# Interfaz de Streamlit
st.title("Simulación del Juego de la Perinola")

# Entradas de usuario para configurar la simulación
jugadores = st.slider("Número de jugadores", 2, 10, 4)
juegos = st.slider("Número máximo de juegos por simulación", 100, 5000, 1000)
dinero_inicial = st.number_input("Dinero inicial por jugador", min_value=10, max_value=1000, value=100)
simulaciones = st.number_input("Número de simulaciones", min_value=1, max_value=500, value=100)

# Botón para iniciar la simulación
if st.button("Ejecutar simulación"):
    st.write(f"Simulando con {jugadores} jugadores, {juegos} juegos por simulación, {dinero_inicial} de dinero inicial y {simulaciones} simulaciones.")
    
    # Ejecutar simulación
    resultados, pozo_final, juegos_totales, ganador = jugar_perinola(jugadores, juegos, dinero_inicial)
    
    # Mostrar resultados
    st.write(f"Número de juegos hasta que un jugador se quede sin dinero: {juegos_totales}")
    
    if ganador is not None:
        st.write(f"El ganador es el Jugador {ganador}")
    else:
        st.write("No hubo ganador en esta simulación.")
    
    # Graficar resultados
    graficar_resultados(resultados)

# Función para analizar resultados
def analizar_resultados(resultados, juegos_totales):
    juegos_para_sin_dinero = juegos_totales
    for jugador, datos in resultados.items():
        if datos['billetera'] <= 0:
            juegos_para_sin_dinero = min(juegos_para_sin_dinero, len(datos['historia']))
    return juegos_para_sin_dinero

# Función para calcular el promedio de juegos para que haya un ganador
def juegos_promedio_para_ganador(jugadores, dinero_inicial, simulaciones):
    juegos_totales = []
    for _ in range(simulaciones):
        resultados, pozo_final, juegos, ganador = jugar_perinola(jugadores, 1000, dinero_inicial)
        if ganador is not None:
            juegos_totales.append(juegos)
    if len(juegos_totales) == 0:
        st.write("No hubo juegos en los que un jugador ganó todo el dinero.")
        promedio = 0
    else:
        promedio = np.mean(juegos_totales)
        st.write(f"Promedio de juegos para que haya un ganador: {promedio:.2f}")
    return promedio

# Efecto del número de jugadores en los juegos necesarios para ganar
def efecto_numero_jugadores(jugadores_list, dinero_inicial, simulaciones):
    juegos_por_jugadores = {}
    for jugadores in jugadores_list:
        promedio_juegos = juegos_promedio_para_ganador(jugadores, dinero_inicial, simulaciones)
        juegos_por_jugadores[jugadores] = promedio_juegos
    fig, ax = plt.subplots()
    ax.plot(list(juegos_por_jugadores.keys()), list(juegos_por_jugadores.values()), marker='o')
    ax.set_xlabel('Número de jugadores')
    ax.set_ylabel('Promedio de juegos para ganar')
    ax.set_title('Efecto del número de jugadores en los juegos necesarios para ganar todo el dinero')
    ax.grid(True)
    st.pyplot(fig)

# Mostrar análisis adicional
if st.button("Analizar el efecto del número de jugadores"):
    jugadores_list = [2, 4, 6, 8, 10]
    efecto_numero_jugadores(jugadores_list, dinero_inicial, simulaciones)
