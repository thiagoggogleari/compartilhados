# Bot de Telegram com Controle de Acesso

Este é um modelo de bot para o Telegram, desenvolvido em Python, que oferece um sistema robusto de controle de acesso, registro de logs e um fluxo de aprovação de novos usuários diretamente pelo administrador.

## Funcionalidades

- **Controle de Acesso:** Apenas usuários previamente autorizados podem interagir com os comandos do bot.
- **Registro de Logs:** Todas as interações (comandos enviados) são salvas em um arquivo de log com data, hora, nome do usuário e ID.
- **Aprovação de Novos Usuários:** Quando um novo usuário tenta se registrar, o administrador recebe uma notificação com botões de ação (inline keyboard) para aprovar ou negar o acesso com um único clique.
- **Armazenamento em Arquivos:** Os dados de usuários autorizados e os logs de atividade são armazenados localmente em arquivos de texto (`.txt`).
- **Fácil Configuração:** O bot pode ser configurado rapidamente alterando apenas 4 variáveis no início do script.

## Como Funciona

1.  **Verificação de Usuário:** Para a maioria dos comandos, o bot primeiro verifica se o ID do usuário que enviou a mensagem está na lista de `usuarios_autorizados.txt`.
2.  **Solicitação de Acesso:** Se um usuário não autorizado envia o comando `/start`, ele recebe uma instrução para solicitar acesso com o comando `/registrar SEU_NOME`.
3.  **Notificação ao Admin:** Ao receber uma solicitação de registro, o bot envia uma mensagem privada para o `chatID_admin` contendo o nome e o ID do solicitante, juntamente com os botões "SIM" e "NÃO" para autorização.
4.  **Liberação de Acesso:** Se o administrador clicar em "SIM", o ID do novo usuário é adicionado ao arquivo `usuarios_autorizados.txt`, e o usuário recebe uma mensagem de boas-vindas, confirmando que seu acesso foi liberado. Se o administrador clicar em "NÃO", o usuário recebe uma mensagem informando que seu acesso não foi autorizado. Em ambos os casos, o administrador é notificado da ação.
5.  **Registro de Atividades:** Cada comando recebido pelo bot é registrado no arquivo `logs_telegram.txt`, facilitando o monitoramento.

## Configuração

Para colocar o bot em funcionamento, siga os passos abaixo no arquivo `bot_telegram_controle.py`:

1.  **Token do Bot:** Insira o token do seu bot na variável `token_telegram_bot`.
    ```python
    token_telegram_bot = "SEU_TOKEN_AQUI"
    ```
2.  **Pasta de Arquivos:** Defina o caminho para uma pasta onde os arquivos de log e de usuários serão salvos. O script precisa de permissão de leitura e escrita neste local. Por padrão, os arquivos serão criados no mesmo diretório do código em execução.
    ```python
    pasta_arquivos = './'
    ```
3.  **ID do Administrador:** Atualize a variável `chatID_admin` com o seu Chat ID do Telegram.
    - **Como obter o Chat ID?** Execute o script (mesmo com o ID `000000000`), envie o comando `/minhaid` para o seu bot e ele retornará seu nome de usuário e ID.
    ```python
    chatID_admin = 123456789  # Substitua pelo seu ID
    ```
4.  **Reinicie o Bot:** Após preencher as variáveis, salve o arquivo e execute o script novamente. O bot estará pronto para uso.

## Comandos Disponíveis

-   `/start`: Inicia a interação. Usuários autorizados recebem uma mensagem de boas-vindas. Usuários não autorizados recebem instruções para solicitar acesso.
-   `/minhaid`: Retorna o nome de usuário e o Chat ID do Telegram de quem enviou a mensagem. Este comando não possui restrição de acesso.
-   `/registrar SEU_NOME`: Envia uma solicitação de acesso para o administrador do bot.
-   `/exemplo`: Um comando de exemplo que demonstra a estrutura de verificação de usuário.

## Estrutura de Arquivos Gerados

O bot criará e gerenciará os seguintes arquivos na pasta definida em `pasta_arquivos`:

-   `usuarios_autorizados.txt`: Armazena o nome e o ID de cada usuário com permissão para usar o bot, um por linha.
-   `logs_telegram.txt`: Registra todos os comandos que o bot recebe, incluindo timestamp, nome, ID do usuário e o texto da mensagem.

## Imagens
**Tela usuário:**

![user1](images/user1.jpg)

![user](images/user.jpg)


**Tela admin:**
![admin](images/admin.jpg)

![admin1](images/admin1.jpg)
