# Sistema_de_Gestao_Escolar_em_Python
## 📚 Sobre o Projeto

Este projeto consiste em um protótipo de **Sistema de Gestão Escolar** desenvolvido com o framework **Django**, com o objetivo de aplicar conceitos fundamentais de desenvolvimento web, como **rotas**, **formulários**, **modelagem de dados** e **integração com banco de dados**. A aplicação tem como foco principal o **cadastro de alunos**, permitindo a criação, visualização e gerenciamento de registros por meio de uma interface simples e funcional.

A estrutura do projeto contempla a criação de um projeto Django denominado `escola` e de um aplicativo interno chamado `alunos`. Dentro deste app, foi modelada a classe `Aluno`, contendo os campos essenciais para identificação e organização dos dados:

- `nome`
- `sobrenome`
- `data de nascimento`
- `curso`

Essa modelagem permite a persistência das informações em um banco de dados **SQLite**, garantindo simplicidade e eficiência no armazenamento.

A interface do sistema inclui uma **página inicial** que serve como ponto de entrada para o usuário, oferecendo acesso direto à **área administrativa do Django**. Essa página foi desenvolvida com foco na **usabilidade**, permitindo que administradores acessem rapidamente o painel de gestão para realizar operações como **cadastro**, **edição** e **exclusão** de registros.

Para o cadastro de alunos, foi implementado um **formulário HTML** integrado ao backend Django, possibilitando a inserção de dados de forma dinâmica e segura. Os alunos cadastrados são exibidos em uma **tabela HTML organizada**, permitindo a visualização clara e objetiva das informações armazenadas.

Este protótipo representa uma **base sólida para aplicações educacionais**, podendo ser expandido futuramente com funcionalidades adicionais como:

- Autenticação de usuários
- Filtros de pesquisa
- Edição inline
- Exportação de dados
- Integração com outros sistemas acadêmicos


