export default function cleanSet(set, startString) {
  const filteredSet = [];
  if (!startString || !startString.length) return '';
  for (const value of set) {
    if (value && value.startsWith(startString)) filteredSet.push(value.slice(startString.length));
  }
  return filteredSet.join('-');
}
