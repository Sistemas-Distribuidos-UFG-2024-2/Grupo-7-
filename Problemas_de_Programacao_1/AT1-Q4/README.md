# Projeto Peso Ideal - Cliente-Servidor

Este projeto implementa um sistema cliente-servidor que calcula o peso ideal de uma pessoa com base em sua altura e sexo. A comunicação entre cliente e servidor ocorre via protocolo TCP/IP, onde o cliente envia os dados (altura e sexo) e o servidor calcula e retorna o peso ideal utilizando fórmulas específicas para homens e mulheres.

## Fórmulas Utilizadas

- Para homens: `(72.7 * altura) – 58`
- Para mulheres: `(62.1 * altura) – 44.7`


## Requisitos

- Python 3.x
- Bibliotecas listadas no arquivo `requirements.txt`

## Como Instalar

1. **Clone o repositório**:


2. **Crie um ambiente virtual (opcional, mas recomendado)**:


3. **Instale as dependências**:


## Como Executar

### Iniciar o servidor

1. Primeiro, inicie o servidor. O servidor aguardará conexões do cliente para receber a altura e o sexo, calcular o peso ideal e retornar o resultado.


2. O servidor estará escutando na porta `12345` e poderá ser acessado pelo `localhost`.

### Executar o cliente

1. Em outro terminal, execute o cliente. O cliente coletará os dados do usuário (altura e sexo) e enviará ao servidor para obter o peso ideal calculado.


2. Insira a altura e o sexo quando solicitado.

## Executar os Testes

Para rodar os testes automatizados do projeto, use o comando:


Os testes garantem que as funções de cálculo e validação funcionam corretamente tanto no cliente quanto no servidor.

## Log de Atividades

O servidor registra logs de cada conexão e eventos importantes em `logs/log.txt`. O conteúdo inclui informações sobre conexões estabelecidas e erros, se houver.

## Exemplo de Uso

1. O cliente solicita a entrada do usuário:


2. O servidor realiza o cálculo com a fórmula correta:


3. O servidor retorna o peso ideal para o cliente:


4. O cliente exibe o resultado para o usuário.

## Contribuição

Se quiser contribuir com este projeto, sinta-se à vontade para fazer um fork do repositório e enviar pull requests. Sugestões e melhorias são bem-vindas!



