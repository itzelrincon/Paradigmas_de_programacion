#include <iostream>
#include "Motor.h"
#include "Rueda.h"
#include "Puerta.h"

class Coche{
	public:
		Motor motor1;
		Rueda rueda1, rueda2, rueda3, rueda4;
		Puerta puerta1, puerta2;
	public: Coche();	
};

Coche::Coche(){
	motor1(Motor)();
	rueda1(Rueda);
	rueda2(Rueda);
	rueda3(Rueda);
	rueda4(Rueda);
	puerta1(Puerta);
	puerta2(Puerta);
}
