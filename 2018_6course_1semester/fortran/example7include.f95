program example7include
implicit none
real print_factorial
real :: n
if (n>0) then
    print(n)
    n = n - 1
    include 'example7include.f95'
else
    print(n)
end if
end program example7include

!recursive subprogram print_factorial(n)
!implicit none
!real :: n
!if (n>0) then
!    n = n - 1
!    include 'example7include.f95'
!end if
!
!end subprogram print_factorial