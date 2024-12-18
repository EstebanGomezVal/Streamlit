import streamlit as st

def main():
    st.title('Curso Streamlit')
    st.header('Esto es un encabezado')
    st.subheader('Esto es un sub encabezado')
    st.text('Esto es un texto')
    nombre = 'Esteban'
    st.text(f'Hola {nombre} esto es un texto')
    st.markdown('# Esto es un markdown')
    st.markdown('## Esto es un markdown')
    st.markdown('### Esto es un markdown')


if __name__ == '__main__':
    main()