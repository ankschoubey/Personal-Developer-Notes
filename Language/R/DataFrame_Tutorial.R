# DataFrame

## Similar to dataframe in Pandas
### Creating Dataframe

a1 = c(1,2,3)
a2 = c(4,5,6)
a3 = c(7,8,9)

df = data.frame(a1,a2,a3)
#

"a1 a2 a3       # name of the columns = name of variable and index starts from 0
1  1  4  7
2  2  5  8
3  3  6  9"

# Replacing values. Remember R is 1 indexed. So Stupid!
row = 1
col = 2
df[[row]][col] = 3

#print(df)

# Creation of Dataframe from file

## df = read.table(file="/Users/ankushchoubey/Desktop/test.csv", sep=',')
## df[row, column]
#print(df[1:4,1:3])

# Visual Edit - Opens a GUI Editing tool
## df = edit(df)

# Appending Rows and columns

## df = rbind(df, c(123123123,123,21,23))
## df = cbind(df, c(12,3,4,5,5,6,6))

# Deleting - sign while accessing indicated deletion delete this row and this column
df = df[-2,-2]
print(df)



