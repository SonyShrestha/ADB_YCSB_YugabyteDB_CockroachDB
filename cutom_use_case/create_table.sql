CREATE DATABASE ecommerce;

\c ecommerce

CREATE TABLE products (
    ProductID INT PRIMARY KEY,
    ProductName TEXT,
    Category TEXT,
    Price NUMERIC,
    StockQuantity INT,
    VendorID INT,
    DateAdded DATE
);

CREATE TABLE customers (
    CustomerID INT PRIMARY KEY,
    CustomerName TEXT,
    Location TEXT,
    JoinDate DATE
);

CREATE TABLE sales (
    SaleID INT PRIMARY KEY,
    ProductID INT,
    QuantitySold INT,
    SaleDate DATE,
    CustomerID INT,
    TotalPrice NUMERIC,
    FOREIGN KEY (ProductID) REFERENCES products (ProductID),
    FOREIGN KEY (CustomerID) REFERENCES customers (CustomerID)
);