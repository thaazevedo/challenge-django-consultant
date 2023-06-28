# challenge-django-consultant
- Produção do Teste Técnico para Consultor Django DigitalSys. O projeto consiste na criação de uma plataforma de empréstimo para a empresa Loans For Good (LFG).

## Inicializando o projeto usando Docker:

- O primeiro passo é realizar o clone deste repositótio.
- Após isso, faça do Download do [Docker](https://www.docker.com/products/docker-desktop/), segundo seu sistema operacional.
- Por meio do CMD/Terminal de Comando entre na pasta principal
``
loans-for-good-challenge
``
- Para iniciar o projeto, digite:
  ``
  docker-compose up --build
  ``
- Pronto, o sistema já foi inicializado.

### Compreendendo o sistema:
#### 1- Parte do Admin:
 - Acessando pelo [link](http://localhost:8000/admin/), você verá a estrutura de administração e montagem de propostas:
 - Na tela de login, use as credenciais `usuário: admin | senha: Admin123`
 - Você irá visualizar a seguinte Estrutura:
   <p float="center">
     <img src="https://github.com/thaazevedo/loans-for-good-challenge/assets/76017955/0e5193db-4d74-46cc-b561-4fb7a7d493d7">
   </p>
 - Na imagem acima, encontram-se as seções:
   
    a. Options: responsável por adicionar opções quando o campo definido para o formulário aceitar opções de seleção única;<br>
    b. Campos propostas: responsável por criar campos ao formulário;<br>
    c. Form propostas: responsável por elaborar o formulário, adicionando os campos dele e o nome da propposta;<br>
    d. Propostas: responsável pela administração da propostas após o retorno da avaliação da API de análise de Crédito.

 - Fluxo para montagem de propostas:

    a. Primeiro, acesse o menu Campos Propostas. No canto superior direito, clique no botão ADICIONAR CAMPOS PROPOSTA:
    <p float="center">
      <img src="https://github.com/thaazevedo/loans-for-good-challenge/assets/76017955/4874f574-f00e-4398-b346-8edf50333c27">
    </p> 
    b. O painel de adicionar campos de propostas será aberto, como no exemplo abaixo, preencha o nome e o tipo do campo. ATENÇÃO: em caso de campo do tipo seleção única, devem ser adicionadas opções para o campo, o que deve ser feito clickando no sinal de mais(+), na seção de options.
    <p float="center">
     <img width="600px" src="https://github.com/thaazevedo/loans-for-good-challenge/assets/76017955/03f2fb7d-bf51-4751-9705-9d39a4ecae97">
    </p> 
    
    c. Após isso, ao entrar na seção de Form Propostas, clique no botão ADICIONAR FORM PROPOSTAS, localizado no canto superior direito da tela:
    <p float="center">
     <img src="https://github.com/thaazevedo/loans-for-good-challenge/assets/76017955/78c56143-5465-48fa-bcdd-0a3830bbf64c">
    </p>
    d. Essa ação abrirá uma tela parecida com a que está abaixo, nessa tela, clique no botão Default, adicione o Nome da Proposta e selecione os campos da corrente proposta (você confirmará os campos selecionados no quadro fields escolhidos na seção Fields da tela).
    <p float="center">
     <img width="600px" src="https://github.com/thaazevedo/loans-for-good-challenge/assets/76017955/cb9bbc32-29f5-4b8d-b0f4-531aa3939832">
    </p> 
ATENÇÃO o funcionamento do botão default ocorre da seguinte forma: por padrão ele fica desabilitado e o formulário com o default preenchido será aquele cujo os campos irá ser colocado para preenchimento do cliente. Em caso de dois formulários marcados como padrão, será mostrado para o cliente o último formulário acrescentado ao sistema.<br>
    e. Após isso, o formulário será enviado para o  preenchimento da proposta pelos clientes e enviado para a avaliação automática da API.<br>
    f. O retorno será visualizado na seção de Propostas, como no exemplo abaixo. 
    <p float="center">
     <img src="https://github.com/thaazevedo/loans-for-good-challenge/assets/76017955/98833c7d-2869-4f42-a02f-6c9ac1aeaa4f">
    </p>
    g. Para análise humana por parte do administrador é possível o uso do filtro lateral. 
    <p float="center">
     <img src="https://github.com/thaazevedo/loans-for-good-challenge/assets/76017955/5ac3af62-650d-4809-b832-ce4df549be52">
    </p>
    h. Ao selecionar o filtro, basta acessar a proposta e alterar o status da proposta pretendida para aprovada ou negada.
    <p float="center">
     <img src="https://github.com/thaazevedo/loans-for-good-challenge/assets/76017955/cd76e057-94c2-40c5-9c2f-242f9dd0d3e7">
    </p>


#### 2- Parte do cliente:
 - Acessando pelo [link](http://localhost:8000/) você verá a parte destinada ao preenchimento das propostas por parte do cliente;
   <p float="center">
     <img width="600px" src="https://github.com/thaazevedo/loans-for-good-challenge/assets/76017955/1b2285f8-d48c-4446-a81e-9afaeb17522c">
   </p>
 - Após o preenchimento das informações, basta clickar no botão de Enviar proposta, e aguarder o retorno!
