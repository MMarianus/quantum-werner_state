# ⚛️ Werner State & Entanglement 

![Type](https://img.shields.io/badge/Type-Quantum-red)  ![Code](https://img.shields.io/badge/Code-Python-blue)  [![Code](https://img.shields.io/badge/License-GPL%20v3-yellow)](https://github.com/MMarianus/quantum-werner_state/blob/main/LICENSE)

## Overview

This repository contains code to create a quantum system with 5 qubits, entangle them, and perform a partial trace to obtain a subsystem. The resultant subsystem is a configurable Werner State, which is useful for studying quantum entanglement properties.

## What is a Werner State?

A Werner state is a specific type of mixed quantum state that represents a mixture of a maximally entangled state and a maximally mixed state. It can be expressed as:

![equation](https://latex.codecogs.com/svg.image?\mathbf{\color{Gray}\rho=\lambda|\Phi^&plus;\rangle\langle\Phi^&plus;|&plus;(1-\lambda)\frac{I}{4}})

λ is a configurable parameter that determines the level of mixture. A two-qubit Werner state is separable for λ ≤ ⅓ and entangled for λ > ⅓.

Werner states are significant for studying quantum entanglement and decoherence, making them valuable in quantum information theory.

### Initial Circuit Preparation:
The following image illustrates the initial quantum system prepared to obtain the desired Werner State:
<img width="400" alt="image" src="https://github.com/MMarianus/quantum-werner_state/assets/25618241/90f1ac5b-a54d-4bb1-ac43-0963abfa9a37">



## Why This Project?

This code was implemented as part of a quantum engineering master degree to demonstrate:
- The creation of entangled states, which are fundamental in quantum computing and quantum information.
- How to perform a partial trace, a key operation in quantum mechanics to study subsystems.
- A practical example of generating Werner states from a quantum composite system, which can be used to explore various properties of quantum entanglement with more depth.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.7+
- Qiskit

You can install Qiskit using pip:

```bash
pip install qiskit
```



