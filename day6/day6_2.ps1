[array]$file = Get-Content input
[uint64]$time = $file[0].Split(":")[1] -join "" -replace " ", ""
[uint64]$distance = $file[1].Split(":")[1] -join "" -replace " ", ""

$ways = 0
for ($j = 1; $j -lt $time; $j++) {
    if ((($time - $j) * $j) -gt $distance) {
        $ways++
    }
}
$ways
