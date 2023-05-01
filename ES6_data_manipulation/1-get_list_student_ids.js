export default function getListStudentIds(fn) {
  const list = fn();

  if (!Array.isArray(list)) return [];

  return list.map(({ id }) => id);
}
