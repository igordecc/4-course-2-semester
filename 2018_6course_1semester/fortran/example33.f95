program example33
real :: x(6)
x = (/1,2,3,4,5,6/)
call reshape(x, 3)
end program example33

subroutine reshape(array, d)
real, intent(in) :: array (2,*)
integer, intent(in) :: d
print *, array(:,:d)
end subroutine reshape