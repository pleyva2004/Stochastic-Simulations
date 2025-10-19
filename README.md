# Stochastic Simulations

A collection of C++ implementations for stochastic simulation algorithms and probability distribution generators, developed as part of coursework in stochastic simulations.

## C++ Implementation

### Core Components

- **`distributions.h/cpp`** - Custom random number generator and probability distribution implementations
  - Multiplicative Congruential Method for pseudorandom number generation
  - Uniform distribution generator with customizable bounds
  - Box-Muller transform for normal distribution generation
  - High-precision floating-point operations for numerical stability

- **`main.cpp`** - Monte Carlo integration example
  - Estimates integrals using importance sampling
  - Implements transformation method for infinite domain integration
  - Demonstrates weighted averaging for convergence

- **`simulationQueue.cpp`** - Queuing system simulation framework (in development)
  - Basic structure for discrete-event simulation
  - Customer arrival and service modeling

### Key Features

- **Custom PRNG**: Implements multiplicative congruential method with configurable parameters
- **Distribution Generation**: Uniform and normal distributions with proper scaling
- **Monte Carlo Methods**: Integration techniques using importance sampling
- **Numerical Precision**: Careful handling of floating-point arithmetic to avoid precision loss

### Build Instructions

```bash
cd cpp_implementation
g++ -o main main.cpp distributions.cpp
./main
```

## Python Implementation

Additional stochastic simulation algorithms implemented in Python, including:
- Poisson process simulation
- Composition and thinning algorithms
- Probability mass function simulations
- Various distribution sampling methods

## Usage

The C++ implementation focuses on core stochastic simulation primitives and can be used as a foundation for more complex simulation studies. The main example demonstrates Monte Carlo integration of the function `g(x) = e^(-x) / (1 + x²)` over the domain [0, ∞).
