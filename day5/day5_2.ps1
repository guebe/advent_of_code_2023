$inputs, $blocks = Get-Content input | Out-String | Foreach-Object { $_ -split "`n`n" }

$inputs = $inputs.Split(': ')[1].Split(' ')

[System.Collections.Generic.List[System.Object]]$seeds = for ($i = 0; $i -lt $inputs.Count; $i += 2) {
    [PSCustomObject]@{
    s = [uint64]$inputs[$i]
    e = [uint64]$inputs[$i] + [uint64]$inputs[$i+1]
    }
}

foreach ($block in $blocks) {
    $ranges = $block.Split(":")[1].Split("`n",[System.StringSplitOptions]::RemoveEmptyEntries) | ForEach-Object { $x = $_.Split(' ')
        [PSCustomObject]@{
        a = [uint64]$x[0]
        b = [uint64]$x[1]
        c = [uint64]$x[2]
        }
    }
    [System.Collections.Generic.List[System.Object]]$new = New-Object System.Collections.Generic.List[System.Object]

    while ($seeds.Count -gt 0) {
        $seed = $seeds[0]
        $seeds.RemoveAt(0)
        $default = $True

        foreach ($range in $ranges) {
            $os = [Math]::Max($seed.s, $range.b)
            $oe = [Math]::Min($seed.e, $range.b + $range.c)

            if ($os -lt $oe) {
                $new.Add([PSCustomObject]@{
                    s = $os - $range.b + $range.a
                    e = $oe - $range.b + $range.a})
                if ($os -gt $seed.s) {
                    $seeds.Add([PSCustomObject]@{
                        s = $seed.s; e = $os})
                }
                if ($seed.e -gt $oe) {
                    $seeds.Add([PSCustomObject]@{
                        s = $oe; e = $seed.e})
                }
                $default = $False
                break
            }
        }

        if ($default) {
            $new.Add([PSCustomObject]@{
                s = $seed.s; e = $seed.e})
        }
    }

    $seeds = $new
}
$seeds | Sort-Object { $_.s } | Select-Object -First 1 | Select -ExpandProperty "s"
