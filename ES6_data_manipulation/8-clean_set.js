export default function cleanSet(set, startString) {
  const filteredSet = new Set([...set].filter((value) => value.startsWith(startString)));
  const resultString = filteredSet.join('-');
  return resultString;
}
