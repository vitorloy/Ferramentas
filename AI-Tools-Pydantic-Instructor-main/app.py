from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv
import os
from helpers import structured_generator
import locale

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

class Titles(BaseModel):
    titles: List[str]

input = "Ferramentas de escrita com IA"
prompt = f"""
Crie 10 títulos de blog engajantes sobre {input}. Escreva em português do Brasil.

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

Exemplos de Palavras de Poder:

Convencional, Comparar, Importante, Encantado, Maravilhoso, Imaginação, Audaz, Desafio, Endossado, Prodigamente, Insuperável, Útil, Simples, Confiável, Avanço, Oportuno, Autêntico, Alerta, Famoso, Exclusivo, Genuíno, Insider, Amor, Perspectiva, Conclusão, A verdade sobre, Barganha, Segurança, Download, Grande presente, Altíssima, Foco, Facilmente, De repente, Promissor, Desejado, Útil, Revolucionário, Novo, Oportunidades, Fortuna, Monumental, Milagre, Escasso, Acessível, Disparar, Bonança, Lançamento, Força de vontade, Atraente, Tecnologia, Revisitado, Alta tecnologia, Reduzido, Segredos, Poderoso, Superior, Estranho, Melhorar, Imediatamente, Melhorou, Considerável, Pressa, Popular, Simplificado, Inovativa, Abarrotado, Oferta, Liberal, Última chance, Amostrador, Portfólio, De valor, Completo, Maravilhoso, Reembolsável, Surpreendente, Fogo certo, Colorida, Incomum, O melhor, Livre, Sobrevivência, Final, Fundamentos, Energia, Prático, Surgindo, Fora do comum, Incondicional, Direto, Grande, Desconto, Luxo, Notável, Aprovado, Chance, Astuto, Conselho, Qualidade, Anunciando, Rentável, Destino, Completo, Comprovado, Testado, Rápido, Desbloquear, Ilimitado, Último minuto, Urgente, Crescimento, Entregue, Compromisso, Pioneirismo, Enorme, Excitante, Absolutamente o mais baixo, Mais recente, Especialista, Como, Ótimo, Está aqui, Forte, Recompensa, Excelente, Obsessão, Mamute, Habilidade, Inigualável, Instrutivo, Fácil, Acabei de chegar, Explorar, Revelador, Apresentando, Valor, Interessante, Oferta especial, Exclusivo, Fascinante, Emergente, Cantor, Rapidamente, Resistente, Sensacional, Tremendo, Profissional, Especial, Informativo, Bem-sucedido, Gigantesco, Agora, Garantido, Borda, Magia, Observado, Maior, Vida, Competitivo, Limitado, Colossal, Incrível, Esquisito, Surpresa, Holofote, Simplista, Abaixo do preço, Confidencial, Cru, Lindo, Selecionado, Surpreendente.

Exemplos de Palavras de Emoção:

Você precisa, Assustador, Estúpido, Retido, Vire as mesas, Shellacking, Tanque, Sozinho, Vingança, Tentador, Lucro, Destemido, Apavorante, Triunfo, Devastador, Linha, Escondido, Oferecer, Não autorizado, Vibrante, Arranca, Frenesi, Tóxico, Pague Zero, Fé, Você vê, Desinformação, Quebrar, Vítima, Vulnerável, Colapso, Libra, Barato, Rico, Do, Queimando, Viral, Ilegal, Atolado, Mergulho, Fora dos limites, Impressionante, Mentindo, Explodir, Horrível, Punir, Sem perguntas feitas, Insanamente, Esmurrar, Frenético, Vaporizar, Isto é o, Fraude, Praga, Afundando, Isso fará, Absurdo, Reembolso, Invasão, Teve o suficiente, Energizar, Lamber, Doloroso, Sob, Vitória, Coluna, Luxúria, Devassa, Triplo, Esnobe, Prumo, Detestável, Dobro, Surpreendente, Gritar, Dissimulado, Armadilha, Pecaminoso, De cair o queixo, Enganado, Superar, Ambição, Surto, Frugal, Refugiado, Presunçoso, Privacidade, Cadeia, Seguro, O que isso, Visadas, Mais baixo, Sem sentido, Inspirador, Revoltante, Odiar, Inacreditavelmente, Repugnante, Esquecido, Mitos, É o que acontece quando, Ajuda São Os, Coisa que eu já vi, Delírio, Ganância por dinheiro, Seis dígitos, Enganar, Privado, Ter esperança, Alto, Desfazer, Celebração, Aviso, Emocionante, Isso vai fazer você, Em um, Luxuoso, Esplêndido, Devolução de dinheiro, Espírito, Bobagem, Pálido, Pela primeira vez, Preocupar, Retorno, Provocante, Perigo, Preso, Desavergonhado, Claro, Fogo, Ser, Enorme, No, Queda brusca, Armadilha, Recuperar, Destruir, Piranha, Incomumente, Grande prêmio, Desprezível, Falhar, Pânico, Mal, Resultados, Afogamento, Devotado, Para o, Lã, Verdade, Isso é o que, Sabe tudo, Parece uma, Abate, A classificação de, Isto se parece com um, Protegido, Pesquisar, Dinheiro, Proibido, Choramingando, Jogado, O que acontece, À espreita, Assassinato, Presente, Nojento, Foguete, Alimentado à força, Insidioso, Tesouro, De mau gosto, O melhor, Mentiras, Perigo, Excitado, Encouraçado, No, Fazer você, Furacão, O que aconteceu, Embaraçar, Isso é, Burro, Proscrito, O que acontece quando, Dólar, Terror, Crédulo, Cortar, Notavelmente, Como fazer, Surpreendentemente, Surpreendente, Fraco, Sem escrúpulos, É o, Expor, Épico, Brinde, Entusiasmado, Malvado, Ferido, Jubilante, Sujo, Quando você vê, Perdido, Irresistível, Ação judicial, Feliz, Desastroso, Tecnologia, Estrangular, Contrabandeado, Você precisa saber, Garra, Acerto de contas, Pobre, Nada de bom, Experimente antes de comprar, Desamparado, Prêmio, Preço, Espetacular, Reparo provisório, Empoderamento, Oficial, Tentador, Volátil, Render, Oscilando, Lunático, Assassino, Você vê o quê, Arriscado, Rubor, Erros, Fresco na mente, Enorme, Olhos abertos, Isto é o que acontece, Inesperado, A razão pela qual é, Planando, Completo, No mundo, Vai fazer você, Farsa, Falta, Pode parecer um, Aquilo vai, Variar, Vindicação, Chicote, Extra, Hipnótico, Prisão, Doente e cansado, Nunca mais, Jogatina, Valentia, Incomumente, Esmagar, Iminente, Quadruplicar, Grato, Como um normal, Cansado, Aproveitar, Perigoso, A maioria, Impiedoso, Marcado para baixo, Famoso, Tabu, Consecutivamente, Quando você, Pesadelo, Minuto, Fantástico, Maravilhoso.

Exemplos de Palavras Incomuns:

Isso é, Facebook, Mundo, Anos, Novo, Coisa, Pensar, Social, Ano, Precisar, Razões, Melhor, Bom, Você vai, Ver, Ocorrido, Fotos, Visto, Lindo, Agora, Um, Fora, Ser, Primeiro, Garota, Querer, Encontrado, Mais, Dia dos namorados, Aqui, Vida, Algo, Amor, Cara, Meios de comunicação, Coração, Realmente, Fazer, Vídeo, Faz, Garoto, Pessoas, Tempo, Cachorro, Pequeno, Assistir, Olhar, Saber, Mente, Abaixo, Caminhos, Nunca, Certo, Melhorar, Feito, Incrível, Bebê, Velho, Homem, Caminho, Na verdade.
"""

openai_model = "gpt-3.5-turbo"
openai_api_key = os.environ['OPENAI_API_KEY']

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')  # Configura a linguagem para português do Brasil

result = structured_generator(openai_model, prompt, Titles)
print(result.titles)
