#include <iostream>

class Puerta{
	private: bool abierta;
	
	public: Puerta();
		bool estado();
		void abrir();
		void cerrar();
};

Puerta::Puerta(){
}

bool Puerta::estado(){
	return abierta;
}

void Puerta::abrir(){
	abierta = true;
}

void Puerta::cerrar(){
	abierta = false;
}
