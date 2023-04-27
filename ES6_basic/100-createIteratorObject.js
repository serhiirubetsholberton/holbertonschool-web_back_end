export default function createIteratorObject(report) {
  const names = [];

  Object.values(report).forEach((employees) => names.push(...employees));
  return names;
}
