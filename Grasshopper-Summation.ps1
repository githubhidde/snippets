# codewars challenge, check out the URL:
# https://www.codewars.com/kata/55d24f55d7dd296eb9000030/train/powershell
function Summation([int] $n) {
  $array = 1..$n
  $thrash_bin = 0
  $array | foreach {$thrash_bin += $_}
  $thrash_bin
}

Summation(8)
# Describe 'Summation' {
#   Context 'Basic tests' {
#     It 'Summation <n> is <r>' -TestCases @(
#       @{ n = 1; r = 1 }
#       @{ n = 8; r = 36 }
#       @{ n = 22; r = 253 }
#       @{ n = 100; r = 5050 }
#       @{ n = 213; r = 22791 }
#     ) {
#       param ($n, $r)
#       Summation $n | Should Be $r
#     }
#   }
# }