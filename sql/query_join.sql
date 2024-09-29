SELECT Rentals.RentalID, 
       Vehicles.Make, 
       Vehicles.Model, 
       Rentals.RentalDate, 
       Rentals.ReturnDate
FROM Rentals
INNER JOIN Vehicles ON Rentals.VehicleID = Vehicles.VehicleID;