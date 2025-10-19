#include "distributions.h"
#include <cmath>
#include <utility>



Distribution::Distribution(long long c_init, long long d_init, long long seed_init) : c(c_init), d(d_init), seed(seed_init) {}




double Distribution::random(){

	// Pseudorandom numbers
        // Multiplicative Congruential Method
        // Sequences that appear random; however, it is just a parametirized equation with a starting seed\

	seed = (c * seed) % d; 	


	 //Selection Process for c and d
        //Selecting large enough scaling constants for the series of events to not repeat. NOT True randomness.


        // The domain is [0, m)
        // This ratio is what creates a Range of [0,1)

	return static_cast<double >(seed)/static_cast<double>(d);	// convert to [0,1)

}

double Distribution::uniform(double a, double b){

        // Scales Uniform to (a,b)
        return a + (b - a) * random();

}


std::pair<float, float> Distribution::normal(){
	float u1 = random();

	// using extrict float operations to retain float precision and improve operations

	while (u1 <= 0.0f){ 
		u1 = random(); //Guard against 0
	}

	float u2 = random();


	float r = std::sqrt(-2.0f * std::log(u1));
					

	// static casting pi (double) into float for exact float operations and avoid silent type conversions
	float theata = -2.0f * static_cast<float>(M_PI)*u2;


	float z1 = r * std::sin(theata);
	float z2 = r * std::cos(theata);
		
	return {z1, z2};
}





