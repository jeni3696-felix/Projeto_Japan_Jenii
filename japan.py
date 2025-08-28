# import streamlit as st
# import pandas as pd


# cidade = ['Nagoya', 'Xinxi', 'Tokio']

# opcao = st.sidebar.selectbox('Escolha uma cidade do Japão',cidade)
# # Dados de exemplo (substitua pelas suas coordenadas do Japão)
# data = {'latitude': [35.6895, 34.6937, 39.701],
#         'longitude': [139.6917, 135.5023, 141.673]}
# df = pd.DataFrame(data)

# st.title("Mapa do Japão")
# st.map(df)

### isso é pra quem vei segunda

import streamlit as st
import pandas as pd

cidade = ['Nagoya', 'Xinxi', 'Tokyo']

## BARRA LATERAL !!!!!!
opcao = st.sidebar.selectbox('Escolha uma cidade do Japão', cidade)

### COORDENADAS DO JAPÃO
data = {'latitude': [35.6895, 34.6937, 39.701],
        'longitude': [139.6917, 135.5023, 141.673]}

df = pd.DataFrame(data) 

### TITULO DO SITE
st.title("Mapa do Japão")
### CRIANDO UM MAPA
st.map(df)