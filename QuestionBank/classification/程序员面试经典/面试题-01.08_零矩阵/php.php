class Solution {

    /**
     * @param Integer[][] $matrix
     * @return NULL
     */
    function rotate(&$matrix) {
        $cnt = count($matrix);
        for ($i = 0; $i < $cnt/2; $i++) {
            for ($j = 0; $j < $cnt; $j++) {
                $tmp = $matrix[$i][$j];
                $matrix[$i][$j] = $matrix[$cnt-$i-1][$j];
                $matrix[$cnt-$i-1][$j] = $tmp;
            }
        }
        for ($i = 0; $i < $cnt; $i++) {
            for ($j = $i; $j < $cnt; $j++) {
                $tmp = $matrix[$i][$j];
                $matrix[$i][$j] = $matrix[$j][$i];
                $matrix[$j][$i] = $tmp;
            }
        }
    }
}