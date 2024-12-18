import streamlit as st

def main():
    st.title('Listas')
    opcion = st.selectbox(
        'Elige tu fruta', 
        ['Manzana', 'Pera', 'Durazno', 'Fresa']
    )

    st.write(f'Tu fruta favorita es {opcion}')

    opciones = st.multiselect(
        'Elige tus colores favoritos', 
        ['rojo', 'azul', 'verde', 'amarillo', 'morado', 'cafe']
    )

    st.write(f'Tus colores favoritos son:', opciones)

    edad = st.slider(
        'Selecciona tu edad',
        min_value=0, 
        max_value=100, 
        value=25, 
        step=1
    )

    st.write('Tu edad es:', edad)

    nivel = st.select_slider(
        'Selecciona tu nivel de satisfaccion:',
        options = ['Muy alto', 'Alto', 'Regular', 'Bajo', 'Muy bajo'], 
        value='Regular'
    )
    st.write('Tu nivel de satisfaccion es: ', nivel)

if __name__ == "__main__":
    main()