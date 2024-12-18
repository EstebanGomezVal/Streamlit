import streamlit as st

def main():
    st.title('Curso Streamlit')
    st.header('Esto es un encabezado')
    st.subheader('Esto es un sub encabezado')
    st.text('Esto es un texto')
    nombre = 'Esteban'
    st.text(f'Hola {nombre} esto es un texto')
    st.markdown('## Esto es un markdown')
    
    st.success('Exito')
    st.warning('Advertencia')
    st.info('informacion')
    st.error('Error')

    st.write('Esta es la suma de uno mas dos')
    st.write(1+2)





if __name__ == '__main__':
    main()