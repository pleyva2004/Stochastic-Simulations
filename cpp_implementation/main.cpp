#include <iostream>
#include <cmath>
#include "distributions.h"






double g(double x){

	return std::exp(-x) / (1 + x * x);

}





int main() {


	Distribution dist;

	int k = 100000;
	double sum = 0.0; // using double to avoid memory overflow

	for (int i = 0; i < k; i++){
		double u = static_cast<double>(dist.random());	// U(0,1)
		
		double x = 1.0f/u - 1.0f;	// tranform to fit 0,infinity bounds

		double y = g(x) / (u * u);	// g(1/u - 1) * 1/u^2
		
		sum += y;

	}

	double estimate = sum/k;		// Weighted Average

	std::cout << "Estimated Integral: " << estimate << std::endl;
	
	return 0;

}
