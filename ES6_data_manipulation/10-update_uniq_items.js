export default function updateUniqueItems(map) {
  if (!(map instanceof Map)) {
    throw new Error('Cannot process');
  }

  for (const entrie of map.entries()) {
    if (entrie[1] === 1) {
      entrie[1] = 100;
    }
  }
}
