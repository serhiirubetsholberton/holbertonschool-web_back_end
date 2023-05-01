export default function cleanSet(set, startString) {
  let result = '';

  if (typeof startString !== 'string') return result;

  set.forEach((value) => {
    if (value && value.startsWith(startString)) {
      const prefix = result === '' ? '' : '-';
      result += `${prefix}${value.substring(startString.length)}`;
    }
  });

  return result;
}
