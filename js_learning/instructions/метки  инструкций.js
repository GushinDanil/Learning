/**
 * Инструкция break с меткой необходима, только когда требуется прервать выпол
 * нение инструкции, не являющейся ближайшим объемлющим циклом или инст
 * рукцией switch. Следующий фрагмент демонстрирует это:
 */
var matrix = [[1,2,3],[1,1,1],[0,1,0]]
var result = 0
matrix_for: for(var i = 0; i < matrix.length; i++){
    for(var j = 0; j < matrix[i].length; j++){
            if (matrix[i][j]){
                result += matrix[i][j]
                continue matrix_for

            }else {
                break matrix_for
            }
    }
}
/**
 * метка также дочтупна функциям и continue
 */
