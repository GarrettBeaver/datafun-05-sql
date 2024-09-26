-- use GROUP BY clause (and optionally with aggregation)
SELECT Year, SUM(DailyRate) AS TotalRateByYear
FROM Vehicles
GROUP BY Year;