import time
from telegram import Bot, ParseMode

# Função para enviar uma mensagem de resposta
def enviar_resposta(bot, chat_id):
    resposta = (
        f"🔒 <b>SINAL FINALIZADO</b> ✅\n\n"
        f"🤑 <b>Recolha seu lucro e fique atento à próxima oportunidade!</b>\n"
        f"🎁 <b>Se ainda não se cadastrou, CADASTRE-SE AQUI</b>\n\n"
        f"🎰🔎 Nossas <b>inteligências artificiais</b> estão buscando novas oportunidades..."
    )
    bot.send_message(chat_id=chat_id, text=resposta, parse_mode=ParseMode.HTML)
    print("Mensagem de resposta enviada")

# Lê as configurações do arquivo "config.txt"
config = {}
with open("config.txt", 'r') as file:
    for line in file:
        key, *value = line.strip().split(': ')
        config[key] = value[0] if value else None

BOT_TOKEN = config.get("TOKEN")
CANAL_IDS = config.get("CANAL_IDS", "").split()

def enviar_mensagem(bot, chat_id, mensagem, reply_markup=None):
    try:
        bot.send_message(chat_id=chat_id, text=mensagem, parse_mode=ParseMode.HTML, reply_markup=reply_markup)
        print(f"Mensagem de resposta enviada para o canal {chat_id}!")

    except Exception as e:
        print(f"Erro ao enviar mensagem de resposta para o canal {chat_id}: {str(e)}")

bot = Bot(token=BOT_TOKEN)

# Função principal que envia mensagens de resposta
def enviar_respostas_principal():
    for chat_id in CANAL_IDS:
        enviar_resposta(bot, chat_id)

# Chame esta função para enviar mensagens de resposta
enviar_respostas_principal()
