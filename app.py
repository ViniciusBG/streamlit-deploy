"""
https://www.youtube.com/watch?v=mrExsjcvF4o
url_for: https://www.youtube.com/watch?v=7X1X39vccW4
https://pythonhow.com/add-css-to-flask-website/
"""

import numpy as np
import streamlit as st
import pickle

model = pickle.load(open('regressor.pkl', 'rb'))

zona_to_onehot = {'norte': np.array([1, 0, 0]),
                  'oeste': np.array([0, 1, 0]),
                  'sul'  : np.array([0, 0, 1]),
                  'leste': np.array([0, 0, 0])}
def main():
    st.title('Calculadora de Imoveis SP')
    zona=st.text_input('Zona')
    quartos=st.text_input('Número de quartos')
    area = st.text_input('Área total')
    zona_prep = zona_to_onehot[zona.lower()]
    quartos_prep = np.log1p(int(quartos))
    area_prep = np.log1p(int(area))
    features = [np.r_[zona_prep, quartos_prep, area_prep]]
    if st.button('Predict'):
        prediction = np.expm1(model.predict(features))
        output = round(prediction[0], 2)
        st.success(f'O valor do aluguel é R${output}')
    else:
        pass

if __name__=='__main__':
    main()
