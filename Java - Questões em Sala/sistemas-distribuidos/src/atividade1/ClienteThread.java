package atividade1;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintStream;
import java.net.Socket;

public class ClienteThread extends Thread{
	private Socket socket;
	public ClienteThread(Socket socket) {
		this.socket=socket;
	}
	
	public void run() {
		try {
			InputStreamReader isr = new InputStreamReader(socket.getInputStream());
			BufferedReader entrada = new BufferedReader(isr);
			String x;
			while((x = entrada.readLine())!=null) {
				System.out.println("Servidor: "+x);
			}
		}catch(Exception ex) {
			ex.printStackTrace();
		}
	}

}
