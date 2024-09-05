# Simulación del Juego de la Perinola

Esta es una aplicación interactiva de Streamlit que simula el juego de la perinola. Permite ajustar varios parámetros de la simulación como el número de jugadores, el número de juegos, el dinero inicial y más. También proporciona gráficos y análisis de los resultados de las simulaciones.

## Requisitos

Asegúrate de tener Python 3.7 o superior instalado en tu sistema. También necesitarás instalar algunas bibliotecas de Python.

## Instalación

Sigue los pasos a continuación para instalar las bibliotecas necesarias y ejecutar la aplicación:

1. **Clona el repositorio o descarga los archivos necesarios**:

    ```bash
    git clone https://github.com/tu_usuario/tu_repositorio.git
    cd tu_repositorio
    ```

2. **Crea un entorno virtual (opcional pero recomendado)**:

    Crear un entorno virtual te ayudará a gestionar las dependencias de la aplicación sin afectar otras configuraciones de Python en tu sistema.

    ```bash
    python -m venv env
    ```

3. **Activa el entorno virtual**:

    - **En Windows**:
    
        ```bash
        .\env\Scripts\activate
        ```

    - **En macOS y Linux**:
    
        ```bash
        source env/bin/activate
        ```

4. **Instala las dependencias**:

    Una vez que el entorno virtual esté activado, instala las bibliotecas necesarias:

    ```bash
    pip install -r requirements.txt
    ```

    **Nota**: Si no tienes un archivo `requirements.txt`, puedes instalar las bibliotecas necesarias manualmente:

    ```bash
    pip install streamlit matplotlib numpy
    ```

## Ejecución de la Aplicación

Una vez que las dependencias estén instaladas, puedes ejecutar la aplicación de Streamlit:

1. **Ejecuta la aplicación**:

    ```bash
    streamlit run perinola_simulacion.py
    ```

2. **Interacción con la aplicación**:

    Al ejecutar el comando anterior, se abrirá una nueva pestaña en tu navegador predeterminado con la aplicación de Streamlit. Aquí podrás ajustar los parámetros de la simulación y visualizar los resultados.

## Uso de la Aplicación

- **Número de jugadores**: Ajusta el número de jugadores en la simulación.
- **Número máximo de juegos por simulación**: Establece el número máximo de juegos que se ejecutarán en cada simulación.
- **Dinero inicial por jugador**: Define cuánto dinero tiene cada jugador al inicio de la simulación.
- **Número de simulaciones**: Configura cuántas veces se ejecutará la simulación con los parámetros definidos.
- **Ejecutar simulación**: Haz clic en este botón para ejecutar la simulación con los parámetros seleccionados.
- **Analizar el efecto del número de jugadores**: Permite ver cómo cambia la simulación al variar el número de jugadores.

## Notas

- Asegúrate de que las bibliotecas `streamlit`, `matplotlib`, y `numpy` estén instaladas correctamente antes de ejecutar la aplicación.
- Si experimentas problemas con la ejecución, verifica que estás utilizando la versión correcta de Python y que todas las dependencias estén instaladas.
- Puedes desactivar el entorno virtual después de ejecutar la aplicación usando el comando `deactivate`.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, crea un fork del repositorio, realiza tus cambios y envía un pull request.

## Licencia

Este proyecto está licenciado bajo la [MIT License](LICENSE).

