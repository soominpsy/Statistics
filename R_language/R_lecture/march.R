#install.packages("installr")
#require(installr)
#updateR()

# 1.1 R previes
#install.packages("ISwR")
#library(ISwR)

#c(42,35,23,53,52)
#x<-c(1,2,3)
#y<-c(10,20)
#z<-c(x,y,5)
#z

#x = c(1,2,3,4)
#x.1 <- c(1.1, 2.2, 3.3, 4,4)
#x1<-c(1,2,3,4)
#X<-c(1,2,3,4)

#x;X;x1
#class(x)
#class(x.1)
#is.numeric(x)
#is.factor(x)
#is.integer(x)
#is.character(x)

#x1 <- c(1.1, 2.2, 3.3, 4.4, 5.5, 6.6)
#x2 <- as.integer(x1)
#x1; class(x1)
#x2; class(x2)
#is.integer(x2); is.numeric(x2); is.character(x2)
#is.logical(x2)

#y <- c(T,T,F,F); y; is.logical(y)
#y<-c(TRUE, FALSE); y; is.logical(y)
#y1<-c(0,1,1,0); y1; is.logical(y1)
#y1=as.logical(y1); y1; is.logical(y1)
#y2<-c(0,1,2,3); y2; y2=as.logical(y2); y2
#y3<-c(0.0,0.1,0.2,0.4,0.5,0.7, 0.8, 0.999999, 1); y3; y3=as.logical(y3); y3

#x<-c(T,T,F,F); y<-c(0,2,3,4)
#x=as.character(x); x; is.character(x)
#y=as.character(y); y; is.character(y)

# z <- c("I","you")
# z
# class(z)
# length(z)
#nchar(z)
#z=="I"

#sex = factor(c(1,1,0,0,1), level=c(0,1), labels=c("male","female")); sex;
#sex = factor(c(1,1,0,0,1), level=c(0,1)); sex;

#exp(-2)
#rnorm(16)

############ 2018/03/05

#x <- c(1,2,3)
#y <-c(10,20)
#z <- x*c(3,2,1)
#print(z)
#z.1 <- c(x,5,y); print(z.1); length(z.1)

#z.2 <- as.character(z.1); class(z.2); print(z.2)

#x.1 <-c("Harry","Dewey","Louie"); class(x.1)
#x.2 <- c("a","B",'C'); class(x.2)
#x.3 <- c(T,T,F,T,F); class(x.3)

c("Harry","Dewey","Louie")         # output : "Harry" "Dewey" "Louie"
cat(c("Harry","Dewey","Louie"))    # output : Harry Dewey Louie  
cat("Harry","Dewey","Louie","\n")  # output : Harry Dewey Louie 
c("what is \"R\"?\n")
cat("what is \"R\"?\n")
cat("what is R ?\n")

x<-c(red="huey",blue="dewey",green="louie");  # adding tags : tag name : "red" "blue" "green"
x.1<-c("Harry","Dewey","Louie")
names(x); class(names(x)); class(x)
names(x.1); class(names(x.1)); class(x.1)
#print(x); print(x.1)        
        
y.1<-c("1"=1, "2"=2, "3"=3); #print(y.1)
names(y.1); class(names(y.1)); class(y.1);  # adding tags : tag name : "1", "2","3"
# so the tag has to be in format of string, the type of the data store inside is flexible.

z.0 <- c(F,3); print(z.0);
z.1 <- c(3.14,"abc"); print(z.1); class(z.1); names(z.1);  # so the vector inside has to be same type, the 3.14 would be change into string
z.3 <- c(FALSE,"abc"); print(z.3)
z.4 <- c("1",3.14); class(z.4); print(z.4);
z.4 <- as.double(z.4); class(z.4); print(z.4)



