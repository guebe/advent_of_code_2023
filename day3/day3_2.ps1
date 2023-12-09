# this is how I got the possible symbols:
# Get-Content input | Foreach-Object {([regex]'[^0-9.]').Matches($_)} | Foreach-object { $_.Value } | Sort-Object | Unique

$row = 0
$numbers = Get-Content input | Foreach-Object { ([regex]'\d+').Matches($_) | Foreach-Object { $_ | Add-Member -NotePropertyName Row -NotePropertyValue $row -PassThru }; $row++ } 
$row = 0
$symbols = Get-Content input | Foreach-Object { ([regex]'[-@*/&#%+=$]').Matches($_) | Foreach-Object { $_ | Add-Member -NotePropertyName Row -NotePropertyValue $row -PassThru }; $row++ } 

# part 1: check if a symbol is inside boundary rows and columns of number
$s = 0
$numbers | Foreach-Object { 
    $rows = ($_.Row - 1)..($_.Row + 1)
    $cols = ($_.Index - 1)..($_.Index + $_.Length)
    foreach ($symbol in $symbols) {
        if ($symbol.Row -in $rows -and $symbol.Index -in $cols) {
            $s += [int] $_.Value
        }
    }
}
$s

# part 2: check connections between gears and sum the product of the connected part numbers
$s = 0
$gears = $symbols | Where-Object Value -eq '*'
foreach ($gear in $gears) {
    $x = $numbers | Where-Object {
        $rows = ($_.Row - 1)..($_.Row + 1)
        $cols = ($_.Index - 1)..($_.Index + $_.Length)
        $gear.Row -in $rows -and $gear.Index -in $cols
        }
    if ($x.Count -eq 2) {
        $s += ([int]$x[0].Value * [int]$x[1].Value)
    }
}
$s
