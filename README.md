# faker-hotkeys

Sabe quando você vai testar um formulário e precisa fornecer um CPF de mentira?
Existem vários sites que facilitam essa tarefa e geram o CPF pra você.


Pois bem. Esta ferramenta facilita ainda mais esse trabalho.
Com apenas 2 atalhos de teclado, você facilmente gera diversos tipos de informação.

## Instruções de uso
1. Instale o python 3.9
2. Baixe o código
3. Execute o main.py (de preferência em background)
4. Aperte Ctrl + Alt + H e aparecerá uma janela com os comandos disponíveis

![demonstração](https://i.ibb.co/GWkHNps/ezgif-com-gif-maker.gif)


## Customização
Os atalhos usam o esquema de [hotkeys do pynput](https://pynput.readthedocs.io/en/latest/keyboard.html#global-hotkeys)
### Atalho global
Basta editar o atalho onde está escrito `'<ctrl>+<alt>+h': on_activate`
### Comandos
Recomendo usar teclas únicas aqui, para não conflitar com os atalhos do programa que você estiver usando.

Os itens do array `self.hotkeys`:

1. tecla ou atalho
2. rótulo do comando
3. descrição do comando
4. função que irá executar com o comando
