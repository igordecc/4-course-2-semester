program example3
implicit none
integer :: i,j, x,y
real, allocatable :: common_array(:,:)
!real, allocatable :: auto_form_array(common_array(:,1)) ! for 3.3 task

print *, "---- task 3.1 -----"  !3.1
x=3
y=5
allocate(common_array(x, y))
do i=1,x
    do j=1,y
        common_array(i, j) = i + j
    end do
end do

print *, "where array>5 make it negative"
where(common_array>5) common_array=-common_array
print *, common_array

common_array = abs(common_array)

print *, "complex where"
where (common_array < 5)
    common_array = 0
elsewhere (common_array == 5)
    common_array = common_array**2
elsewhere (common_array >5 .AND. common_array<8)
    common_array = common_array*10
end where
print *, "result: ", common_array 

print *, "---- task 3.2 -----" !3.2

forall (i=1:x:1)
    forall(j=1:y:1)
        common_array(i,j) = common_array(i,j) + 1
    end forall
end forall


print *, "forall(): ", common_array

print *, "--- task 3.3 ---" !3.3

!First, some terminology. Consider the dummy arguments declared as

!real :: a(n)                ! An explicit shape array
!real, allocatable :: c(:)   ! A deferred shape array - перенимает форму
!real :: d(*)                ! An assumed size array - перенимает размер

print *, "auto form array ", size(common_array)
end program example3

