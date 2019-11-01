program example2
    implicit none
    integer :: array_size = 20
    integer :: i,j, array_size_1st_d, array_size_2nd_d
    real, allocatable :: common_array(:)
    integer :: x = merge(10,5,10>5) !ternar operator
    real, allocatable :: common_2d_array(:, :)  ! for task 2.3 

    print *, "--------  2.1  ---------"!2.1 array slices
    allocate (common_array(array_size))
    do i=1, array_size
        common_array(i) = i
    end do
    print *, "common array: ", common_array
    print *, "sliced sqrt array: ", common_array(floor(array_size/4.):)
    print *,  "ternar operator: ", x    ! just for self expirience
    
    print *, "mask array", common_array>2
    print *, "masking without deleting elements: ",  common_array * merge(1,0,common_array>2) 
    print *, "masking with deletin elements: ",  pack(common_array,common_array>2) 
    
    open(1, file='example2.dat')
    write(1, '(4F10.5)') common_array(1:20:4)

    print *, "masking with vector indexes: ", common_array((/5/))

    print *, "--------  2.2  ---------" !12.2 array builtins operations
    print *, "operation all"    , all( common_array >2)
    print *, "operation any"    , any( common_array >2)
    print *, "operation 'count' true elements"  , count( common_array>2)  
    print *, "operation size"   , size(  common_array>2)
    print *, "operation shape"  , shape( common_array>2)

    print *, "opertion lbound", lbound(common_array)
    print *, "opertion ubound", ubound(common_array)
    print *, "opertion 'maxloc' max array element", maxloc(common_array)
    print *, "opertion product", product(common_array)
    print *, "opertion 'sum' to sum all elements in array", sum(common_array)
    print *, "opertion dot_product - scalar product of to arrays", dot_product(common_array, common_array)

    print *, "opertion 'matmul' produc of two matrix", dot_product(common_array, common_array(1:array_size:2))    !12.3 dynamic memory arrays
    ! а1 имеет форму (n,m), а а2 – (m,k), тогда результат имеет форму (n,k). Допустимо n=k.
    ! а1 имеет форму (m), а а2 – (m,k), тогда результат имеет форму (k).
    ! а1 имеет форму (n,m), а а2 – (m), тогда результат имеет форму (m).

    print *, "operation 'cshift' circular shift", cshift(common_array, 1)    ! циклический сдвиг массива
    print *, "operation 'eoshift' left or right shift", eoshift(common_array, -1)

    print *, "operation before reshape", common_array(1:10)
    print *, "operation reshape", reshape(common_array(1:10), (/2, 5/) )
    print *, "operation transpose", transpose(reshape(common_array(1:10), (/2, 5/) ))
    !print *, "operation ", (common_array)

    print *, "--------  2.3  ---------"!2.3 dynamic memory arrays
    array_size_1st_d =10
    array_size_2nd_d = 20
    allocate(common_2d_array(array_size_1st_d, array_size_2nd_d))
    print *, "first 2d array usage"
    do i=1, array_size_1st_d
        do j=1,array_size_2nd_d
            common_2d_array(i,j) = i+j
        end do
        print *, common_2d_array(i,:)
    end do
    deallocate(common_2d_array)
    
    array_size_1st_d = 4
    allocate(common_2d_array(array_size_1st_d, 1))
    print *,"second 2d array usage"
    do i=1, array_size_1st_d
     print *, "element number: ", i, " is ", common_2d_array(i, 1)
    end do
end program example2