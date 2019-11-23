module overloadfunc
    implicit none

    interface check
    module procedure check_int, check_real
    end interface

    contains 

    subroutine check_int(cur)
    integer, intent(in) :: cur
    print '(i10)', cur
    end subroutine

    subroutine check_real(cur)
    real, intent(in) :: cur
    print '(f10.5)', cur
    end subroutine
end module overloadfunc

program example5
use overloadfunc
integer(8)::i,j
real(8)::variable
integer(8), allocatable :: a(:,:)

print *, "------- 5,1 ------"

variable=-2.300000000000000
i=5
ca2=i*variable

print *, variable
print *, "int() ",int(variable)
print *, "real()", real(int(variable))
print *, "cmplx()", cmplx(variable, variable+1)
print *, "convert one type to another implicitly - is bad"

allocate(a(2,5))
do j=1,size(a(:,1))
do i=1,size(a(1,:))
a(i,j)=i/(10*j)
end do
end do
print *, "a with impicite cast real to int will be zerro ", a
print *, "---------5.2--------"
call check_int(10)
call check_real(10.84564)
print * 
end program example5