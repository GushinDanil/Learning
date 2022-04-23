var empty = {};                          //Объект без свойств
var point = { x:0, y:0 };                // свойства
var point2 = { x:point.x, y:point.y+1 }; // Более сложные значения

var book = {
    "main title": "JavaScript",     //Имена свойств с пробелами
    'sub-title': "The Definitive Guide", // и дефисами, поэтому используются
    'for': "all audiences",              // строковые литералы
                                         // for - зарезервированное слово,
                                            // поэтому в кавычках


    author: {                            // Значением этого свойства является

        firstname: "David",              // объект. Обратите внимание, что имена этих свойств без кавычек.

        surname: "Flanagan"

    },
    tester : new Object()
};
obj = Object.create(book)
console.log(obj.author);
console.log(obj.prototype);



// Оператор in требует, чтобы в левом операнде ему было передано имя свойства
// (в виде строки) и объект в правом операнде. Он возвращает true, если объект име
// ет собственное или унаследованное свойство с этим именем:
var o = { x: 1 }
"x" in o;        // true: o имеет собственное свойство "x"
"y" in o;        // false: o не имеет свойства "y"
"toString" in o; // true: o наследует свойство toString
// Метод hasOwnProperty() объекта проверяет, имеет ли объект собственное свойство
// с указанным именем. Для наследуемых свойств он возвращает false:
var o = { x: 1 }
o.hasOwnProperty("x");        // true: o имеет собственное свойство x
o.hasOwnProperty("y");        // false: не имеет свойства y
o.hasOwnProperty("toString"); // false: toString - наследуемое свойство

// Метод propertyIsEnumerable() накладывает дополнительные ограничения по срав
// нению с hasOwnProperty(). Он возвращает true, только если указанное свойство яв
// ляется собственным свойством, атрибут enumerable которого имеет значение true.
// Свойства встроенных объектов не являются перечислимыми.

var o = { x: 1 }
o.propertyIsEnumerable("x");        // true: o имеет собственное свойство x
o.propertyIsEnumerable("y");        // false: не имеет свойства y
o.propertyIsEnumerable("toString"); // false: toString - наследуемое свойство и не перечисляемое


console.log(Object.prototype.toString())


// В ECMAScript 5 1 значение может замещаться одним или двумя методами,
// известными как методы чтения (getter) и записи (setter). Свойства, для которых
// определяются методы чтения и записи, иногда называют свойствами с метода
// ми доступа, чтобы отличать их от свойств с данными, представляющих простое
// значение.
// Самый простой способ определить свойство с методами доступа заключается
// в использовании расширенного синтаксиса определения литералов объектов:
var k = {
    title: {
        value:0
    },
    x: 1,
    set free(title){
        this.title = title;
    },
    get free(){
        return this.title
    }
}
console.log(k.title);
k.title='helooo'
k.free='titlee'
console.log(k.free);


