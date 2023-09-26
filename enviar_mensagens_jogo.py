import random
import time
from datetime import datetime, timedelta
from telegram import Bot, ParseMode, InlineKeyboardMarkup, InlineKeyboardButton

# Função para enviar mensagem de jogo
def enviar_mensagem_jogo(bot, chat_id):
    jogos_habilitados = {
        "Fortune Tiger": "🐯",  # Emoji para Fortune Tiger
        "Fortune Ox": "🐂",     # Emoji para Fortune Ox
    }

    estrategias = ["Alterne os giros entre normal e turbo, e se vier um Grande Ganho, <b>PARE</b>, e espere o próximo sinal!"]

    nomes_ia = ["IANLYS8T", "T1GD0UR", "FR33T1GR"]

    repeticoes = ["Repita a estratégia no <b>Máximo 1x</b>", "Repita a estratégia no <b>Máximo 2x</b>"]

    jogo = random.choice(list(jogos_habilitados.keys()))
    emoji_jogo = jogos_habilitados[jogo]
    nome_ia = random.choice(nomes_ia)
    estrategia = random.choice(estrategias)
    repeticao = random.choice(repeticoes)

    # Calcula horário de início e fim
    horario_inicio = datetime.now()
    horario_fim = horario_inicio + timedelta(minutes=4)

    # Formata os horários para exibição
    horario_fim_str = horario_fim.strftime("%H:%M")

    # Escolhe um valor aleatório entre 5 e 9 para Rodada Normal e atribui o mesmo valor para Rodada Turbo
    valor_rodadas = random.randint(5, 9)

    # Cria os botões inline
    teclado_inline = InlineKeyboardMarkup([
        [InlineKeyboardButton("DÚVIDAS? FALE CONOSCO!", url="https://t.me/OtigredouradoBOT")]
    ])

    mensagem_jogo = (
        f"<b>🔥 {nome_ia} DETECTOU JOGO PAGANDO 🔥</b>\n\n"
        f"{emoji_jogo} <b>{jogo}</b> {emoji_jogo}\n\n"
        f"<b>🎯 {valor_rodadas}x Normal / <b>{valor_rodadas}x Turbo 🚀</b></b>\n\n" 
        f"<b>💡 Dica:</b> {estrategia}\n\n"
        f"⏳ Sinal disponível até <b>{horario_fim_str}</b> aproximadamente\n\n"
        f"🔁 {repeticao}"
    )

    # Envia a mensagem de jogo
    try:
        bot.send_message(chat_id=chat_id, text=mensagem_jogo, parse_mode=ParseMode.HTML, reply_markup=teclado_inline)
        print(f"Mensagem de jogo enviada com sucesso para o canal {chat_id}!")

    except Exception as e:
        print(f"Erro ao enviar mensagem de jogo para o canal {chat_id}: {str(e)}")

# Lê as configurações do arquivo "config.txt"
config = {}
with open("config.txt", 'r') as file:
    for line in file:
        key, *value = line.strip().split(': ')
        config[key] = value[0] if value else None

BOT_TOKEN = config.get("TOKEN")
CANAL_IDS = config.get("CANAL_IDS", "").split()

bot = Bot(token=BOT_TOKEN)

# Função principal que envia mensagens de jogo
def enviar_mensagens_principal():
    for chat_id in CANAL_IDS:
        enviar_mensagem_jogo(bot, chat_id)

# Chame esta função para enviar mensagens de jogo
enviar_mensagens_principal()
