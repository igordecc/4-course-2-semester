module constants  
implicit none 

   real, parameter :: pi = 3.1415926536  
   real, parameter :: e = 2.7182818285 
   
contains      
   subroutine show_consts()          
      print*, "Pi = ", pi          
      print*,  "e = ", e     
   end subroutine show_consts 
   recursive subroutine fibonacci(n,fibo)
    implicit none
    integer, intent(in) :: n
    integer, intent(out) :: fibo
    integer :: tmp
    if (n <= 2) then
        fibo = 1
    else
        call fibonacci(n-1, fibo)
        call fibonacci(n-2,tmp)
        fibo = fibo + tmp
        print *, fibo
    end if
    end subroutine fibonacci

end module constants 


program example7     
use constants      
implicit none     
   integer :: i
   real :: x, ePowerx, area, radius 
   x = 2.0
   radius = 7.0
   ePowerx = e ** x
   area = pi * radius**2     
   
   call show_consts() 
   
   print*, "e raised to the power of 2.0 = ", ePowerx
   print*, "Area of a circle with radius 7.0 = ", area  
   i = 1
   call fibonacci(20,i)
   print *, i
end program example7