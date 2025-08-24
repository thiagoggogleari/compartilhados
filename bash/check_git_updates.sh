#!/bin/bash

# Verifica se há alterações em um repositório remoto e sinaliza via Telegram
# Sugestão de uso, colocar para rodar na crontab a cada 30 minutos

# Configurações do Telegram
BOT_TOKEN="SEU_TOKEN_AQUI"
CHAT_ID="SEU_CHAT_ID_AQUI"

# Branch que você quer monitorar
BRANCH="main"

# Diretório do repositório
REPO_DIR="/caminho/para/seu/repositorio"

# Função para enviar mensagem via Telegram
send_telegram_message() {
    MESSAGE="$1"
    curl -s -X POST "https://api.telegram.org/bot$BOT_TOKEN/sendMessage" \
        -d chat_id="$CHAT_ID" \
        -d text="$MESSAGE"
}

# Ir para o diretório do repositório
cd "$REPO_DIR" || exit

# Buscar atualizações do remoto
git fetch

# Verificar se há commits novos no remoto
COMMITS=$(git log HEAD..origin/$BRANCH --oneline)

if [ -n "$COMMITS" ]; then
    send_telegram_message "🚨 O repositório remoto foi atualizado! Commits novos:\n$COMMITS"
else
    echo "Nenhuma atualização encontrada."
fi
