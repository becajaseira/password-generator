import string as st
import numpy as np

ncarac = int(input('Quantos caracteres quer sua senha? '))
letras = st.ascii_letters
numeros = st.digits
especial = st.punctuation
alg = (letras + numeros + especial)
senha = np.random.choice(list(alg), ncarac)
print(''.join(senha))
