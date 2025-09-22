# 📘 Résumé : Les classes en ES6

## 🔹 1. Qu'est-ce qu'une classe ?

-   Introduites avec **ES6**, les classes offrent une syntaxe moderne et
    plus lisible pour créer des objets.
-   Elles simplifient la gestion du **prototypage** et de
    l'**héritage**.

------------------------------------------------------------------------

## 🔹 2. Définir une classe

``` js
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  sayHello() {
    return `Bonjour, je m'appelle ${this.name} et j'ai ${this.age} ans.`;
  }
}

const p1 = new Person("Alice", 25);
console.log(p1.sayHello());
```

------------------------------------------------------------------------

## 🔹 3. Héritage avec `extends`

``` js
class Student extends Person {
  constructor(name, age, subject) {
    super(name, age); // appelle le constructeur parent
    this.subject = subject;
  }

  study() {
    return `${this.name} étudie ${this.subject}.`;
  }
}

const s1 = new Student("Bob", 20, "Maths");
console.log(s1.sayHello()); // hérité
console.log(s1.study());    // spécifique
```

------------------------------------------------------------------------

## 🔹 4. Méthodes statiques

``` js
class MathUtils {
  static add(a, b) {
    return a + b;
  }
}

console.log(MathUtils.add(2, 3)); // 5
```

➡️ Les méthodes statiques appartiennent à la **classe** et non aux
instances.

------------------------------------------------------------------------

## 🔹 5. Getters et Setters

``` js
class Rectangle {
  constructor(width, height) {
    this.width = width;
    this.height = height;
  }

  get area() {
    return this.width * this.height;
  }

  set width(value) {
    if (value > 0) this._width = value;
  }

  get width() {
    return this._width;
  }
}

const r = new Rectangle(4, 5);
console.log(r.area); // 20
```

------------------------------------------------------------------------

# ✅ À retenir

-   `class` = syntaxe moderne pour objets/prototypes.
-   `constructor` = initialise les instances.
-   `extends` + `super()` = héritage.
-   `static` = méthodes liées à la classe.
-   `get/set` = accès contrôlé aux propriétés.
