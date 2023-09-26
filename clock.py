from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess

# Função que será executada a cada 20 minutos
def enviar_mensagem_jogo():
    subprocess.call(["python", "enviar_mensagem_jogo.py"])

# Configuração do agendador
scheduler = BlockingScheduler()
scheduler.add_job(enviar_mensagem_jogo, 'interval', minutes=20)

if __name__ == '__main__':
    scheduler.start()
