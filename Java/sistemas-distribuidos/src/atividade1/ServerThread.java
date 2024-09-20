package atividade1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintStream;
import java.net.Socket;

public class ServerThread extends Thread{
	private Socket socket;
	public ServerThread(Socket socket) {
		this.socket = socket;
	}
	public void run() {
		System.out.println("Cliente conectado");
		try {
			InputStreamReader isr = new InputStreamReader(this.socket.getInputStream());
			BufferedReader entrada = new BufferedReader(isr);
			PrintStream saida = new PrintStream(this.socket.getOutputStream());
			String x = entrada.readLine();
			System.out.println("Cliente: " + x);
			saida.println("World!");
			System.out.println("World -> enviado");
			this.socket.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}
