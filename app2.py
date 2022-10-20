import streamlit as st
from img_classification import teachable_machine_classification
import keras
from PIL import Image, ImageOps
import numpy as np

st.title("Aplicación de reconocimiento de Wild Animals 🦁 🐆 :wolf:")
uploaded_file = st.file_uploader("Carga una imagen ...", type=["jpg","jpeg"])
if uploaded_file is not None:
  image = Image.open(uploaded_file)
  st.image(image)
  label = teachable_machine_classification(image, 'keras_model.h5') 
  st.write(label)
  if label==0:
   st.header("Es un 🐆")
   st.subheader("Definición")
   st.write("El guepardo (Acinonyx jubatus) es un gran felino originario de África y el centro de Irán. Es el animal terrestre más rápido, se estima que es capaz de correr de 80 a 128 km/h (50 a 80 mph) con las velocidades más rápidas registradas de manera confiable siendo 93 y 98 km/h (58 y 61 mph), y como tal tiene varias adaptaciones para la velocidad, incluida una constitución ligera, patas largas y delgadas y una cola larga. Por lo general, alcanza los 67 a 94 cm (26 a 37 pulgadas) en el hombro, y la longitud de la cabeza y el cuerpo es de entre 1,1 y 1,5 m (3 pies 7 pulgadas y 4 pies 11 pulgadas). Los adultos pesan entre 21 y 72 kg (46 y 159 lb). Su cabeza es pequeña y redondeada, con un hocico corto y rayas faciales negras en forma de lágrimas. El pelaje es típicamente rojizo a blanco cremoso o ante pálido y está cubierto en su mayoría con manchas negras sólidas espaciadas uniformemente. Se reconocen cuatro subespecies.")
   st.balloons()
  if label==1:
   st.header("Es un :wolf:")
   st.subheader("Definición")
   st.write("El lobo (Canis lupus[b]; pl: lobos), también conocido como lobo gris o lobo gris, es un gran canino originario de Eurasia y América del Norte. Se han reconocido más de treinta subespecies de Canis lupus, y los lobos grises, como se entiende popularmente, comprenden subespecies salvajes. El lobo es el miembro más grande que existe de la familia Canidae. También se distingue de otras especies de Canis por sus orejas y hocico menos puntiagudos, así como por un torso más corto y una cola más larga. No obstante, el lobo está lo suficientemente relacionado con especies de Canis más pequeñas, como el coyote y el chacal dorado, para producir híbridos fértiles con ellos. El pelaje con bandas de un lobo suele ser moteado de blanco, marrón, gris y negro, aunque las subespecies en la región ártica pueden ser casi todas blancas.")
   st.balloons()
  if label==2:
    st.header("Es un 🦁")
    st.subheader("Definición")
    st.write ("El león (Panthera leo) es un gran felino del género Panthera originario de África e India. Tiene un cuerpo musculoso, de pecho ancho, cabeza corta y redondeada, orejas redondas y un mechón peludo al final de la cola. Es sexualmente dimórfico; los leones machos adultos son más grandes que las hembras y tienen una melena prominente. Es una especie social, formando grupos llamados manadas. La manada de un león consiste en unos pocos machos adultos, hembras emparentadas y cachorros. Los grupos de leonas suelen cazar juntas y se alimentan principalmente de grandes ungulados. El león es un depredador ápice y clave; aunque algunos leones se alimentan cuando se presentan las oportunidades y se sabe que cazan humanos, la especie generalmente no busca activamente ni se aprovecha de los humanos.")
    st.balloons()

