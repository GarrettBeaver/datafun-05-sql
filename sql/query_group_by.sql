-- sum daily rate by year
SELECT Year, SUM(DailyRate) AS TotalRateByYear
FROM Vehicles
GROUP BY Year;