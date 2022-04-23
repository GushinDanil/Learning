//вы обязаны инициализировать константу при ее объявлении:

const НО = 74;
const С = 299792.458;
const AU = 1.496;

/*
Как следует из названия, значения констант изменяться не может и любая
попытка изменения приводит к генерации ошибки ТуреЕггог.
Общепринятое (но не универсальное) соглашение предусматривает объявление
 констант с использованием имен, содержащих все прописные буквы, напо
добие НО или HTTP_NOT_FOUND , как способ их различения от переменных.
 */

/**
 * В главе 5 речь пойдет об операторах циклов for,for/in и for/of в
 * JavaScript. Каждый из указанных циклов включает переменную цикла, кото
 * рая получает новое значение, присваиваемое ей на каждой итерации цикла.
 * JavaScript позволяет нам объявлять переменную цикла как часть синтаксиса са
 * мого цикла, и это еще один распространенный способ применения let :
 * for(let i=0,len=data.length;i<len;i++) console.log(data[i]);
 * for(let datum of data) console,log(datum);
 * for(let property in object) console.log(property);
 *
 *
 *
 * Область видимости переменной представляет собой часть исходного кода
 * программы, в которой переменная определена. Переменные и константы, объяв
 * ленные с помощью letиconst, имеют блочную область видимости. Другими
 * словами, они определены только внутри блока кода, в котором находятся опе
 * ратор let или const. Определения классов и функций JavaScript являются бло
 * ками, равно как и тела операторов if/else , циклов while , for и т.д. Грубо
 * говоря, если переменная или константа объявляется внутри набора фигурных
 * скобок, то эти фигурные скобки ограничивают область кода, где переменная
 * или константа определена (хотя, конечно же, нельзя ссылаться на перемен
 * ную или константу из строк кода, который выполняется до оператора let или
 * const, объявляющего переменную или константу ЭТО ВАЖНО ). Переменные и константы,
 * объявленные как часть цикла for , for/in или for/of , имеют в качестве об
 * ласти видимости тело цикла, даже если формально они появляются за рамками
 * фигурных скобок.
 *
 * Применение одного и того же имени в более чем одном объявлении let или
 * const внутри той же области видимости является синтаксической ошибкой.
 * Объявлять новую переменную с тем же именем во вложенной области види
 * мости разрешено (но на практике лучше так не поступать)
 *
 * Хотя varиlet имеют одинаковый синтаксис, существуют важные отличия
 * в том, как они работают.
 * • Переменные, объявленные с помощью var, не имеют блочной области ви
 * димости. Взамен область видимости таких переменных распространяется
 * на тело содержащей функции независимо от того, насколько глубоко их
 * объявления вложены внутрь этой функции.
 * • Если вы применяете var вне тела функции, то объявляется глобальная пе
 * ременная. Но глобальные переменные, объявленные посредством var, от
 * личаются от глобальных переменных, объявленных с использованием let ,
 * одним важным аспектом. Глобальные переменные, объявленные с помо
 * щью var, реализуются в виде свойств глобального объекта (см. раздел 3.7).
 * На глобальный объект можно ссылаться как на globalThis . Таким обра
 * зом, если вы записываете var х = 2; за пределами функции, то это подоб
 * но записи globalThis .х = 2 ;. Тем не менее, следует отметить, что анало
 * гия не идеальна: свойства, созданные из глобальных объявлений var, не
 * могут быть удалены посредством операции delete (см. подраздел 4.13.4).
 * Глобальные переменные и константы, объявленные с применением let и
 * const, не являются свойствами глобального объекта.
 * • В отличие от переменных, объявленных с помощью let , с использова
 * нием var вполне законно объявлять ту же самую переменную много раз.
 * И поскольку переменные var имеют область видимости функции, а не
 * блока, фактически общепринято делать повторное объявление такого рода.
 * Переменная i часто применяется для целочисленных значений особенно
 * в качестве индексной переменной циклов for . В функции с множеством
 * циклов for каждый цикл обычно начинается с for (var i = 0; . . . . Из-за
 * того, что var не ограничивает область видимости этих переменных телом
 * цикла, каждый цикл (безопасно) повторно объявляет и заново инициали
 * зирует ту же самую переменную.
 * • Одна из самых необычных особенностей объявлений var известна как
 * подъем (hoisting). Когда переменная объявляется с помощью v ar, объявле
 * ние поднимается к верхушке объемлющей функции. Инициализация пере
 * менной остается там, где вы ее записали, но определение переменной пере
 * мещается к верхушке функции. Следовательно, переменные, объявленные
 * посредством var, можно использовать безо всяких ошибок где угодно в
 * объемлющей функции. Если код инициализации пока еще не выполнен,
 * тогда значением переменной может быть undefined , но вы не получите
 * ошибку в случае работы с переменной до ее инициализации. (Это может
 * стать источником ошибок и одной из нежелательных характеристик, кото
 * рую исправляет let : если вы объявите переменную с применением let ,
 * но попытаетесь ее использовать до выполнения оператора let , то получи
 * те действительную ошибку, а не просто увидите значение undefined .)
 */
'ДЛЯ const И let НЕ РАБОТАЕТ МЕХАНИЗМ ПОДЪЁМА'

const a = 15

function f() {
    console.log(a)
}
f()