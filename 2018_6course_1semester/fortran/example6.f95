program example6
integer(8)::i,j, array_size
real(8), allocatable:: a(:,:)
real(8), allocatable:: free_array(:)
character(20):: nick
print *, "----- 6.1 -----"
allocate(a(5,4))
a = 100.123456
print '(f8.3)', a
!write(1,’1x,f8.3,i10’)
j = 3145647
print '(i5)', j
print '(i10)', j

print *, "----- 6.2 ------"

open(1, file='example2.dat')
write(1, '(i10)') (/(i, i=1, 10, 1)/)


print*, "writing in file done..."

print *, "open file"

rewind(1)
!inquire(iolength=array_size) a,s

array_size = 5

rewind(1)
inquire(1,name=nick)
print *, nick
allocate(free_array(array_size))
read(1, *) free_array
print *, free_array
deallocate(free_array)


close(1)

end program example6