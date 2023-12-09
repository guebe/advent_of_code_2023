[array]$FILE = Get-Content input
$inputs = $FILE[0].Trim().toCharArray()

$maps = @{}
foreach ($line in $FILE[2..($FILE.Count-1)]) {
    $a, $b, $c = $line -replace '[=(),]' -replace '  ', ' ' -split ' '
    $maps.$a = $b, $c
}

$i = 0
$key = 'AAA'
while ($True) {
    foreach ($n in $inputs) {
        $key = $maps.$key[($n -eq 'L') ? 0 : 1]
        $i++
        if ($key -eq 'ZZZ') {
            $i
            exit
        }
    }
}
