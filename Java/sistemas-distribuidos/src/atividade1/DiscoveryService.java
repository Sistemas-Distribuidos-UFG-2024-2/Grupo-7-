package atividade1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;
import java.util.List;

public class DiscoveryService {
	private static List<String> servidores =  new ArrayList<>();
	public static void main(String[] args) {
		ServerSocket serverReceiver = null;
		ServerSocket serverSender = null;
		Socket socketReceiver;
		try {
			serverReceiver = new ServerSocket(4998);
			serverSender = new ServerSocket(4999);
			System.out.println("Servidores Receiver e Sender criados");
		} catch (IOException e) {
			System.out.println("Portas em uso");
			e.printStackTrace();
		}
		if(serverReceiver != null && serverSender!=null) {
			DiscorevyServiceThread thread = new DiscorevyServiceThread(serverSender);
			thread.start();
			HealthCheckerThread health = new HealthCheckerThread();
			health.start();
			//Bloco abaixo é reponsável por escutar os servidores que querem anunciar seus IP/porta
			while(true) {
				try {
					socketReceiver = serverReceiver.accept();
					System.out.println("Servidor Conectado");
					InputStreamReader isr = new InputStreamReader(socketReceiver.getInputStream());
					BufferedReader entrada = new BufferedReader(isr);
					String servidor = entrada.readLine();
					DiscoveryService.recebeServidor(servidor);
					System.out.println("Lista de servidores atualizada");
					socketReceiver.close();
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
