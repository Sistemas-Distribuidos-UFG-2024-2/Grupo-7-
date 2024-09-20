package atividade1;

import java.io.IOException;
import java.io.ObjectOutputStream;
import java.io.PrintStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;
import java.util.List;

public class DiscoveryService {
	private static List<String> servidores =  new ArrayList<>();
	public static void main(String[] args) {
		ServerSocket serverReceiver = null;
		ServerSocket serverSender = null;
		Socket socketSender;
		try {
			serverReceiver = new ServerSocket(4998);
			serverSender = new ServerSocket(4999);
			System.out.println("Servidores Receiver e Sender criados");
		} catch (IOException e) {
			System.out.println("Portas em uso");
			e.printStackTrace();
		}
		if(serverReceiver != null && serverSender!=null) {
			DiscorevyServiceThread thread = new DiscorevyServiceThread(serverReceiver);
			thread.start();
			while(true) {
				try {
					socketSender = serverSender.accept();
					System.out.println("Cliente Conectado");
					ObjectOutputStream objectOutputStream = new ObjectOutputStream(socketSender.getOutputStream());
					objectOutputStream.writeObject(retornaServidores());
					System.out.println("Lista retornada para cliente");
					socketSender.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
		}
	}
	
	public static void recebeServidor(String servidor) {
		servidores.add(servidor);
		System.out.println(servidores);
	}
	
	public static List<String> retornaServidores(){
		return servidores;
	}
}
