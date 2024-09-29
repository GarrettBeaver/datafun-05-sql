-- average daily rate
SELECT AVG(DailyRate) AS AverageDailyRate
FROM Vehicles;

-- count number of cars by year
SELECT Year, COUNT(*) AS NumberOfVehicles
FROM Vehicles
GROUP BY Year;