export default function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(2);
  return new DataView(buffer).setInt8(position, value);
}
