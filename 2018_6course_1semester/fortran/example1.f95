program example1
    implicit none
    integer :: a=2, b=4, i
    real :: a_real=2.756, b_real= 4.257, ir
    complex :: z
    parameter (z=(-12.6, -7.69))
    integer :: int_array(10)=  (/(i, i=2, 20, 2)/)
    real :: real_array12(5)= [1.7, 2.3, 4.5, 4.8, 5.2]
    ! Arrays for 1.3
    real, allocatable :: real_array(:, :)
    complex, allocatable :: complex_array(:)

    print *, "----- 1.1 -----" ! 1.1
    print *, "integers: ", a + b
    print *, "reals: ", a_real + b_real
    print *, "complex: ", z, "complex conjugate: ", conjg(z)
    print *, "----- 1.2 -----" ! 1.2
    print *, "generated ineger array: ", int_array
    print *,  "sqrt applied to real array: ", sqrt(real_array12)
    print *,  "sin applied to real array: ", sin(real_array12)

    print *, "----- 1.3 -----" ! 1.3
    allocate (real_array (4, 2))
    real_array(:,1) = 1.0
    real_array(1:2, 2) = -1.0
    real_array(3:4, 2) = -2.0
    print *, "2d real array: "
    print '(4f10.5)', real_array

    allocate (complex_array (4))
    do i = 1, size(real_array, 1)
        complex_array(i) = complex(real_array(i,1), real_array(i,2))
    end do
    print *, "complex array: "
    print '(f10.5,f10.5,"i")', complex_array

    deallocate(real_array)
    deallocate(complex_array)

end program example1