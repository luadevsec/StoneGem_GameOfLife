# StoneGem_GameOfLife

um projeto participante de uma jam baseada em ascii2 e python vanila puro (para converter para StoneScript)

## arquitetura

esse projeto deve ser constrido de forma modular e otimizada, pois é realmente dificil converter para um codigo de stonescript compativel.

a ideia é seguir as recomendações do cleancode e outras coisas de uncle Bob.

a composição da ideia é a seguite:

1. precisamos **Gerar** um grid, ou, placa celular, para seu observada pelas leis de conway.
2. precisamos **Visualizar** essa placa em um formato grafico, que no caso seria em ascii2.
3. precisamos **Executar** todas as 4 leis de conway, sendo elas
   1. toda celula **Morta** com **3 vizinhos vivos** se torna **viva** (nascimento)
   2. toda celula **viva** com **menos de 2** vizinhos **vivos** se torna **morta** (isolamento)
   3. toda celula **viva** com **mais de 3** vizinhos **vivos** se torna **morta** (superpopulação)
   4. toda celula **viva** com **2 ou 3** vizinhos **vivos** continua **viva** (sociedade)
4. precisamos então coletar e **juntar** todos os acontecimentos das leis em um novo grid.
5. e então precisamos **visualizar** o novo grid, voltando para a etapa 2.
