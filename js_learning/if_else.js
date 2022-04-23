if (1==1)
    console.log('hello')
else if (1==0)
    console.log('good night')
else
    console.log('good midnight')


// надо использовать фигурные скобки если ифы вложены друг в друга как в примере ниже иначе
// else примерит на себя вложенный иф а не объемлюющий
i = j = 1;
k = 3;
if (i == j) {
    if (j == k) {
        console.log("i равно k");
    }    
}
else{
    console.log("i не равно j"); // НЕПРАВИЛЬНО!!
}

// тут сработает не так как хотелось бы поэтому скобки обязательно
i = j = 1;
k = 3;
if (i == j)
    if (j == k)
        console.log("i равно k");

else
    console.log("i не равно j"); // НЕПРАВИЛЬНО!!
