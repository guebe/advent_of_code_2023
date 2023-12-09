$file = Get-Content input | Out-String  
$contents = ([regex]'\n\n').Split($file)
$seeds = $contents[0].Split(': ')[1].Split(' ')

foreach ($mapping in $contents[1..($contents.Count)]) {
    $dataset = $mapping.Split(":")
    $mapname = $dataset[0]

    $new = @(0) * $seeds.Count
    $i = 0
    [uint64]$seed = 0;
    foreach ($seed in $seeds) {
        [uint64]$dst = $seed
        foreach ($data in ([regex]'\n').Split($dataset[1])) {
            $d = $data.Split(' ')
            if ($d.Count -eq 3) {
                [uint64]$dst_start = $d[0]
                [uint64]$src_start = $d[1]
                [uint64]$len = $d[2]
                if (($seed -ge $src_start) -and ($seed -lt ($src_start+$len))) {
                    $dst = $seed + $dst_start - $src_start
                    break
                }
            }
        }
        $new[$i++] = $dst
    }
    $seeds = $new
}
$new | Sort-Object | Select-Object -First 1
