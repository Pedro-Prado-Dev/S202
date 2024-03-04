# Banco Orientados a Documentos

Diferente dos BD’s relacionais, BD’s Orientados a Documentos possuem como filosofia conter todas as informações importantes sobre algo em um único documento, ao invés de quebra-las em parte.

Foram feitos para guardar e buscar documentos JavaScript Object Notation (JSON), formato simplificado e muito popular dentro do desenvolvimento de software.

Um documento Json é formado por um conjunto de pares do tipo KEY:VALUE. Os pares são separados por “,” e encapsulados dentro de { (abre e fecha chaves).

Um ponto muito importante nestes BDs é identificar quais campos a serem armazenados podem exigir múltiplos valores. Estes campos serão candidatos a serem documentos mais internos ou Lista de Valores.

O Esquema(Schema) de um documento é flexível e auto descritivo. Não é necessário defini-lo antes de usá-lo, ou seja, campos podem variar de documento para documento e podem ter suas estruturas modificadas a qualquer momento.