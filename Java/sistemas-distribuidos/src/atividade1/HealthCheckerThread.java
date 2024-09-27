package atividade1;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import org.apache.commons.net.telnet.TelnetClient;

public class HealthCheckerThread extends Thread{
	private final int TIMEOUT = 2000;
	public void run() {
		while(true) {
			System.out.println(".");
			try {
				Thread.sleep(10000);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
			List<String> listaAntiga = DiscoveryService.retornaServidores();
			if(!listaAntiga.isEmpty()) {
				List<String> listaNova = new ArrayList<>();
				for(String servidor : listaAntiga) {
					if(testaConexao(servidor)) {
						listaNova.add(servidor);
					}
				}
				System.out.println(listaNova);
			}	
		}
	}
	public boolean testaConexao(String servidor) {
		String[] dados = servidor.split(":");
		String host = dados[0];
		int porta = Integer.parseInt(dados[1]);
		TelnetClient telnet =  new TelnetClient();
		try {
			telnet.setConnectTimeout(TIMEOUT);
			telnet.connect(host,porta);
			return true;
		}catch(IOException e) {
			return false;
		}finally {
			try {
				telnet.disconnect();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
	}
}
