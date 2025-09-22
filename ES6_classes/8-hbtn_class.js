export default class HolbertonClass {
    constructor(size, location) {
      this._size = size;
      this._location = location;
    }
  
    // ---- Getters ----
    get size() {
      return this._size;
    }
  
    get location() {
      return this._location;
    }
  
    // ---- Conversion en primitif ----
    [Symbol.toPrimitive](hint) {
      if (hint === 'number') {
        return this._size;
      }
      if (hint === 'string') {
        return this._location;
      }
      return this._size;
    }
  }
  