import streamlit as st
from PIL import Image

def main():
    st.title('Videos')
    # st.header('Imagen de escritorio:')
    # img = Image.open('Lluvia.webp')
    # st.image(img, use_column_width=True)

    st.header('Imagen de internet:')
    st.image('https://i.pinimg.com/originals/2b/ea/b0/2beab067ba0e6076643c8f70fb8d884b.jpg')

    st.header('Video:')
    with open('Lluvia.mp4', 'rb') as video_file:
        st.video(video_file.read(), start_time=0)

    # with open('Cancion.mp3', 'rb') as audio_file:
        # st.audio(audio_file.read())'''
    



if __name__ == '__main__':
    main()  