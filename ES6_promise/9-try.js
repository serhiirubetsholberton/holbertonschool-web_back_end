export default function guardrail(mathFunction) {
  let candidate = 0;
  try {
    candidate = mathFunction();
  } catch (err) {
    candidate = err.toString();
  }

  return [candidate, 'Guardrail was processed'];
}
