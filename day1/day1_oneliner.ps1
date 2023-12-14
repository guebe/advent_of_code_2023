$res = 0; foreach ($line in Get-Content "input") { $line = $line -replace "[a-z]", "" ; $res += $line[0] + $line[-1]; } $res
