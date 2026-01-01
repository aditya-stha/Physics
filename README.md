# Physics
repository for my Physics projects


single_qubit_visualizer:

Hi to the veiwer,
This is a command-line quantum visualization tool built with Python and Qiskit. It lets you apply quantum gates to a single qubit and see:

- The updated quantum state in Dirac (ket) notation
- A 3D Bloch sphere representation of the qubit

---

Features

Interactive terminal interface  
Supports key gates: `X`, `Y`, `Z`, `H`, `S`, `T`, `RX`, `RY`, `RZ` (with angles)  
Live **Bloch sphere visualization** after every gate  
Shows the full **quantum statevector** in complex notation  
Uses the library `qiskit.quantum_info.Statevector` for full fidelity simulation  

---

How It Works

1. You start with a qubit in the `|0>` state. ( every time i initialized it to start with |0> )
2. It shows a visualiztion in a window of the initial state ( you can close it to proceed on )
3. You apply gates one by one (e.g., `h`, `rz 3.14`, `x`, etc.).
4. After each gate:
   - The state is updated
   - The new ket form is printed
   - The qubit vector is plotted on the Bloch sphere
   - A new window pops up with the new updated Bloch Sphere

---


Installation

Requirements

- Python 3.8+
- [Qiskit](https://qiskit.org/)
- `matplotlib`
- `numpy`

Install dependencies:

bash
pip install qiskit matplotlib numpy
