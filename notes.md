# Anotações do Projeto RPG Terminal

Este documento explica, em linguagem simples, os elementos que existem no projeto. Ele não ensina apenas como o código funciona: também mostra para que cada parte serve dentro do jogo.

## 1. Visão geral do projeto

O projeto é um RPG simples executado no terminal. Ele organiza o jogo em classes, que funcionam como moldes para criar personagens, monstros, itens e outros elementos.

Atualmente, o projeto contém:

- Personagens controláveis: Guerreiro, Mago e Arqueiro.
- Monstros com vida, ataque e defesa.
- Itens como poções, armas e armaduras.
- Um inventário com capacidade máxima de 20 itens.
- Habilidades especiais.
- Testes automáticos com pytest para verificar algumas regras.

Pasta principal: `src/models/`.

---

## 2. Conceitos básicos usados no código

### Classe

Uma classe é um modelo usado para criar objetos. Por exemplo, a classe `Guerreiro` é o modelo usado para criar um personagem chamado Conan.

### Objeto

Um objeto é uma criação baseada em uma classe. Cada personagem criado existe como um objeto separado e pode ter seus próprios valores de vida, mana e equipamento.

### Atributo

Atributo é uma informação guardada dentro de um objeto. Por exemplo:

- `nome_personagem`
- `vida`
- `mana`
- `dano_base`

### Método

Método é uma ação que o objeto pode realizar. Por exemplo:

- `atacar()`
- `receber_dano()`
- `usar()`
- `adicionar_item()`

### Construtor

O construtor é o método chamado `__init__`. Ele prepara o objeto assim que ele é criado.

Exemplo:

```python
guerreiro = Guerreiro("Conan")
```

Nesse caso, o construtor do guerreiro define sua vida inicial, mana inicial e dano básico.

### Encapsulamento

Encapsulamento significa proteger os dados e controlar como eles podem ser alterados. No projeto, isso aparece principalmente nas propriedades `vida`.

A vida não pode ficar negativa: ao tentar definir uma vida menor que zero, o sistema ajusta o valor para zero.

### Herança

Herança permite que uma classe reutilize características de outra. Por exemplo:

- `Guerreiro`, `Mago` e `Arqueiro` herdam de `Personagem`.
- `Pocao_Cura`, `Arma` e `Armadura` herdam de `Item`.
- `GritoDeGuerra` herda de `Habilidade`.

### Classe abstrata

Uma classe abstrata serve como um modelo incompleto. Ela define o que as classes filhas devem possuir, mas não pode ser usada diretamente para criar objetos.

No projeto, `Personagem`, `Item` e `Habilidade` são exemplos de classes abstratas.

### Propriedade

Uma propriedade permite ler ou alterar um atributo com regras adicionais. Por exemplo, a propriedade `vida` impede que a vida ultrapasse limites inválidos.

---

# 3. Personagens

Arquivo: `src/models/personagem.py`

Classe principal: `Personagem`

Essa classe representa a base de todos os personagens jogáveis.

## Atributos da classe Personagem

| Atributo | Significado |
|---|---|
| `nome_personagem` | Nome escolhido para o personagem. |
| `vida_maxima` | Maior quantidade de vida que o personagem pode possuir. |
| `mana_maxima` | Maior quantidade de mana que o personagem pode possuir. |
| `vida` | Vida atual do personagem. |
| `mana` | Mana atual do personagem. |
| `inventario` | Inventário pertencente ao personagem. |
| `arma_equipada` | Arma que o personagem está usando; começa como `None`, ou seja, nenhuma. |
| `armadura_equipada` | Armadura que o personagem está usando; começa como `None`, ou seja, nenhuma. |
| `dano_base` | Dano básico do personagem sem considerar uma arma. |
| `buff_ataque` | Valor reservado para representar um aumento temporário de ataque. Atualmente não é usado pelas classes implementadas. |

## Métodos da classe Personagem

### `__init__(nome_personagem, vida, mana, dano_base)`

Cria um personagem e prepara todos os seus valores iniciais.

Como `Personagem` é abstrata, esse método normalmente é chamado pelas classes Guerreiro, Mago e Arqueiro.

### `atacar()`

É uma ação abstrata. Isso significa que cada tipo de personagem precisa definir como realiza seu ataque.

Nas classes implementadas, o dano é a soma do dano básico com o dano da arma equipada.

