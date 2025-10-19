# Stochastic Simulations

A collection of C++ implementations for stochastic simulation algorithms and probability distribution generators, developed as part of coursework in stochastic simulations.

## C++ Implementation

**Goal**: Expand C++ programming skills while learning stochastic variable and event simulation techniques, with emphasis on code readability, computational efficiency, and numerical accuracy.

**Development Process**: All code is hand-written from scratch using VIM - no AI-generated code or automated assistance used in the implementation.

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

- **Readable Code Design**: Clean class structure with well-documented methods and clear variable naming
- **Efficient Algorithms**: Optimized multiplicative congruential method with minimal computational overhead
- **Accurate Numerical Methods**: 
  - Explicit type casting to prevent silent conversions
  - Guard conditions against edge cases (e.g., zero values in log operations)
  - High-precision floating-point operations for numerical stability
- **Modular Architecture**: Separated concerns between random number generation and distribution sampling
- **Robust Implementation**: Error-resistant design with proper bounds checking and overflow prevention

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
