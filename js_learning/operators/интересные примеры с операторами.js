i = j = k = 0; // Инициализировать 3 переменные значением 0


/**
 * оператор ! всегда возвращает true или false что всегда мож
 * но преобразовать любое значение x в его логический эквивалент, дважды приме
 * нив этот оператор: !!x (раздел 3.8.2). это равносильно new Boolean(x)
 * (a = b) == 0 есть и такая гибкость
 */
var max_width = false
var preferences = {max_width:''}
var max = max_width || preferences.max_width || 500;
console.log(max)

/**
 * тернарный оператор
 */
b = ''
var a = b == true ? b : 'b is not true'
console.log(a)

/**
 * аналогичная запись
 */
if (b)
    a=b
else
    a='b is not true'
console.log(a)
var value = true && true ? 500 : 250
console.log(value)