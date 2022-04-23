'use strict'
function f() {  debugger
    var a = 5
    function f1() {
        console.log(a);
        a+=1
    }
    return f1
}
var sparseArray = [1,,,,5];
console.log(sparseArray)
var func = f()
func()
func()
func()
func()
var func2 = f()
func2()
func2()
func2()
func2()
/**
 * как и в пайтоне объекты из объемлюющей области видимости способны сохранять
 * своё состояние для вложенной области видимости
 * хоть и отсутствует явное ключевое слово nonlocal как в пайтоне
*/
