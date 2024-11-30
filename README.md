AtividadeTestePytest
Este repositório contém uma atividade prática desenvolvida com pytest, focada em testes automatizados. O objetivo principal é demonstrar o uso de pytest para testar funcionalidades e garantir a qualidade de código.

Chaves necessarias:
API FIXER: 6bd54dcfbe23f60c1e5fd8ee255a7b98

🎯 Objetivo
Fornecer exemplos práticos de como usar o pytest para realizar testes automatizados em projetos Python. Os exemplos abordam:

Estrutura de testes.
Uso de fixtures.
Testes parametrizados.
Boas práticas em testes.

📋 Pré-requisitos
Antes de começar, certifique-se de ter o seguinte instalado em sua máquina:

Python 3.8 ou superior.
pip (gerenciador de pacotes do Python).
pytest (instalado através do pip).
requests (instalado atavés do pip).
selenium (instalado através do pip).


🚀 Como usar

1. Clone o repositório:

git clone https://github.com/kirkdouglasouza/AtividadeTestePytest.git
cd AtividadeTestePytest
2. Crie um ambiente virtual (opcional, mas recomendado):

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

3. Instale as dependências:

pip install -r requirements.txt

4. Execute os testes:

pytest


🛠️ Estrutura do Repositório

AtividadeTestePytest/
├── tests/                   # Diretório contendo os arquivos de teste.
│   ├── test_example.py      # Exemplo de testes usando pytest.
│   └── ...                  # Outros arquivos de teste.
├── src/                     # Código principal a ser testado.
│   └── ...                  # Arquivos do projeto.
├── requirements.txt         # Dependências do projeto.
├── README.md                # Documentação do repositório.
└── ...                      # Outros arquivos e configurações.


🔧 Funcionalidades

Testes Unitários: Verificação de funções e métodos isolados.
Fixtures: Configuração e limpeza do ambiente de teste.
Parametrização: Testes com múltiplos valores de entrada.
Cobertura de Testes: Medição do percentual de código testado.

📄 Referências
Documentação do pytest
Boas práticas para testes em Python


