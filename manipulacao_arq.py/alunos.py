import streamlit as st 

def cadastrar_alunos(nome, matricula, curso):
    with open("usuarios.txt", "a") as arquivo:
        arquivo.write(
            f"Nome: {nome:<30} | Matrícula: {matricula:<20} | Curso: {curso:<30}\n"
        )

st.title("Cadastrar alunos 💕")

nome = st.text_input("Digite seu nome:")
matricula = st.text_input("Digite sua matrícula:")
curso = st.text_input("Digite o seu curso:")

if st.button("Salvar"):
    if nome and matricula and curso:
        cadastrar_alunos(nome, matricula, curso)
        st.success("Aluno cadastrado com sucesso! 🎉")
    else:
        st.warning("Preencha todos os campos!")
