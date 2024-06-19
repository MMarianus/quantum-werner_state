from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
import qiskit.quantum_info as qi

def werner_state():
  print("Generating a Werner State from a composite quantum system:")
  qc = QuantumCircuit(5,5)
  
  # Werner state: ρ = λ|Φ-⟩⟨Φ-| + (1-λ)I/4
  #lamb = 0 -> Identity
  #lamb = 1 -> Phi-
  #lamb = 0.5 -> P + I
  lamb = 0.5
  rot = 2 * np.arcsin(np.sqrt(lamb))
  qc.ry(rot, 4)
  qc.cx(4,0)
  qc.ch(4,0)
  qc.ccx(4,0,1)
  qc.cx(4,0)
  qc.ch(4, [2,3], ctrl_state=0)
  qc.ccx(4, 2,0, ctrl_state=0)
  qc.ccx(4, 3,1, ctrl_state=0)
  qc.cx(4,[0,1], ctrl_state=0)

  qc.save_statevector()
  qc.measure_all()

  backend = Aer.get_backend('qasm_simulator')
  transpiled_qc = transpile(qc, backend)
  results = backend.run(transpiled_qc, shots=1000).result()

  state_vector = results.get_statevector()
  print("\n [i]- Initial system preparation:")
  print("System State:")
  display(state_vector.draw('latex'))

  dm = qi.DensityMatrix(state_vector)
  print("\n Density Matrix:")
  display(dm.draw('latex'))

  print("\n Circuit:")
  display(qc.draw(output="mpl"))

  print("\n [i]- Obtaining a Werner State:")
  traced_over_qubits = [2,3,4]
  ws_density_matrix = qi.partial_trace(results.get_statevector(), traced_over_qubits)
  display(ws_density_matrix.draw('latex'))

if __name__ == "__main__":
    werner_state()
