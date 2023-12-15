$total = 0
foreach ($line in Get-Content "input") {
    $line = $line -replace "[a-z]"
    $total += [int]($line[0] + $line[-1])
}
$total
