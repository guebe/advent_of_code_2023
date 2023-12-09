[array] $file = Get-Content input

$s1 = 0 # counts winning numbers
$s2 = 0 # counts winning cards
$cards = @(1) * $file.Count # contains card counts including copies

for ($index = 0; $index -lt $file.Count; $index++) {
    $line = $file[$index].Split(":")[1].Split("|")
    $a = $line[0].Split(" ",[System.StringSplitOptions]::RemoveEmptyEntries)
    $b = $line[1].Split(" ",[System.StringSplitOptions]::RemoveEmptyEntries)

    $n = 0
    foreach ($x in $a) {
        if ($b -contains $x) {
            $n++
        }
    }

    if ($n -gt 0) {
        $s1 += [Math]::Pow(2, $n - 1)
    }

    for ($i = 0; $i -lt $n; $i++) {
        $x = $index + $i + 1
        if ($x -lt $cards.Count) {
            $cards[$x] += $cards[$index]
        }
    }

    $s2 += $cards[$index]
}

"$s1 $s2"
