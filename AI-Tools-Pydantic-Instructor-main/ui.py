import streamlit as st
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv
import os
from helpers import structured_generator
import locale

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Define a classe para os títulos
class Titles(BaseModel):
    titles: List[str]

def main():
    # Configura a linguagem para português do Brasil
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

    # Título do aplicativo Streamlit
    st.title('Gerador de Títulos de Blog com IA')

    # Entrada do usuário para o tópico do blog
    input_topic = st.text_input('Digite o tópico do blog:', 'Ferramentas de escrita com IA')

    # Variáveis para o OpenAI
    openai_model = "gpt-3.5-turbo"
    openai_api_key = os.environ.get('OPENAI_API_KEY')

    if st.button('Gerar Títulos'):
        if openai_api_key:
            # Define o prompt com o tópico fornecido pelo usuário
            prompt = f"""
            Crie 10 títulos de blog engajantes sobre {input_topic}. Escreva em português do Brasil.

            1. Pontuação geral: Uma boa pontuação é entre 40 e 60. Esforce-se para obter um score de 70.
            2. Equilíbrio das palavras: Seu título será mais atraente e atrairá mais cliques se você adicionar mais palavras emocionais, incomuns e poderosas.
            3. Contador de caracteres: Títulos com 55 caracteres serão exibidos completamente nos resultados de pesquisa e tendem a obter mais cliques.
            4. Contagem de palavras: Os títulos têm mais probabilidade de serem clicados nos resultados de pesquisa se tiverem 6 palavras.
            5. Sentimento: Títulos positivos tendem a ter melhor engajamento do que os neutros e negativos.
            6. Tipo de Título: Títulos com “listas” e “como” costumam ter mais engajamento que outros.
            7. O título deve ser “somente” sobre dicas ou curiosidade para o tópico ou palavra-chave quando inserido.
            8. O título deve obrigatoriamente ter “até no máximo 55 caracteres.”
            9. O título deve conter 20 a 30% de palavras comuns.
            10. O título deve conter 10 a 20% de palavras incomuns.
            11. O título deve conter 10 a 15% de palavras emocionais.
            12. O título deve conter pelo menos uma palavra de poder.
            13. Crie 10 títulos.
            """

            # Chama a função para gerar os títulos
            try:
                result = structured_generator(openai_model, prompt, Titles)
                st.write('Títulos Gerados:')
                for title in result.titles:
                    st.write(f'- {title}')
            except Exception as e:
                st.error(f'Erro ao gerar títulos: {e}')
        else:
            st.error('Chave de API do OpenAI não encontrada. Verifique o arquivo .env.')

if __name__ == "__main__":
    main()

