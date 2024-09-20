package atividade1;
import java.io.BufferedReader;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;
import java.io.InputStreamReader;
import java.io.PrintStream;

public class Server {
	private final static String HOST = "localhost";
	private final static int PORT = 4998;
	public static void main(String[] args) throws IOException {
		Scanner scanner = new Scanner(System.in);
		int porta =  scanner.nextInt();
		ServerSocket server = new ServerSocket(porta);
		try {
			Socket socket = new Socket(HOST, PORT);
			PrintStream saida = new PrintStream(socket.getOutputStream());
			saida.println("localhost:"+porta);
			socket.close();
		}catch(IOException e) {
			e.printStackTrace();
		}
		while(true) {
			Socket socket = server.accept();
			ServerThread thread = new ServerThread(socket);
			thread.start();
		}
	}
}