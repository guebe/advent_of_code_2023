$m = @{}; $i = 0; $key = 'AAA'
[array]$F = Get-Content input
$d = $F[0].Trim().toCharArray()
$F[2..($F.Count-1)] |% { $a,$b,$c = $_ -replace '[=(),]' -replace '  ', ' ' -split ' '; $m.$a=$b,$c }
while ($key -ne 'ZZZ') { $key = $m.$key[($d[$i++%$d.Count] -eq 'L')?0:1] }
$i
