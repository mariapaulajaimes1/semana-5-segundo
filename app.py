import streamlit as st
import os
import time
import glob
import os
from gtts import gTTS
from PIL import Image
import base64

st.title("El renacuajo paseador")
image = Image.open('rinrin.jpg')
st.image(image, width=350)
with st.sidebar:
    st.subheader("Esrcibe y/o selecciona texto para ser escuchado.")


try:
    os.mkdir("temp")
except:
    pass

st.subheader("EL RENACUAJO PASEADOR.")
st.write(
El hijo de rana, Rinrín renacuajo, salió esta mañana muy tieso y muy majo, con pantalón corto, corbata a la moda, sombrero encintado y chupa de boda. "¡Muchacho, no salgas!" le grita mamá, pero él hace un gesto y orondo se va. Halló en el camino a un ratón vecino, y le dijo: "¡Amigo! venga usted conmigo, visitemos juntos a doña Ratona y habrá francachela y habrá comilona." A poco llegaron y avanza ratón, estírase el cuello, coge el aldabón, da dos o tres golpes, preguntan: "¿Quién es?" "Yo, doña Ratona, beso a usted los pies. ¿Está usted en casa?" "Sí señor, sí estoy, y celebro mucho ver a ustedes hoy; estaba en mi oficio, hilando algodón, pero eso no importa; bienvenidos son." Se hicieron la venia, se dieron la mano, y dice Ratico, que es más veterano: "Mi amigo el de verde rabia de calor, démelo cerveza, hágame el favor." Y en tanto que el pillo consume la jarra, mandó la señora traer la guitarra, y a renacuajo le pide que cante versitos alegres, tonada elegante. "¡Ay! de mil amores lo hiciera, señora, pero es imposible darle gusto ahora, que tengo el gaznate más seco que estopa y me aprieta mucho esta nueva ropa." "Lo siento infinito," responde tía Rata, "aflójese un poco chaleco y corbata, y yo mientras tanto les voy a cantar una cancioncita muy particular." Mas estando en esta brillante función de baile y cerveza, guitarra y canción, la gata y sus gatos salvan el umbral, y vuélvese aquello el juicio final. Doña Gata vieja trinchó por la oreja al niño Ratico maullándole: "¡Hola!" Y los niños gatos a la vieja rata, uno por la pata y otro por la cola. Don Renacuajito, mirando este asalto, tomó su sombrero, dio un tremendo salto, y abriendo la puerta con mano y narices, se fue dando a todos noches muy felices. Y siguió saltando tan alto y aprisa, que perdió el sombrero, rasgó la camisa, se coló en la boca de un pato tragón y éste se lo embucha de un solo estirón. Y así concluyeron, uno, dos y tres: ratón y ratona, y el rana después; los gatos comieron y el pato cenó, ¡y mamá ranita solita quedó!
        
        )
           
st.markdown(f"Quieres escucharlo?, copia el texto")
text = st.text_area("Ingrese El texto a escuchar.")

tld='com'
option_lang = st.selectbox(
    "Selecciona el lenguaje",
    ("Español", "English"))
if option_lang=="Español" :
    lg='es'
if option_lang=="English" :
    lg='en'

def text_to_speech(text, tld,lg):
    
    tts = gTTS(text,lang=lg) # tts = gTTS(text,'en', tld, slow=False)
    try:
        my_file_name = text[0:20]
    except:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")
    return my_file_name, text


#display_output_text = st.checkbox("Verifica el texto")

if st.button("convertir a Audio"):
     result, output_text = text_to_speech(text, 'com',lg)#'tld
     audio_file = open(f"temp/{result}.mp3", "rb")
     audio_bytes = audio_file.read()
     st.markdown(f"## Tú audio:")
     st.audio(audio_bytes, format="audio/mp3", start_time=0)

     #if display_output_text:
     
     #st.write(f" {output_text}")
    
#if st.button("ElevenLAabs",key=2):
#     from elevenlabs import play
#     from elevenlabs.client import ElevenLabs
#     client = ElevenLabs(api_key="a71bb432d643bbf80986c0cf0970d91a", # Defaults to ELEVEN_API_KEY)
#     audio = client.generate(text=f" {output_text}",voice="Rachel",model="eleven_multilingual_v1")
#     audio_file = open(f"temp/{audio}.mp3", "rb")

     with open(f"temp/{result}.mp3", "rb") as f:
         data = f.read()

     def get_binary_file_downloader_html(bin_file, file_label='File'):
        bin_str = base64.b64encode(data).decode()
        href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
        return href
     st.markdown(get_binary_file_downloader_html("audio.mp3", file_label="Audio File"), unsafe_allow_html=True)

def remove_files(n):
    mp3_files = glob.glob("temp/*mp3")
    if len(mp3_files) != 0:
        now = time.time()
        n_days = n * 86400
        for f in mp3_files:
            if os.stat(f).st_mtime < now - n_days:
                os.remove(f)
                print("Deleted ", f)


remove_files(7)
