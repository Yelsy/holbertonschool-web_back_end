export default function updateUniqueItems(map) {
  if (!(map instanceof Map)) throw Error('Cannot process');

  map.forEach((key, value) => {
    if (key === 1) map.set(value, 100);
  });
}