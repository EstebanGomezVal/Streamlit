import streamlit as st

def main():
    st.title('Input')
    nombre = st.text_input('ingresa tu nombre')
    st.title(nombre)

    mensaje = st.text_area('ingresa tu mensaje', height=100)
    st.write(mensaje)

    numero = st.number_input('Ingresa un numero', 1.0, 25.0, 1.0)
    st.write(numero)

    cita = st.date_input('Ingresa una fecha')
    st.write(cita)

    hora = st.time_input('Ingresa una hora')
    st.write(hora)

    color = st.color_picker('Selecciona un color')
    st.write(color)


if __name__ == '__main__':
    main()
    