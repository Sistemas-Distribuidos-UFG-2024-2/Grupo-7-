import rpyc

class AposentadoriaService(rpyc.Service):
    def on_connect(self, conn):
        pass  # Conexão estabelecida

    def on_disconnect(self, conn):
        pass  # Conexão encerrada

    def exposed_pode_aposentar(self, idade, tempo_servico):
        if idade >= 65 and tempo_servico >= 30:
            return True
        elif idade >= 60 and tempo_servico >= 25:
            return True
        return False

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    server = ThreadedServer(AposentadoriaService, port=12345)
    print("Servidor aguardando conexões...")
    server.start()