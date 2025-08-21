import streamlit as st


# -------------------------------------------------- Sidebar

st.sidebar.image("logo2.png")
st.sidebar.title("Car Rental")

st.sidebar.title("Aluguel de Carros ")

carros = ["Mustang","Fusca","Ferrari","Tesla Model","Porsche"]

opcao = st.sidebar.selectbox("Escolha o carro que foi alugado",carros)









# ---------------------------------------------------- Principal

st.title("Car Rental - Aluguel de Carros ")

st.markdown(f"#### Você alugou o modelo: {opcao}")

st.image(f"{opcao}.png")

st.markdown("---")

dias = st.text_input(f"Por quantos dias o {opcao} foi alugado?")
km = st.text_input(f"Quantos km você rodou com o {opcao}?")

if opcao == "Mustang":
    diaria = 670

elif opcao == "Fusca":
    diaria = 1000

elif opcao == "Ferrari":
    diaria = 890

elif opcao == "Tesla Model":
    diaria = 876

elif opcao == "Porsche":
    diaria = 765


if st.button("Calcular"):
    dias = int(dias)
    km = float(km)

    total_dias = dias*diaria
    total_km = km*0.15
    aluguel_total = total_dias + total_km

    st.warning(f"Você alugou o {opcao} por {dias} dias e rodou {km} km. O volor total a pagar é R${aluguel_total}")