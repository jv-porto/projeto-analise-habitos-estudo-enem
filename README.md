<h1 align="center">Quais fatores mais influenciam no desempenho de um aluno no ENEM e como podemos ajudá-lo a melhorar sua performance?</h1>

Este documento especifica o projeto em desenvolvimento pelo nosso grupo como produto das disciplinas: **Projeto Integrado** e **Banco de Dados**.

Link do dataset usado: [Microdados do ENEM 2022](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem)

## **Descrição do Projeto**

Com o tema focado em: Quais hábitos de estudo são mais relevantes para o desempenho dos estudantes no ENEM?

O seguinte projeto consiste em sistematizar as técnicas apresentadas nas disiciplimas de projeto em negócios e banco de dados para atingir os objetivos definidos.

## **Metódo**

O projeto deve seguir o seguinte método:

### Entendimento do negócio:
- 1. Oferecer uma contextualização do contexto do negócio e da necessidade da solução que seu grupo irá propor.
	- O ENEM (Exame Nacional do Ensino Médio), a princípio criado para avaliar a qualidade do ensino brasileiro. É hoje a principal forma de ingresso nas instituições de ensino superior. Com uma média de mais de 4 milhões de inscritos nos últimos 5 anos,<sup>[1](https://brasilescola.uol.com.br/educacao/o-que-e-enem.htm)</sup> os microdados do exame podem fornecer informações valiosas sobre os diversos perfis de alunos e como as escolas poderiam melhorar seus desempenhos.

- 2. Estabelecer claramente o objetivo do trabalho.
	- A partir de questões que englobam a percepção de aprendizagem do aluno, sua gestão de tempo, práticas de estudo, rotina, acesso a tecnologia e a infraestrutura, o projeto tem como adjetivo mapear os principais hábitos dos alunos com sua performance no ENEM. Ao disponibilizar tal análise para as escolas, é possível estruturar um planejamento para minimizar as dificuldades e reforçar as qualidades mais relevantes para otimizar o desempenho dos alunos na prova.

3. Implementar o projeto. (Entendimento, preparação e modelagem dos dados).
4. Analisar como a implementação atende ao objetivo proposto. (Avaliação e implementação).
5. Conclusão.

## **Requisitos do projeto**

**Banco de Dados**

O projeto deve considerar os seguintes requisitos:

- REQ#01: Definir pelo menos uma função para realizar tarefas específicas.
- REQ#02: Identificar um dataset.
- REQ#03: Construir um modelo conceitual.
- REQ#04: Construir um modelo lógico.
- REQ#05: Construir um físico.
- REQ#06: Popular o BD a partir do dataset.
- REQ#07: Criar 10 questões para que o BD responda.
- REQ#08: O relatório do projeto deve ser desenvolvido e entregue em um caderno Jupyter.
- REQ#09: O projeto deve ser apresentado para a banca na data estipulada.


**Machine Learning**

- REQ#01: Utilizar um ou mais datasets (não pode ser toy) para o treinamento dos classificadores(*).
- REQ#02: Realizar uma análise exploratória do dataset por meio de um caderno Jupyter. Utilize gráficos na análise.
- REQ#03: Treinar um classificador kNN.
- REQ#04: Treinar um classificador de Regressão Linear.
- REQ#05: Treinar um classificador de Regressão Logística.
- REQ#06: Treinar um classicador Naive Bayes (Multinomial, Bernoulli ou Gaussian).
- REQ#07: Treinar um classificador Support Vector Machine (SVM) (desejável).
- REQ#08: Treinar um classificador de Árvore de Decisão ou Floresta Aleatória.
- REQ#09: Todos os classificadores devem ser avaliados com 30% dos dados, utilizando as métricas F1, acurácia, revocação (recall), precisão. Além disso, utilizem a matriz de confusão para a visualização do desempenho.
- REQ#10: Todos os classificadores devem ser persistidos (joblib, pickle) antes de serem entregues.