### `esta_vivo()`

Retorna `True` quando a vida é maior que zero e `False` quando o personagem está morto.

Exemplo simples:

- Vida igual a 10: está vivo.
- Vida igual a 0: não está vivo.

### `tem_mana()`

Retorna `True` quando existe mana disponível e `False` quando a mana atual é zero ou menor.

### `usar_habilidade()`

É uma ação abstrata que deve ser implementada por cada tipo de personagem.

Nas classes atuais, ela retorna o valor `25`, mas não executa uma habilidade especial completa.

### `vida` — getter

Permite consultar o valor atual da vida.

### `vida` — setter

Permite alterar a vida aplicando limites:

- Vida menor que zero vira zero.
- Vida maior que a vida máxima vira a própria vida máxima.
- Valores dentro dos limites são mantidos.

### `receber_dano(dano)`

Faz o personagem perder vida.

Se houver uma armadura equipada:

1. A defesa da armadura é subtraída do dano recebido.
2. Se o dano ficar menor que zero, o dano efetivo vira zero.
3. Apenas o dano efetivo é retirado da vida.

Exemplo:

- Dano recebido: 30
- Defesa da armadura: 20
- Vida perdida: 10

Se não houver armadura, toda a quantidade do dano é retirada da vida.

---

# 4. Classes de personagens jogáveis

## Guerreiro

Classe: `Guerreiro`

Valores iniciais:

- Vida máxima: 120
- Mana máxima: 20
- Dano base: 50

É o personagem mais resistente e com maior dano básico.

### `atacar()`

Retorna o dano base do guerreiro. Se houver arma equipada, soma o dano da arma.

### `usar_habilidade()`

Atualmente retorna `25`.

---

## Mago

Classe: `Mago`

Valores iniciais:

- Vida máxima: 90
- Mana máxima: 80
- Dano base: 20

É o personagem com mais mana, mas com menos vida e dano básico.

### `atacar()`

Retorna o dano base do mago mais o dano da arma equipada, quando existir uma.

### `usar_habilidade()`

Atualmente retorna `25`.

---

## Arqueiro

Classe: `Arqueiro`

Valores iniciais:

- Vida máxima: 95
- Mana máxima: 30
- Dano base: 40

É um personagem intermediário em vida e mana.

### `atacar()`

Retorna o dano base do arqueiro mais o dano da arma equipada, quando existir uma.

### `usar_habilidade()`

Atualmente retorna `25`.

---

# 5. Monstro

Arquivo: `src/models/monstro.py`

Classe: `Monstro`

Um monstro representa um inimigo que possui informações próprias de combate.

## Atributos

| Atributo | Significado |
|---|---|
| `nome` | Nome do monstro. |
| `vida` | Vida atual do monstro. |
| `ataque` | Dano causado ao atacar. |
| `defesa` | Quantidade de dano que pode bloquear. |

## Métodos

### `__init__(nome, vida, ataque, defesa)`

Cria o monstro com todos os valores básicos necessários para o combate.

### `vida` — getter

Permite consultar a vida atual do monstro.

### `vida` — setter

Impede que a vida do monstro seja menor que zero.

### `receber_dano(dano)`

Calcula o dano efetivo retirando a defesa do monstro.

Se o resultado for menor que zero, o dano efetivo vira zero.

### `atacar()`

Retorna o valor de ataque do monstro.

---

# 6. Itens

Arquivo: `src/models/item.py`

## Classe Item

`Item` é a base para todos os itens do jogo.

### Atributos

| Atributo | Significado |
|---|---|
| `nome` | Nome do item. |
| `tipo` | Categoria do item, como poção, espada ou armadura. |
| `descricao` | Explicação sobre o que o item representa ou faz. |
| `valor` | Valor comercial do item. |
| `peso` | Peso do item. |

### Método `usar(alvo)`

É abstrato. Cada tipo de item precisa decidir o que acontece ao ser usado.

O método deve receber o personagem que será afetado pelo item.

---

# 7. Poção de cura

Classe: `Pocao_Cura`

## Atributos

Além dos atributos herdados de `Item`, possui:

| Atributo | Significado |
|---|---|
| `cura` | Quantidade de vida que a poção recupera. |

O nome da poção é automaticamente definido como “Poção de Cura Baixo Nivel”.

