#include <iostream>

class Ventana{
	private: bool abierta;
	
	public: Ventana();
		bool estado();
		void abrir();
		void cerrar();		
};

Ventana::Ventana(){
}

bool Ventana::estado(){
	return abierta;
}

void Ventana::abrir(){
	abierta = true;
}

void Ventana::cerrar(){
	abierta = false;
}
