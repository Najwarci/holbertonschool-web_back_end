import Building from './5-building.js';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft);
    this._floors = floors;
  }

  // ---- Getter ----
  get floors() {
    return this._floors;
  }

  // ---- Override de la méthode abstraite ----
  evacuationWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors`;
  }
}
