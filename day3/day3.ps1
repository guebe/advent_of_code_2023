# draw a border of dots around the schematic to ease checking later-on
$schematic = @(' ') * 142
$i = 0
$schematic[$i++] = '.' * 142
foreach ($line in Get-Content input) {
    $schematic[$i++] = '.' + $line + "."
}
$schematic[$i++] = '.' * 142

$s = 0
# checks if a symbol not equals '.' is on previous or next line
# or left or right of part number
for ($i = 1; ($i -lt $schematic.Count - 1); $i++) {
    $prev_line = $schematic[$i-1] 
    $this_line = $schematic[$i] 
    $next_line = $schematic[$i+1] 

    foreach ($n in ([regex]'\d+').Matches($this_line)) {
        $first = $n.Index - 1
        $last = $n.Index + $n.Length

        if (($this_line[$first] -ne '.') -or
            ($this_line[$last] -ne '.') -or
            ($prev_line[$first..$last] -match '[^.]') -or
            ($next_line[$first..$last] -match '[^.]')) {
            $s += [int] $n.Value
        }
    }
}
$s

