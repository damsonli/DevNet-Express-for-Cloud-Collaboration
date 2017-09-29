$os = Get-WmiObject win32_operatingsystem
$uptime =(Get-Date) - ($os.ConvertToDateTime($os.lastbootuptime))
$body = @{
    roomId="Y2lzY29zcGFyazovL3VzL1JPT00vZDUyOWQyYjAtYTNkYy0xMWU3LWI5NmYtNWZiY2I3ZjUxYWEx"
    text=$uptime.ToString()
}
$json=$body | ConvertTo-Json
Invoke-RestMethod -Method Post `
-Headers @{"Authorization"="Bearer Your_Access_Token"} `
-ContentType "application/json" -Body $json `
-Uri https://api.ciscospark.com/v1/messages