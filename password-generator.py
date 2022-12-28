import string as st
import numpy as np

letras = st.ascii_letters
numeros = st.digits
especial = st.punctuation
alg = (letras + numeros + especial)
senha = np.random.choice(list(alg), 10)
print(''.join(senha))