Também possui os seguintes valores definidos:

- Tipo: `Poção`
- Valor: `25`
- Peso: `0.5`

## Método `usar(alvo)`

Aumenta a vida do alvo em uma quantidade igual a `cura`.

Exemplo:

- Vida atual: 30
- Cura da poção: 50
- Vida máxima: 120
- Resultado: vida igual a 80

O limite máximo é aplicado pela propriedade `vida`. Portanto, uma poção não pode deixar a vida acima da vida máxima.

O método retorna `True` depois de usar a poção.

---

# 8. Arma

Classe: `Arma`

## Atributos

Além dos atributos de `Item`, possui:

| Atributo | Significado |
|---|---|
| `dano` | Valor adicional de dano enquanto a arma estiver equipada. |

## Método `usar(alvo)`

Coloca a arma no atributo `arma_equipada` do personagem.

Depois disso, os ataques do personagem somam o dano da arma ao dano base.

Exemplo:

- Dano base: 50
- Dano da espada: 10
- Dano total: 60

Retorna `True` após equipar a arma.

---

# 9. Armadura

Classe: `Armadura`

## Atributos

Além dos atributos de `Item`, possui:

| Atributo | Significado |
|---|---|
| `defesa` | Quantidade que a armadura reduz de cada ataque recebido. |

## Método `usar(alvo)`

Coloca a armadura no atributo `armadura_equipada` do personagem.

Depois disso, o personagem perde menos vida ao receber dano.

Retorna `True` após equipar a armadura.

---

# 10. Inventário

Arquivo: `src/models/inventario.py`

Classe: `Inventario`

O inventário guarda os itens que pertencem a um personagem.

## Atributos

| Atributo | Significado |
|---|---|
| `_itens` | Lista interna que guarda os itens. O `_` indica que essa lista é considerada interna e não deve ser manipulada diretamente. |

O inventário aceita no máximo 20 itens diferentes.

## Métodos

### `adicionar_item(item)`

Tenta adicionar um item ao inventário.

Retorna `True` quando o item foi adicionado.

Retorna `False` nos seguintes casos:

- O item é `None`, ou seja, não existe.
- O mesmo item já está no inventário.
- O inventário já possui 20 itens.

### `remover_item(item)`

Remove um item existente no inventário.

Retorna `True` quando removeu o item.

Retorna `False` nos seguintes casos:

- O item é `None`.
- O item não existe no inventário.

### `listar_itens()`

Percorre todos os itens e mostra cada um no terminal.

Atualmente, ela usa `print(f"- {item}")`, mas não define uma apresentação personalizada para cada objeto. Como resultado, o texto exibido pode usar a representação padrão do objeto.

### `tem_item(item)`

Verifica se o item está no inventário.

Retorna `True` se estiver presente e `False` caso contrário.

### `quantidade_itens`

É uma propriedade que informa quantos itens existem no inventário.

Ela não altera o inventário, apenas informa o tamanho da lista interna.

---

# 11. Habilidades

Arquivo: `src/models/habilidades.py`

## Classe Habilidade

`Habilidade` é a base para criar habilidades especiais.

Ela é abstrata e representa uma habilidade que precisa ser aplicada por uma classe filha.

### Atributos

| Atributo | Significado |
|---|---|
| `nome` | Nome da habilidade. |
| `descricao` | Explicação do efeito da habilidade. |
| `custo_mana` | Quantidade de mana necessária para usar a habilidade. |

### Método `pode_usar(mana_atual)`

Compara a mana atual do usuário com o custo da habilidade.

Retorna `True` quando a mana é suficiente e `False` quando não é.

### Método `usar(usuario, alvo=None)`

É abstrato. Cada habilidade precisa definir seu próprio efeito.

A estrutura planejada retorna um dicionário com:

- `dano`: dano causado pela habilidade.
- `efeito`: descrição curta do efeito.
- `mensagem`: texto para mostrar ao usuário.

---

# 12. Grito de Guerra

Classe: `GritoDeGuerra`

## Atributos herdados

- Nome: `Grito de Guerra`
- Descrição: `Aumenta o ataque por 3 turnos.`
- Custo de mana: `20`

## Método `usar(usuario, alvo=None)`

Antes de aplicar o efeito:

