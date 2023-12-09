[array] $file = Get-Content input

# 1. checks if game is valid if color blocks are less then $max[COLOR]
# 2. determines minimal color blocks needed to make the game valid
$s1 = 0 # sum of valid game ids
$s2 = 0 # sum of product of minimal block power
$max = @{ red = 12; green = 13; blue = 14 }
for ($i = 0; $i -lt $file.Count; $i++) {
    $valid = $True
    $min = @{ red = 0; green = 0; blue = 0 }
    foreach ($x in $file[$i].Split(":")[1].Replace(",",";").Split(";")) {
        $x = $x.Split(" ",[System.StringSplitOptions]::RemoveEmptyEntries)
        $n = [int]$x[0]
        $color = $x[1]
        if ($n -gt $max[$color]) { $valid = $False }
        if ($n -gt $min[$color]) { $min[$color] = $n }
    }
    if ($valid) {
        $s1 += ($i + 1)
    }
    $s2 += ($min.red * $min.green * $min.blue)
}
"$s1 $s2"
