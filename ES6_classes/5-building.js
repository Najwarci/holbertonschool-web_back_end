export default class Building {
    constructor(sqft) {
      this._sqft = sqft;
  
      // Vérifie si la classe fille implémente bien evacuationWarningMessage
      if (this.constructor !== Building && this.evacuationWarningMessage === undefined) {
        throw new Error('Class extending Building must override evacuationWarningMessage');
      }
    }
  
    // ---- Getter ----
    get sqft() {
      return this._sqft;
    }
  }
  