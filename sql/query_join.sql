-- use INNER JOIN operation and optionally include LEFT JOIN, RIGHT JOIN, etc.
SELECT Customers.Name, Orders.OrderID, Orders.OrderDate, Orders.TotalAmount
FROM Customers
INNER JOIN Orders
ON Customers.CustomerID = Orders.CustomerID
WHERE Customers.Country = 'USA';