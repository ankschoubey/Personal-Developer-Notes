
variable_assignment <- 'Data can be in double quotations' 

# Single line comment

"Multi line"

assign('variable_assignment2',3)
# keep in quotes if not declared

# new environment

my.environment <- new.env()

assign('var1',10, my.environment)

my.environment$var2 = 1


my.environment1 <- new.env()

assign('var1',10, my.environment1)
my.environment1$var2 = 1
india <-new.env()
assign("temp",30,india)
india[["var_4"]]=10

# maths 

abs()
log()
exp()
factorial()

## Special constants
pi


## Special Numbers

# Inf -Inf
## Infinity and -Infininty

# NaN
## Not a number


# 

months <- c('Item1', 'Item2')

## Types of operations on vector

## Type 1: vector -> gives a single value 
## Type 2: vector -> operation on each item of vector
## Type 3: multiple vector -> pairwise operation 
### Eg: Addition, ==

## Complex Numbers

a <- 1 + 6i
b <- 6 + 2i
a + b

## Factors of a set

a <- c(1,2,3,4,5,1,2,3)
b <- factor(a)
b

c <- c(a,a,a,a)
c
c = data.frame(a,a,a,a)
c


BMI = data.frame(
  gender = c('M','F'),
  height = c(1,2)
)
BMI
