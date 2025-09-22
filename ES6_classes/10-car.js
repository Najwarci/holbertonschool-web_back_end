// Création d'un symbole pour la méthode interne de clonage
const _clone = Symbol('cloneCar');

export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  // ---- Méthode interne privée ----
  [_clone]() {
    return new this.constructor();
  }

  // ---- Méthode publique ----
  cloneCar() {
    return this[_clone]();
  }
}
