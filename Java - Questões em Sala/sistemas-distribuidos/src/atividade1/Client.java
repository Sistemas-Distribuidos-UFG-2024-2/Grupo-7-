package atividade1;

import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.PrintStream;
import java.net.ConnectException;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.List;
import java.util.Scanner;

public class Client {
	private final static String HOST = "localhost";
	private final static int PORT = 4999;
	public static void main(String[] args) throws UnknownHostException, IOException {
		Socket socket = null;
		List<String> servidores= retornaListaServidores();
		for(String servidor : servidores) {
			String[] dados = servidor.split(":");
			String host = dados[0];
			int porta = Integer.parseInt(dados[1]);
			try {
				socket = new Socket(host, porta);
				System.out.println("Conectado ao servidor "+host+":"+porta);
				break;
			}catch(IOException e) {
				System.out.println("Impossível se conectar com servidor "+host+":"+porta);
			}
		}
		if(socket !=null) {
//			Scanner scn = new Scanner(System.in); 
			//Thread responsável pela leitura das mensagens que o server enviar
			ClienteThread clientThread = new ClienteThread(socket);
			clientThread.start();
			
			PrintStream saida = new PrintStream(socket.getOutputStream());
//			String mensagem;
//			do{
//				System.out.print(": ");
//				mensagem = scn.nextLine();
//				saida.println("menagem");
//			}while(mensagem.equals(""));
			saida.println("Hello");
			System.out.println("Hello -> enviado");
		}
	}
	
	private static List<String> retornaListaServidores(){
		List<String> servidores = null;
		try {
			Socket socketReceiver = new Socket(HOST,PORT);
			ObjectInputStream objectInputStream = new ObjectInputStream(socketReceiver.getInputStream());
			servidores = (List<String>) objectInputStream.readObject();
			socketReceiver.close();
		} catch (IOException | ClassNotFoundException e) {
			e.printStackTrace();
		}
		return servidores;
	}
}
