#include <utility>


class Distribution {
private:
    long long c;	//scaling
    long long d;	//modulus
    long long seed; 	//internal seed

public:
    Distribution(long long c_init = 16087, long long d_init = 2147483647, long long seed_init = 1);
	
    
    double random();

    double uniform(double a = 0.0, double b = 1.0);
    
    std::pair<float, float> normal();
};

