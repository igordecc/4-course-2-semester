program example5
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

end program example5