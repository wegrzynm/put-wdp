CREATE TABLE Products (
  ProductID int primary key,
  ProductName varchar(100),
  Price int,
  InStock bool //tinyint
);

INSERT INTO Products (ProductID, ProductName, Price, InStock)
VALUES (1,"Laptop",3000,1),(2,"Mouse", 50,1),(3,"Monitor",800, 0);

SELECT ProductName
FROM Products;
