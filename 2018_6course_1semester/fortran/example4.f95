program example4
integer :: i, go_to_index
real(8), allocatable :: a(:)
integer(8), allocatable :: integer_array(:)


print *, "----- 4,1 -----"  !------ 4,1
a = (/(mod(i,2),i=1,5, 1)/) 
print *, a

do i=1,10
if (a(i)>0) then
a(i)=a(i)+1
else if (a(i)==0) then
a(i)=a(i)-1
else
a(i)=-9999
end if
end do

print *, "IF statement: ", a

integer_array = (/(int(mod(i,2)),i=1,5, 1)/) 
do i=1,size(integer_array),1
select case(integer_array(i))
case(1:)
integer_array(i) = +1
case(:-1)
integer_array(i) = -1
case default
integer_array(i) = 0
end select
end do


print *, "SELECT CASE: ", integer_array


print *, "----- 4.2 -----"


go_to_index = 0

10 continue
print *, go_to_index
go_to_index = go_to_index + 1

if (go_to_index < 5) then 
go to 10
else 
print *, go_to_index, " <- end GO TO"
end if

print *, "exit cycle at 5"
do i = 1, 20, 1
print *, i
if (i<5) then 
cycle
else
print *, " bye !"
exit
end if
print *, "this will no be printed FOREVER"
end do

end program example4