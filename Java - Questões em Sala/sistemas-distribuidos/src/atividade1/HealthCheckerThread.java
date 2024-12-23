package atividade1;

import java.io.IOException;
import java.net.Socket;
import java.util.ArrayList;
import java.util.List;

public class HealthCheckerThread extends Thread{
	private final int TIMEOUT = 2000;
	public void run() {
		while(true) {
			try {
				Thread.sleep(10000);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
			List<String> listaAntiga = DiscoveryService.retornaServidores();
			if(!listaAntiga.isEmpty()) {
				System.out.println(".");
				List<String> listaNova = new ArrayList<>();
				for(String servidor : listaAntiga) {
					if(testaConexao(servidor)) {
						listaNova.add(servidor);
					}
				}
				DiscoveryService.atualizaLista(listaNova);
			}	
		}
	}
	public boolean testaConexao(String servidor) {
		String[] dados = servidor.split(":");
		String host = dados[0];
		Socket socket = null;
		int porta = Integer.parseInt(dados[1]);
		try {
			socket = new Socket(host,porta);
			return true;
		} catch (IOException e) {
			return false;
		}
	}
}
	
