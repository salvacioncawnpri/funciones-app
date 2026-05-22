import streamlit as st

import numpy as np

import matplotlib.pyplot as plt

st.markdown("""
<style>

.stApp {
    background-color: #0E1117;
    color: white;
}

section[data-testid="stSidebar"] {
    background-color: #161A23;
}

h1, h2, h3, h4, h5, h6, p, label {
    color: white;
}

</style>
""", unsafe_allow_html=True)
st.set_page_config(page_title="Funciones Matemáticas", layout="centered")

st.title("🧠 Laboratorio Interactivo de Funciones Matemáticas")
st.markdown("""
Este laboratorio interactivo permite analizar funciones matemáticas
mediante algoritmos programados en Python.

El usuario puede modificar coeficientes en tiempo real y observar
cómo cambian las propiedades algebraicas y gráficas de cada función.
""")
st.write("Proyecto de matemáticas sobre funciones y aplicaciones reales.")
st.sidebar.title("📚 Menú de Funciones")

st.sidebar.markdown("""
### Proyecto de algoritmos matemáticos

Aplicación interactiva desarrollada en Python y Streamlit.
""")
st.sidebar.markdown("---")
st.sidebar.markdown("### 👨‍💻 Desarrollador")
st.sidebar.write("Cristian Amir Gómez Jiménez")
st.sidebar.write("Proyecto escolar de Matemáticas")
opcion = st.selectbox(
    "Selecciona un tipo de función:",
    [
        "Polinomial",
        "Racional",
        "Exponencial",
        "Logarítmica",
        "Trigonométrica"
    ]

)

x = np.linspace(-10,10,400)

if opcion == "Polinomial":
    st.header("📈 Función Polinomial")
    st.write("""
    Las funciones polinomiales están formadas por potencias de x con exponentes enteros positivos.
    Estas funciones son utilizadas en física, ingeniería y modelado matemático.
    """)

    a = st.slider("Valor de a", -10.0, 10.0, 1.0)
    b = st.slider("Valor de b", -10.0, 10.0, -4.0)
    c = st.slider("Valor de c", -10.0, 10.0, 3.0)

    y = a*x**2 + b*x + c

    st.latex(f"f(x)={a}x^2+({b})x+({c})")

    st.subheader("Dominio")
    st.write("Todos los números reales.")

    st.subheader("Comportamiento")
    vertice_x = -b / (2*a)
    vertice_y = a*(vertice_x**2) + b*vertice_x + c

    st.write(f"Vértice aproximado: ({vertice_x:.2f}, {vertice_y:.2f})")
    discriminante = b**2 - 4*a*c

    st.write(f"Discriminante: {discriminante:.2f}")

    if discriminante > 0:
        raiz1 = (-b + np.sqrt(discriminante)) / (2*a)
        raiz2 = (-b - np.sqrt(discriminante)) / (2*a)

        st.write(f"Raíz 1: {raiz1:.2f}")
        st.write(f"Raíz 2: {raiz2:.2f}")
        st.write("La función tiene dos raíces reales.")

    elif discriminante == 0:
        raiz = -b / (2*a)

        st.write(f"Raíz única: {raiz:.2f}")
        st.write("La función tiene una raíz real.")

    else:
        st.write("La función no tiene raíces reales.")

    if a > 0:
        st.write("La parábola abre hacia arriba.")
    else:
        st.write("La parábola abre hacia abajo.")

    st.subheader("Aplicaciones reales")

    st.write("""
    • Movimiento de objetos  
    • Trayectorias de pelotas  
    • Diseño de puentes  
    • Física y arquitectura  
    """)

    fig, ax = plt.subplots()

    ax.plot(x, y, linewidth=3, color="#00D9FF")
    if discriminante >= 0:
            ax.scatter(raiz1, 0, s=100)
            ax.scatter(raiz2, 0, s=100)
            ax.scatter(vertice_x, vertice_y, s=150)
    ax.grid(alpha=0.25)
    ax.axhline(0, color="white", linewidth=1)
    ax.axvline(0, color="white", linewidth=1)

    ax.set_facecolor("#0E1117")
    fig.patch.set_facecolor("#0E1117")

    st.pyplot(fig)


