


select DEVICE_ID, count(*) / (SELECT COUNT(*) FROM TableName) as percentage
FROM event_logs
GROUP BY DEVICE_ID
order_by percentage desc
