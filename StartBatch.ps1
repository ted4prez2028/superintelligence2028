# Starts backend and frontend concurrently

$backend = Start-Process -FilePath "python" -ArgumentList "-m uvicorn api.server:app --host 0.0.0.0 --port 8080 --reload" -WorkingDirectory "$PSScriptRoot/backend" -PassThru -NoNewWindow
$frontend = Start-Process -FilePath "npm" -ArgumentList "run dev" -WorkingDirectory "$PSScriptRoot/frontend" -PassThru -NoNewWindow

Write-Host "Backend PID: $($backend.Id)"
Write-Host "Frontend PID: $($frontend.Id)"

Wait-Process -Id $backend.Id,$frontend.Id
