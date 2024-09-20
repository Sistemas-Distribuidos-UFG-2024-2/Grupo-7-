package atividade1;

import java.util.ArrayList;
import java.util.List;

public class ServerFinder {
	private static List<Integer> portas = new ArrayList<>();	
	public ServerFinder() {
	}

	public static void lancaPorta(int porta) {
		portas.add(Integer.valueOf(porta));
		System.out.println("Servidor localhost:"+porta);
	}
	public static List<Integer> retornaPortas(){
		for(int i : portas) {
			System.out.println(i);
		}
		return  portas;
	}
}
