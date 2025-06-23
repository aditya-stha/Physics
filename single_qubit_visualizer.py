
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_vector
import numpy as np
import matplotlib.pyplot as plt



def state_to_bloch_vec(state):
    ψ = state.data
    x = 2 * np.real(np.conj(ψ[0]) * ψ[1])
    y = 2 * np.imag(np.conj(ψ[0]) * ψ[1])
    z = abs(ψ[0])**2 - abs(ψ[1])**2
    return [x, y, z]

# Format ket notation string
def format_ket(state):
    a, b = state.data
    def fmt(c):
        re = f"{c.real:.3f}"
        im = f"{c.imag:+.3f}i"
        return re + im
    return f"|ψ⟩ = ({fmt(a)})|0⟩ + ({fmt(b)})|1⟩"

# Maping user input to Qiskit gates
def apply_gate(qc, gate, angle=None):
    if gate == "x":
        qc.x(0)
    elif gate == "y":
        qc.y(0)
    elif gate == "z":
        qc.z(0)
    elif gate == "h":
        qc.h(0)
    elif gate == "s":
        qc.s(0)
    elif gate == "t":
        qc.t(0)
    elif gate == "rx":
        if angle is None:
            print("RX gate requires an angle (radians)")
        else:
            qc.rx(angle, 0)
    elif gate == "ry":
        if angle is None:
            print("RY gate requires an angle (radians)")
        else:
            qc.ry(angle, 0)
    elif gate == "rz":
        if angle is None:
            print("RZ gate requires an angle (radians)")
        else:
            qc.rz(angle, 0)
    else:
        print(f"Unknown gate: {gate}")

def main():
    qc = QuantumCircuit(1)

    state = Statevector.from_instruction(qc)
    print("Initial state:")
    print(format_ket(state))
    bloch_vec = state_to_bloch_vec(state)
    plot_bloch_vector(bloch_vec, title="Initial Bloch Sphere")
    print("Close the Bloch sphere window to continue.")
    plt.show()

    print("Single Qubit Interactive Gate Application")
    print("Available gates: x, y, z, h, s, t, rx, ry, rz")
    print("Type 'N' to finish applying gates.")

    while True:
        cmd = input("Enter gate: ").strip().lower()
        if cmd == "done":
            break

        parts = cmd.split()
        gate = parts[0]
        angle = None

        if gate in ["rx", "ry", "rz"]:
            if len(parts) != 2:
                print(f"Gate {gate} requires an angle in radians, e.g. '{gate} 3.14'")
                continue
            try:
                angle = float(parts[1])
            except ValueError:
                print("Invalid angle. Please enter a number in radians.")
                continue

        apply_gate(qc, gate, angle)

        # Get the updated statevector
        state = Statevector.from_instruction(qc)

        # Print ket notation
        print(format_ket(state))

        # Plot Bloch sphere
        bloch_vec = state_to_bloch_vec(state)
        plot_bloch_vector(bloch_vec, title="Bloch Sphere")
        print(" Close the Bloch sphere window to continue.")
        plt.show()
        

if __name__ == "__main__":
    main()
