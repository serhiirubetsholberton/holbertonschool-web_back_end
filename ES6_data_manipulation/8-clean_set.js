export default function cleanSet(set, startString) {
  let result = '';

  set.forEach((value) => {
    console.log(value)
    if (value && value.startsWith(startString)) {
      const prefix = result === '' ? '' : '-';
      result += `${prefix}${value.substring(startString.length)}`;
    }
  });

  return result;
}
