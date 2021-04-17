# Pokemon-Okynaua-Edition
Um trabalho feito no começo de 2021 para o final do Introcomp

Por Okynaua (Samuel Rodrigues Ferreira)

Arte do Menu Por: Pedro Brites (@ph_braitzz)

Beta Testers: Lanix, UrsaPolarPontual e Fafale

Músicas Extras:
Dark, Darker, Yet Darker por The Great Anansi
An Ending por Toby Fox

Fórmula do Dano tirada de https://bulbapedia.bulbagarden.net/wiki/Damage
Valores e informações dos ataques tirados de https://pokemondb.net/move/
Todos os Pokemons estão no Nível 21


Observações a serem destacadas:

Eu notei que o jogo parava de responder em alguns momentos, principalmente depois ou durante uma animação.
Pesquisei e achei essa pergunta no stackoverflow: https://stackoverflow.com/questions/20165492/pygame-window-not-responding-after-a-few-seconds
Decobri que o jogo precisava se comunicar com o sistema, então no código há alguns pygame.event.get() "soltos", para que a janela não pare de responder.

Os Beta Testers (também conhecidos como meus amigos) relataram que quando pressionavam Enter várias vezes durante uma animação de ataque, ao entrar nos menus de seleção de ação ou de ataque, uma opção era escolhida sozinha, instantaneamente.
Para resolver isso, criei a função conserta_enter_adiantado, no jogo.py, que é chamada no começo do loop da batalha. Ela desativa todos os Enters ativados antes da hora.


EASTER EGG
Ao interagir com a Bolsa durante a batalha, você vai notar que possui um item, Item Misterioso. Segundo sua descrição, ele só pode ser usado quando ambos os pokémons estiverem no carmesim.

Se quiser resolver o mistério, vá em frente, mas aqui está a resposta:





SPOILER!

Carmesim é um tom de vermelho, portanto, os dois Pokémons devem estar com a vida vermelha para você utilizar o Item Misterioso.
Ao utilizar o item devidamente, ele te levará para uma batalha secreta com o famoso Pokémon "Erro" MissingNo.
Você deverá usar os dois Pokémons que escolheu para lutar contra o destemido MissingNo.
Boa Sorte :)
