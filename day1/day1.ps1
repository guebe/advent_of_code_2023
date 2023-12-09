[array] $file = Get-Content input

# adds first and last digit in each line
$s = 0
foreach ($line in $file) {
    $x = $line -replace "[^0-9]", ''
    $s += [int]($x[0] + $x[-1])
}
$s

$s = 0
# converts strings to numbers
# also works for strings like twone => two2twone1one
# adds first and last digit in each line
foreach ($line in $file) {
    $x = $line -replace "one", 'one1one' -replace "two", 'two2two' -replace "three", 'three3three' -replace "four", 'four4four' -replace "five", 'five5five' -replace "six", 'six6six' -replace "seven", 'seven7seven' -replace "eight", 'eight8eight' -replace "nine", 'nine9nine' -replace "[^0-9]", ''
    $s += [int]($x[0] + $x[-1])
}
$s

