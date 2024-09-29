
DROP TABLE IF EXISTS Vehicles;
DROP TABLE IF EXISTS Rentals;



CREATE TABLE Vehicles (
    VehicleID INT PRIMARY KEY,
    Make VARCHAR(100),
    Model VARCHAR(100),
    Year INT,
    DailyRate DECIMAL(6, 2)
);

CREATE TABLE Rentals (
    RentalID INT PRIMARY KEY,
    CustomerName VARCHAR(100),
    VehicleID INT,
    RentalDate DATE,
    ReturnDate DATE,
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID)
);