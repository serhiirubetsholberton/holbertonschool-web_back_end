export default function createIteratorObject(report) {
  const names = [];

  Object.values(report.allEmployees).forEach((employees) => names.push(...employees));
  return names;
}
