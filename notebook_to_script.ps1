param (
    [string]$notebookPath  
)

Set-PSDebug -Strict

$outputDirectory = Join-Path -Path (Split-Path -Path $notebookPath -Parent) -ChildPath "python_scripts"

if (-Not (Test-Path -Path $outputDirectory)) {
    New-Item -ItemType Directory -Path $outputDirectory
}

$outputFile = Join-Path -Path $outputDirectory -ChildPath (Get-Item $notebookPath).Basename 

try {
    jupyter nbconvert --to script $notebookPath --output $outputFile 2>NUL

    if (Test-Path -Path ($outputFile + ".py")) {
        Write-Host "
        d8888b.  .d88b.  d8b   db d88888b 
        88  `8D .8P  Y8. 888o  88 88'     
        88   88 88    88 88V8o 88 88ooooo 
        88   88 88    88 88 V8o88 88~~~~~ 
        88  .8D `8b  d8' 88  V888 88.     
        Y8888D'  `Y88P'  VP   V8P Y88888P 
       "
    } else {
        Write-Host "Failed to convert $($notebookPath). Check the output above for errors."
    }
} catch {
    Write-Host "Error converting notebook: $_"
}