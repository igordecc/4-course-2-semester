module constants  
implicit none 

   real, parameter :: pi = 3.1415926536  
   real, parameter :: e = 2.7182818285 
   
contains      
   subroutine show_consts()          
      print*, "   Pi = ", pi          
      print*,  "  e = ", e     
   end subroutine show_consts 
   
   subroutine many_functions(inarray)
      implicit none
      integer :: i
      integer ,intent(in):: inarray(:)
      !real , intent(out):: element
      integer,allocatable :: array(:)

      array = inarray
      print *, "array size: ", size(array)
      print *, array
      print *, inarray
      return

      entry summ(inarray, i)
         print *, "array + ", 5, " = ", inarray + i
      return
      
      entry substr(inarray,i)
         print *, "array - ", 5, " = ", inarray - i
      return
   end subroutine many_functions
end module constants 


program example7     
use constants      
implicit none     
   integer :: i
   real :: powered_e, area
   real :: AVRAGE
   integer, allocatable :: inarray(:)

   print *, "-------- 7.1 -----------"
   print *, "module with constants: "
   call show_consts() 
   powered_e = e ** 2
   print*, "   e raised to the power of 2.0 = ", powered_e
   area = pi * 7.0**2
   print*, "   Area of a circle with radius 7.0 = ", area  
   
   print *, "avarage function"
   print *, "  avarage of 3 numbers: ", AVRAGE(1.,2.,3.)

   print*, "----- 7.2 -------"
   i = 1
   print *, "recursive subroutine fibonacci"
   call fibonacci(20,i)
   print *, "  fibonacci number: ", i
   
   print *, "---------- 7.3 ---------"
   print *,"initial array: ",  (/(i,i=1,10,1)/)

   !included in include_file.f95 
   !inarray = (/(i,i=1,10,1)/)
   !call many_functions(inarray)
   !call summ(inarray, 5)
   !call substr(inarray, 5)
   include 'include_file.f95'


end program example7

real function AVRAGE(X,Y,Z)
     real x,y,z,sum
     sum = x + y + z
     AVRAGE = sum /3.0
     return ! task 7.3 RETURN
     end

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
    end if
    end subroutine fibonacci