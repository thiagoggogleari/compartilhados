# Modelo para bot do telegram com controle de acesso, regitro de logs e liberação de novos usuários por mensagem ao admin.

# Usuários e logs são salvos em 2 arquivos de texto que o código irá gerar.

import telebot
from telebot import types
import datetime


###########################################################################################################
# Configuração inicial

# 1 - Inserir token do bot.
token_telegram_bot = "SEU_TOKEN_AQUI"  
bot_telebot = telebot.TeleBot(token_telegram_bot, parse_mode=None) 

# 2 - Inserir o caminho para uma pasta que será utilizada para armazenar os usuários e logs. 
# Pasta deve ter permissão de escrita e leitura
pasta_arquivos = '/home/thiago/Documents/repos/jobs/'

# 3 - Atualizar o chat id do usuário. Caso não saiba, é possível colocar agora mesmo este código para rodar e enviar /minhaid para o bot que ele irá retornar o código.

chatID_admin = 0000000000

# 4 - Após atualizar chatID_admin, reiniciar o código. Pronto.
###########################################################################################################

# Emojis para utilizar em suas mensagens
emoji_foguete = "\U0001F680"
emoji_losango_azul = "\U0001F539"
emoji_warning = "\U000026A0"
emoji_critical = "\U0001F6A8"
emoji_ok = "\U00002705"
emoji_x_vermelho = "\U0000274C"
emoji_caixa_correio = "\U0001F4EC"
emoji_estrela = "\U00002B50"
emoji_cadeado_chave = "\U0001F510"
emoji_chave = "\U0001F511"
emoji_cadeado_aberto = "\U0001F513"
emoji_flecha_direita = "\U000023E9"
emoji_flecha_vermelha_baixo = "\U0001F53B"
emoji_papel_lapis = "\U0001F4DD"
emoji_relampago = "\U000026A1"
emoji_losango_laranja = "\U0001F538"

# Nome dos arquivos que serão gerados
path_autorizados = pasta_arquivos + 'usuarios_autorizados.txt'
path_log = pasta_arquivos + 'logs_telegram.txt'

print("\nLocal")
print("\nautorizados:")
print(path_autorizados)
print("\nlogs")
print(path_log)

print()
print("*"*25)
print("Código em execução")
print("*"*25)

###########################################################################################################
# Funções controle de acesso
###########################################################################################################

# Verifica se o usuário está autorizado
def consulta_usuario(id):
    print("Entrou na função 'consulta_usuario'")
    try:
        with open(path_autorizados, 'r') as file:
            linhas = file.readlines()          
        linhas = [linha.strip() for linha in linhas]
        if(str(id) in linhas):
            print("Usuário encontrado")
            return True
            
        else:
            print("Usuário não encontrado")
            return False
    except FileNotFoundError:
        print("Arquivo não encontrado")
        with open(path_autorizados, 'w') as file:
            print("Arquivo consulta_usuario.txt criado\n")
            file.write("Consulta_usuarios" + '\n')
     

# Insere uma linha com registro de nome e id no arquivo
def adiciona_novo_usuario(array_nome_id):
    try:
        with open(path_autorizados, 'a') as file:
            for elemento in array_nome_id: 
                file.write(elemento + '\n')
    except FileNotFoundError:
        print("Erro de arquivo não encontrado!!\n\n")
        with open(path_autorizados, 'w') as file:
            for elemento in array_nome_id: 
                file.write(elemento + '\n')
        

# Log de comandos enviandos
def registra_log(message):
    print("Entrou na função 'registra_log'")
    usuario = message.from_user.first_name
    id_user = message.from_user.id

    data_hora_atual = datetime.datetime.now()
    time_stamp = data_hora_atual.strftime("%d/%m/%Y %H:%M:%S")
    registro = time_stamp +" " + usuario + "/" + str(id_user) + " = " + message.text

    try:
        
        # Para desativar log de comandos do admin, descomentar if abaixo
        
        #if(id_user == chatID_admin):
            #return

        with open(path_log, 'a') as file:
            for elemento in registro: 
                file.write(elemento)
            file.write("\n")
            print("Log registrado")
    except FileNotFoundError:
        print("Arquivo de log não econtrado")
        with open(path_log, 'w') as file:
            for elemento in registro: 
                file.write(elemento)
            file.write("\n")
            print("Arquivo log_telegram.txt")

