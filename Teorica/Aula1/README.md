# 1.1 O que é NoSQL?

---

Não seguem a popular e bem conhecida filosofia dos bancos de dados SQL “Not Only SQL”.

# 1.2. Principais Objetivo do NoSQL

---

- Bancos NoSQLs vieram para complementar os BD’s SQL
- Esquema de armazenamento de dados maleável (Schemaless): Em suam, suma não é necessário criar uma estrutura de Bd inicialmente para começar a usa-lá e novos tipos de dados podem ser adicionados facilmente
- Escalabilidade horizontal: Adiciona reorganize nós de armazenamento dedados com facilidade, sem a necessidade de para o serviço quando isso acontecer;
- Seguem o modelo Base de operação ao invés do ACID (seguido pelos BD’s relacionais)

# 1.3. O modelo Base

---

- BA - algumas partes do sistema ficam disponíveis mesmo após uma falha, mas não disponível por completo;
- S - ao acontecer uma operação de escrita, exclusão, ou atualização, em um dado do BD, o sistema não avisa todas as réplicas
- E - em um mesmo momento no tempo, pode se ter 2 valores diferentes para um mesmo dado que está em diferentes nós, até que o banco os sincronize.

# 1.4. Tipos de dados NoSQL

- DOCUMENTOS
    - Armazenados em Jsons
    - Criação rápida de novos atributos em documentos individuais
    - Não possuem esquemas, mas sim Coleção de documentos
    - Não existe relacionamento natural, um documento pode possuir todas as informações necessárias (evitando uma consulta adicional a outro documento)
    - Exemplo: armazenar de forma simples comentários de um post
- GRAFOS
    - Representa os dados ou esquemas dos dados como grafos dirigidos;
    - Interessante em casos quando a interconectividade dos dados são muito importantes;
    - Formado por três componentes básicos: Nós (Vértices), Relacionamentos(Arestas) e propriedades (atributos dos nós e relacionamentos)
    - Tabela de adjacência com todos as relações.
        
        ![Untitled](Sem%20ti%CC%81tulo%2072d68727d01241bcbe00a3cfc7f84843/Untitled.png)
        
    - Exemplos de uso: relações entre personagens, relações de clientes com produtos
        
        ![Untitled](Sem%20ti%CC%81tulo%2072d68727d01241bcbe00a3cfc7f84843/Untitled.jpeg)
        
        ![Untitled](Sem%20ti%CC%81tulo%2072d68727d01241bcbe00a3cfc7f84843/Untitled%201.png)
        
- CHAVE-VALOR
    - Armazena dados como um conjunto de pares chaves-valor, chave ( identificador exclusivo).
    - Chaves e valores podem ser qualquer coisa, desde objetos simples até objetos compostos complexos;
    - Um dos modelos de BD’s NoSQL de maior performance por conta da sua estrutura simples
    - Apesar de consultas rápidas o banco fica cada vez mais pesado.
    - Geralmente usados para criação de “cache” de dados que precisam ter um desempenho diferenciado
    - Exemplo acessar dados com rapidez sendo usados por um usuário em acesso em uma plataforma web.
- COLUNAS
    - Colunares são otimizados para recuperação rápida de colunas.
    - Reduz expressivamente custo de I/O ( input/output ) para operações no BD.
    - Evita consumir espaço quando existem valores nulos.
    - Colunas são capazes de armazenar qualquer tipo de dado, desde que o dado possa se transformar em um Array de bytes.
    - Armazena qualquer tipo de dado.
    - Baseado em “Famílias Colunares”
