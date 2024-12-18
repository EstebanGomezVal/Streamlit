import streamlit as st
import pandas as pd

df = pd.read_csv(r'C:\Users\esteb\OneDrive\Documents\GitHub\Streamlit\Pyhton\titanic.csv')
df2 = df[['Age', 'Pclass', 'Parch', 'SibSp']].sample(n=100, random_state=42)

def main():
    st.title('DataFrames')
    st.header('Data:')
    st.dataframe(df) #st.table(df) (Tabla completa)
    #st.write(df.head())
    st.header('DataFrame con subrayado')
    st.dataframe(df2.style.highlight_max(axis=0))
    st.header('Json')
    st.json({'clave':'valor'})

    codigo = '''
    def saludar():
        print('Hola)
    '''

    st.code(codigo, language='python')

if __name__=='__main__':
    main()