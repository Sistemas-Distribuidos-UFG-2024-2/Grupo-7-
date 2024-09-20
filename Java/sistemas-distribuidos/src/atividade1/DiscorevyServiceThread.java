package atividade1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;

public class DiscorevyServiceThread extends Thread{
	private ServerSocket serverReceiver;
	private Socket socket;
	private InputStreamReader isr;
	private BufferedReader entrada;
	public DiscorevyServiceThread(ServerSocket server) {
		this.serverReceiver = server;
	}
	public void run () {
		while(true) {
			try {
				this.socket = serverReceiver.accept();
				System.out.println("Servidor Conectado");
				isr = new InputStreamReader(socket.getInputStream());
				entrada = new BufferedReader(isr);
				String servidor = entrada.readLine();
				DiscoveryService.recebeServidor(servidor);
				System.out.println("Lista de servidores atualizada");
				socket.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
	}
}
