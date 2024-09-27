package atividade1;

import java.io.IOException;
import java.io.ObjectOutputStream;
import java.net.ServerSocket;
import java.net.Socket;

//Thread responável por enviar a lista de servidores para os clientes
public class DiscorevyServiceThread extends Thread{
	private ServerSocket serverSender;
	private Socket socketSender;
	public DiscorevyServiceThread(ServerSocket server) {
		this.serverSender = server;
	}
	public void run () {
		while(true) {
			try {
				socketSender = serverSender.accept();
				System.out.println("Cliente Conectado");
				ObjectOutputStream objectOutputStream = new ObjectOutputStream(socketSender.getOutputStream());
				objectOutputStream.writeObject(DiscoveryService.retornaServidores());
				System.out.println("Lista retornada para cliente");
				socketSender.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
	}
}
