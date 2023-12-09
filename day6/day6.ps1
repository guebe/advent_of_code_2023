[array]$file = Get-Content input
$times = $file[0].Split(":")[1].Split(" ",[System.StringSplitOptions]::RemoveEmptyEntries)
$distances = $file[1].Split(":")[1].Split(" ", [System.StringSplitOptions]::RemoveEmptyEntries)
$p = 1
for ($i = 0; $i -lt $times.Count; $i++) {
    [uint64]$t = $times[$i]
    [uint64]$d = $distances[$i]
    $ways = 0
    for ($j = 1; $j -lt $t; $j++) {
        if ((($t - $j) * $j) -gt $d) {
            $ways++
        }
    }
    $p *= $ways
}
$p
