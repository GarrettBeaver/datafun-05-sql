-- use aggregation functions including COUNT, AVG, SUM.
SELECT AVG(DailyRate) AS AverageDailyRate
FROM Vehicles;

SELECT Year, COUNT(*) AS NumberOfVehicles
FROM Vehicles
GROUP BY Year;