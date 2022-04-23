/**
 * Унарный оператор delete выполняет попытку удалить свойство объекта или эле
 * мент массива, определяемый операндом. 1 Подобно операторам присваивания, ин
 * кремента и декремента, оператор delete обычно используется ради побочного эф
 * фекта, выражающегося в удалении свойства, а не ради возвращаемого значения.
 * Ниже приводятся несколько примеров его использования:
 * var o = {x: 1, y: 2}; // Определить объект
 * delete o.x;           // Удалить одно из его свойств
 * "x" in o              // => false: свойство больше не существует
 * var a = [1,2,3];      // Создать массив
 * delete a[2];          // Удалить последний элемент массива
 * 2 in a               // => false: второй элемент больше не существует
 * a.length             // => 3: обратите внимание, что длина массива при этом не изменилась
 * Внимание: удаленное свойство или элемент массива не просто получает значение
 * undefined. После удаления свойства оно прекращает свое существование. Попыт
 * ка прочитать значение несуществующего свойства возвратит значение undefined,
 * но вы можете проверить фактическое наличие свойства с помощью оператора in
 * (раздел 4.9.3). Операция удаления элемента массива оставляет в массиве «дырку»
 * и не изменяет длину массива. В результате получается разреженный массив.
 * Оператор delete требует, чтобы его операнд был левосторонним выражением. Ес
 * ли операнд не является левосторонним выражением, оператор не будет выпол
 * нять никаких действий и вернет значение true. В противном случае delete попы
 * тается удалить указанное левостороннее выражение. В случае успешного удале
 * ния значения левостороннего выражения оператор delete вернет значение true.
 * Не все свойства могут быть удалены: некоторые встроенные свойства из базового
 * и клиентского языков JavaScript устойчивы к операции удаления. Точно так же
 * не могут быть удалены пользовательские переменные, объявленные с помощью
 * инструкции var. Кроме того, невозможно удалить функции, объявленные с помо
 * щью инструкции function, а также объявленные параметры функций.
 * В строгом режиме, определяемом стандартом ECMAScript 5, оператор delete воз
 * буждает исключение SyntaxError, если его операндом является неквалифициро
 * ванный идентификатор, такой как имя переменной, функции или параметра
 * функции: он может оперировать только операндами, которые являются выраже
 * ниями обращения к свойству (раздел 4.4). Кроме того, строгий режим определя
 * ет, что оператор delete должен возбуждать исключение TypeError, если запрошено
 * удаление ненастраиваемого свойства (раздел 6.7). В обычном режиме в таких слу
 * чаях исключение не возбуждается, и оператор delete просто возвращает false,
 * чтобы показать, что операнд не был удален.
 * Ниже приводится несколько примеров использования оператора delete:
 * var o = {x:1, y:2}; //
 * delete o.x;         //
 * typeof o.x;         //
 * delete o.x;         //
 * delete o;           //
 *                     //
 * delete 1;           //
 * this.x = 1;         //
 * delete x;           //
 *                     //
 * x;                  //
 * С оператором delete мы снова встретимся в разделе 6.3.
 */
var o = {x: 1, y: 2}; // Определить объект
delete o.x;           // Удалить одно из его свойств
"x" in o              // => false: свойство больше не существует
var a = [1,2,3];      // Создать массив
delete a[2];          // Удалить последний элемент массива
2 in a               // => false: второй элемент больше не существует
a.length             // => 3: обратите внимание, что длина массива при этом не изменилась






var o = {x:1, y:2}; // Определить переменную; инициализировать ее объектом
delete o.x;         // Удалить одно из свойств объекта; вернет true
typeof o.x;         // Свойство не существует; вернет "undefined"
delete o.x;         // Удалить несуществующее свойство; вернет true
delete o;           // Объявленную переменную удалить нельзя; вернет false
                    // В строгом режиме возбудит исключение.
delete 1;           // Аргумент не является левосторонним выражением; вернет true
this.x = 1;         // Определить свойство глобального объекта без var
delete x;           // Удалить: вернет true при выполнении в нестрогом режиме; в строгом
                    // режиме возбудит исключение. Используйте 'delete this.x' взамен.
x;                  //