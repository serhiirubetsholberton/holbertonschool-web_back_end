export const weakMap = new WeakMap();

export function queryAPI(endpoint) {
  const prevCallsCount = weakMap.get(endpoint);

  if (prevCallsCount >= 5) {
    throw new Error('Endpoint load is high');
  }

  const count = prevCallsCount > 0 ? prevCallsCount + 1 : 1;
  weakMap.set(endpoint, count);
}
