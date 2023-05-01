export default function cleanSet(set, startString) {
  let result = '';

  set.forEach((value) => {
    if (value.startsWith(startString)) {
      result += `-${value.substring(startString.length)}`;
    }
  });

  return result;
}