1. Verifica se o usuário possui mana suficiente.
2. Se não possuir, retorna dano 0, efeito “Nenhum” e uma mensagem informando que não há mana suficiente.
3. Se possuir, retira 20 pontos de mana.
4. Aumenta o `dano_base` do usuário em 10.
5. Retorna uma mensagem informando que o grito foi usado.

Importante:

- O texto da descrição fala em aumento por 3 turnos.
- A implementação atual aumenta o `dano_base` diretamente.
- Não existe uma regra implementada para terminar o efeito após três turnos.
- Além disso, o código usa `usuario.nome`, mas o personagem possui o atributo `nome_personagem`. Essa diferença precisa ser corrigida antes que a habilidade funcione completamente.

---

# 13. Testes automatizados

Pasta: `tests/`

Os testes usam pytest para verificar automaticamente se as regras do jogo estão funcionando.

## Teste de ataque

Arquivo: `tests/test_personagem.py`

Verifica:

- O dano do guerreiro somado ao dano da arma.
- Se a arma foi equipada corretamente.
- Se a armadura foi equipada corretamente.
- Se vida e mana permanecem nos valores esperados.

## Testes de dano

Também em `tests/test_personagem.py`, existem testes para verificar:

- Que receber dano não aumenta a vida.
- Que a defesa da armadura reduz o dano corretamente.
- Que um personagem com vida zero ou menos é considerado morto.

## Testes da poção

Arquivo: `tests/test_item.py`

Verificam:

- Se a poção aumenta a vida.
- Se a poção não ultrapassa a vida máxima.

## Testes do inventário

Arquivo: `tests/test_inventario.py`

Verificam:

- Se um item pode ser adicionado.
- Se o item pode ser localizado no inventário.
- Se a quantidade de itens é atualizada.
- Se um item pode ser removido.

---

# 14. Como os testes são executados

Com o ambiente preparado, use:

```bash
pytest tests -v --tb=short
```

Cada teste possui o prefixo `test_`.

Um teste aprovado significa que a regra testada funcionou.

Um teste reprovado significa que o comportamento observado foi diferente do comportamento esperado.

---

# 15. Situação atual do projeto

Os testes existentes foram executados e, no estado atual, não chegaram a começar por causa de um erro de importação.

Foram encontrados os seguintes problemas:

1. `src/models/personagem.py` importa `Personagens` de `src.models.habilidades`, mas essa classe não existe em `habilidades.py`.

2. `src/models/habilidades.py` importa `Personagem` por meio de `from models.personagem import Personagem`, mas o projeto está usando o pacote `src.models`.

Como consequência, ao importar um personagem ou um item que importa personagem, o Python procura módulos incompatíveis e os testes falham durante a coleta.

Os problemas relacionados à correção desses imports devem ser resolvidos antes que os testes possam validar o restante do projeto.

---

# 16. Resumo de como as partes se relacionam

## Personagem

- Possui um inventário.
- Pode equipar uma arma.
- Pode equipar uma armadura.
- Pode atacar.
- Pode receber dano.
- Pode usar habilidades.

## Item

- Pode representar poções, armas ou armaduras.
- Pode ser usado em um personagem.

## Inventário

- Guarda itens do personagem.
- Impõe um limite de 20 itens.
- Impede duplicatas do mesmo objeto.

## Monstro

- Possui vida, ataque e defesa.
- Pode atacar.
- Pode receber dano considerando sua defesa.

## Habilidade

- Possui custo de mana.
- Pode verificar se está disponível.
- Pode aplicar efeitos em personagens.

---

# 17. Observações para estudo

## `None`

`None` representa “não existe” ou “nenhum valor”.

Exemplo: `arma_equipada = None` significa que o personagem não está usando uma arma.

## `True` e `False`

São respostas booleanas:

- `True`: positivo, verdadeiro ou realizado.
- `False`: negativo, falso ou não realizado.

## `pass` e `...`

Indicam partes ainda vazias ou abstratas que podem ser implementadas pelas classes filhas.

## Dicionário

Um dicionário guarda informações em pares de chave e valor.

Exemplo da habilidade:

```python
{
    "dano": 0,
    "efeito": "Aumento de Ataque",
    "mensagem": "O personagem usou o Grito de Guerra."
}
```

## POO

POO significa Programação Orientada a Objetos. Ela organiza o código em objetos que representam coisas reais ou conceitos do jogo.