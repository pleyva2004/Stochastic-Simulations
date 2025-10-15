#include <iostream>
#include <cmath>


class Distribution{

	private:

		int c;
		int d;
		int seed;
	public: 

		Distribution(int seed_init = 1, int c_init = 16087, int d_init = 2147483647) : c(c_init), d(d_init), seed(seed_init) {}

	

		float random(int x0=1){
			float x = (c*x0)%d;
			return x/d;

		}	

		float uniform(int a=0, int b=0){ 	
			return a + (b - a) * Distribution::random();

		}

		float normal(){
			float u1 = Distribution::random();

			while (u1 <= 0){ 
				u1 = Distribution::random(); //Guard against 0
			}

			float u2 = Distribution::random();


			float r = sqrt(-2 * std::log(u1));
					

			float t = 2 * 3.14159 *u2;


			float z1 = r * std::sin(r);
			float z2 = r * std::cos(r);
		
			return z1, z2;
		}
};

int main() {
	
	Distribution dist(42);
	float X, Y = dist.normal();
	std::cout << X << ", " << Y << std::endl;
	return 0;

}



