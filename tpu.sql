
--Hace muchos años no trabajo con SQL y no me dió el tiempo, disculpen

select DEVICE_ID, count(*) / (SELECT COUNT(*) FROM TableName) as percentage
FROM event_logs
GROUP BY DEVICE_ID
order_by percentage desc