elif opcion == "Racional":

    st.header("📉 Función Racional")

    st.write("""
    Las funciones racionales representan divisiones entre polinomios.
    Estas funciones pueden generar asíntotas y comportamientos extremos.
    """)

    a = st.slider("Valor de a", -10.0, 10.0, 1.0, key="ra")
    b = st.slider("Valor de b", -10.0, 10.0, -1.0, key="rb")
    c = st.slider("Valor de c", -10.0, 10.0, 1.0, key="rc")
    d = st.slider("Valor de d", -10.0, 10.0, 1.0, key="rd")

    x = np.linspace(-10, 10, 1000)

    denominador = c*x + d

    x = x[np.abs(denominador) > 0.1]

    y = (a*x + b)/(c*x + d)

    st.latex(r"f(x)=\frac{ax+b}{cx+d}")

    st.subheader("Función actual")
    st.latex(fr"f(x)=\frac{{{a:.1f}x+({b:.1f})}}{{{c:.1f}x+({d:.1f})}}")

    if c != 0:
        asintota_vertical = -d/c
        asintota_horizontal = a/c

        st.subheader("Asíntotas")

        st.write(f"Asíntota vertical: x = {asintota_vertical:.2f}")
        st.write(f"Asíntota horizontal: y = {asintota_horizontal:.2f}")

    st.subheader("Dominio")

    if c != 0:
        st.write(f"Todos los reales excepto x = {-d/c:.2f}")
    else:
        st.write("Todos los números reales.")

    st.subheader("Aplicaciones reales")

    st.write("""
    • Velocidad promedio  
    • Economía  
    • Circuitos eléctricos  
    • Modelos físicos  
    """)

    fig, ax = plt.subplots()

    ax.plot(x, y, linewidth=3, color="#00D9FF")

    ax.grid(alpha=0.25)
    ax.axhline(0, color="white", linewidth=1)
    ax.axvline(0, color="white", linewidth=1)

    ax.set_facecolor("#0E1117")
    fig.patch.set_facecolor("#0E1117")

    st.pyplot(fig)

elif opcion == "Exponencial":

    st.header("📈 Función Exponencial")

    st.write("""
    Las funciones exponenciales tienen la variable en el exponente.
    Son utilizadas para modelar crecimiento acelerado y decaimiento.
    """)

    a = st.slider("Valor de a", 0.01, 20.0, 2.0, 0.1, key="ea")
    b = st.slider("Valor de b", -5.0, 5.0, 0.0, key="eb")

    x = np.linspace(-10, 10, 1000)

    y = a**(x+b)

    st.subheader("Función actual")

    st.latex(fr"f(x)={a:.1f}^{{x+({b:.1f})}}")

    st.subheader("Dominio")
    st.write("Todos los números reales.")

    st.subheader("Rango")
    st.write("(0, ∞)")

    st.subheader("Comportamiento")

    if a > 1:
        st.write("La función presenta crecimiento exponencial.")
    elif a < 1:
        st.write("La función presenta decaimiento exponencial.")

    st.subheader("Aplicaciones reales")

    st.write("""
    • Crecimiento poblacional  
    • Bacterias  
    • Interés compuesto  
    • Redes sociales  
    • Radioactividad  
    """)

    fig, ax = plt.subplots()

    ax.plot(x, y, linewidth=3, color="#00D9FF")

    ax.grid(alpha=0.25)
    ax.axhline(0, color="white", linewidth=1)
    ax.axvline(0, color="white", linewidth=1)

    ax.set_facecolor("#0E1117")
    fig.patch.set_facecolor("#0E1117")

    st.pyplot(fig)

