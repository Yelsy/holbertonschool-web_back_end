export default function cleanSet(set, startString) {
  let result = '';
  for (const value of set) {
    if (value.startsWith(startString)) {
      const suffix = value.substring(startString.length);
      if (result.length > 0) {
        result += '-';
      }
        result += suffix;
    }
  }
    
  return result;
}
