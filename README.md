# Lyapunov Diagram Generator

The Lyapunov-diagram-generator is a tool to be used to further study the stability of a dynamical system through the concept of Lyapunov exponents. This README will provide a brief overview of what Lyapunov exponents are, and how the code works and can be used.

## Table of Contents

- [Lyapunov Exponents](#lyapunov-exponents)
- [Lyapunov Diagram Generator](#lyapunov-diagram-generator)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Parameters](#parameters)
- [Examples](#examples)
- [References](#references)

## Lyapunov Exponents
The Lyapunov exponents are a quantity of a dynamical system that characterizes the rate of separation of infinitesimally close trajectories. If a dynamical system consists of only negative Lyapunov exponents, the system is stable. If it contains negative and zero Lyapunov exponents, it’s considered periodic. Finally, if it contains all the previously mentioned as well as positive exponents, the system is considered chaotic. 

If two trajectories in phase space are seperated with an initial vector $\delta \boldsymbol{\mathrm{Z_0}}$, their trajectories divergence at a rate given by

$$
|\delta \boldsymbol{\mathrm{Z}}(t)| \sim e^{\lambda t}|\delta \boldsymbol{\mathrm{Z_0}}|
$$

where $\lambda$ is the Lyapunov exponent. The lambdas vary with variations in orientation of the initial seperation vector which introduces a spectrum of Lyapunov exponents (with dimension equal to the dimensionality of the phase space). The Lyapunov exponents can be calculated using the following formula [1]

$$
\lambda = \lim_{n\rightarrow \infty} \frac{1}{n} \sum_{i=0}^{n-1} \ln | f'(x_i) |. 
$$

## Lyapunov Diagram Generator

The Lyapunov Diagram Generator is a Python-based tool that allows you to visualize the behavior of a dynamic system by generating Lyapunov diagrams. These diagrams are two-dimensional plots where each point $(r_1, r_2)$ constitutes the values used within the user defined recurrence-relation. The corresponding output on this two-dimensional grid is the Lyapunov exponent of the dynamical system. 

### Installation 

1. Clone this repository to your local machine.
2. Navigate to the project directory.

```
git clone https://github.com/yourusername/lyapunov-diagram-generator.git
cd lyapunov-diagram-generator
```


### Parameters

- `N` - number of iterations of the recurrence relation
- `resol` - resolution of the grid along one axis
- `seq` - user defined sequence for how the recurrence relation should alternate between the $r_i$'s
- `x0` - the initial value for the recurrence relation

Modify these parameters in the script to explore different system behaviours. 

## Examples

Here are some examples using the logistic recurrence relation $x_{n+1} = r \cdot x_n \cdot (1-x_n)$ for some different sequences and resolutions. The parameters can be found in the title of each diagram. Notice the cool fractals that are formed!

<p align = "center">
  <img src = "https://github.com/Thidius/Lyapunov-diagram-generator/assets/121384892/0081dd20-9699-46d0-a959-27a690e0e533" alt = "Fig1" width = "300">
  <img src = "https://github.com/Thidius/Lyapunov-diagram-generator/assets/121384892/97f60f46-bd4f-4c64-b4f8-788840449209" alt = "Fig1" width = "300">
  <img src = "https://github.com/Thidius/Lyapunov-diagram-generator/assets/121384892/6096fd59-04f7-45a1-9260-7d5bd6caaee0" alt = "Fig1" width = "300">
</p>

## References

[1] Libretexts (2022) 9.3: Lyapunov exponent, Mathematics LibreTexts. Available at: https://math.libretexts.org/Bookshelves/Scientific_Computing_Simulations_and_Modeling/Book%3A_Introduction_to_the_Modeling_and_Analysis_of_Complex_Systems_(Sayama)/09%3A_Chaos/9.03%3A_Lyapunov_Exponent (Accessed: 08 August 2023). 