elif opcion == "Logarítmica":

    st.header("📊 Función Logarítmica")

    st.write("""
    Las funciones logarítmicas son inversas de las funciones exponenciales.
    Se utilizan para representar fenómenos donde el crecimiento ocurre lentamente.
    """)

    a = st.slider("Valor de a", 0.1, 10.0, 1.0, 0.1, key="la")
    b = st.slider("Desplazamiento horizontal", -10.0, 10.0, 0.0, 0.1, key="lb")

    x = np.linspace(0.1, 20, 1000)

    y = a * np.log(x + abs(b) + 0.1)

    st.subheader("Función actual")

    st.latex(fr"f(x)={a:.1f}\log(x+{abs(b):.1f})")

    st.subheader("Dominio")
    st.write("x > 0")

    st.subheader("Rango")
    st.write("Todos los números reales.")

    st.subheader("Comportamiento")

    st.write("""
    • Crece lentamente  
    • Tiene una asíntota vertical  
    • Es inversa de la exponencial  
    """)

    st.subheader("Aplicaciones reales")

    st.write("""
    • Escala Richter  
    • Decibeles  
    • Crecimiento poblacional lento  
    • Ciencias e ingeniería  
    """)

    fig, ax = plt.subplots()

    ax.plot(x, y, linewidth=3, color="#00D9FF")

    ax.grid(alpha=0.25)
    ax.axhline(0, color="white", linewidth=1)
    ax.axvline(0, color="white", linewidth=1)

    ax.set_facecolor("#0E1117")
    fig.patch.set_facecolor("#0E1117")

    st.pyplot(fig)

elif opcion == "Trigonométrica":

    st.header("🌊 Función Trigonométrica")

    st.write("""
    Las funciones trigonométricas modelan fenómenos periódicos
    como ondas, sonido y movimiento oscilatorio.
    """)

    a = st.slider("Amplitud", 0.1, 10.0, 1.0, 0.1, key="ta")
    b = st.slider("Frecuencia", 0.1, 10.0, 1.0, 0.1, key="tb")
    c = st.slider("Desplazamiento horizontal", -10.0, 10.0, 0.0, 0.1, key="tc")

    x = np.linspace(-20, 20, 2000)
    tipo = st.selectbox(
        "Tipo de función trigonométrica",
        ["Seno", "Coseno", "Tangente"]
    )
    if tipo == "Seno":
        y = a * np.sin(b * (x + c))

    elif tipo == "Coseno":
        y = a * np.cos(b * (x + c))

    elif tipo == "Tangente":
        y = a * np.tan(b * (x + c))

    st.subheader("Función actual")

    if tipo == "Seno":
        st.latex(fr"f(x)={a:.1f}\sin({b:.1f}(x+{c:.1f}))")

    elif tipo == "Coseno":
        st.latex(fr"f(x)={a:.1f}\cos({b:.1f}(x+{c:.1f}))")

    elif tipo == "Tangente":
        st.latex(fr"f(x)={a:.1f}\tan({b:.1f}(x+{c:.1f}))") 

    st.subheader("Dominio")
    st.write("Todos los números reales.")

    st.subheader("Rango")
    st.write(f"[{-a:.1f}, {a:.1f}]")

    periodo = (2*np.pi)/b

    st.subheader("Período")
    st.write(f"Período aproximado: {periodo:.2f}")

    st.subheader("Comportamiento")

    if b > 1:
        st.write("La onda oscila más rápido.")
    elif b < 1:
        st.write("La onda oscila más lento.")

    st.subheader("Aplicaciones reales")

    st.write("""
    • Ondas del mar  
    • Música  
    • Sonido  
    • Electricidad  
    • Física  
    • Vibraciones  
    """)

    fig, ax = plt.subplots()

    ax.plot(x, y, linewidth=3, color="#00D9FF")

    ax.grid(alpha=0.25)
    ax.axhline(0, color="white", linewidth=1)
    ax.axvline(0, color="white", linewidth=1)

    ax.set_facecolor("#0E1117")
    fig.patch.set_facecolor("#0E1117")

    st.pyplot(fig)