###########################################################################################################
# Handlers Telegram - Comandos

# Esta função é um exemplo de como devem ser a estrutura dos Handlers.
# Copiando este bloco e alterando 'exemplo', você cria os trechos que irão responder aos comandos do bot.
@bot_telebot.message_handler(commands=['exemplo'])
def handle_exemplo_command(message):
    print("\nHandler Exemplo")
    # Verifica se o usuário está cadastrado
    if (consulta_usuario(message.from_user.id) == True):
        print("O usuário está cadastrado. Código prossegue")
        bot_telebot.reply_to(message, emoji_estrela + ' Usuário está cadastrado')
    else:
        print("Usuário sem cadastro")
        bot_telebot.reply_to(message, emoji_estrela + ' Usuário não está cadastrado')
    

# Devolve para o usuário o seu 'first_name/id'
# Este handler não possui restrição de execução
@bot_telebot.message_handler(commands=['minhaid'])
def handle_chatid_command(message):
    print("\nHandler minhaid")
    usuario = message.from_user.first_name
    id_user = message.from_user.id
    combinado = str(usuario) + "\n" + str(id_user)
    print(combinado)
    bot_telebot .reply_to(message, combinado)


# Este handler pode ser personalizado
# Ele é executado ao usuário acessar o bot pela primeira vez ou enviar /start
@bot_telebot.message_handler(commands=['start'])
def send_welcome(message):
    print("\nHandler start")
    if (consulta_usuario(message.from_user.id) == True):
        bot_telebot.reply_to(message, emoji_foguete +' Olá, seja bem-vindo!!')
    else:
        bot_telebot.reply_to(message, emoji_warning +' Desculpe, você não está autorizado a usar este bot ' + emoji_warning + '\n\nPara solicitar acesso envie uma mensagem no seguinte formato:\n\n/registrar SEU_NOME')
        registra_log(message)


# Envia mensagem para o admin para autorização de acesso
@bot_telebot.message_handler(commands=['registrar'])
def handle_registrar_command(message):
    print("\nHandler Registrar")
    if (consulta_usuario(message.from_user.id) == False):
        bot_telebot.reply_to(message, emoji_caixa_correio + " A sua solicitação foi enviada.\n\nQuando o acesso for concedido, você será informado.")        
        usuario = message.from_user.first_name
        id_user = message.from_user.id
        array_user = str(usuario) + "/" + str(id_user)
        mensagem = message.text

        bot_telebot.send_message(chatID_admin, emoji_cadeado_chave + ' O usuário %s/%i gostaria de obter acesso ao bot.\n\nComando enviado:\n%s'%(usuario,id_user,mensagem))
        
        keyboard = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text='SIM', callback_data=array_user)
        keyboard.add(button)
        bot_telebot.send_message(chat_id=chatID_admin, text='Autorizar o acesso?', reply_markup=keyboard)
    else:
        bot_telebot.reply_to(message, "Você já possui acesso ao bot! \n¯\( ͡❛ ͜ʖ ͡❛)/¯")


# Handler de callback do botão.
# Ao ser acionado, registra o usuário em questão e manda uma mensagem para ele informando sua liberação de acesso.
@bot_telebot.callback_query_handler(func=lambda call: True)
def handle_button_press(call):
    mensagem_format = call.data

    if '/' in str(mensagem_format):
        partes = mensagem_format.split('/')
        adiciona_novo_usuario(partes)
        bot_telebot.send_message(chatID_admin, emoji_caixa_correio + ' Novo usuário cadastrado.\nEnviando mensagem de boas vindas!')
        bot_telebot.send_message(str(partes[1]), emoji_cadeado_chave +" Acesso liberado!\nAgora o bot irá responder a seus comandos.")

# Esta linha mantém o bot ativo (loop_infinito)
bot_telebot.infinity_polling()
