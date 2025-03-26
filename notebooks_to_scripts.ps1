param (
    [string]$notebookPath  
)

$outputDirectory = Join-Path -Path (Split-Path -Path $notebookPath -Parent) -ChildPath "python_scripts"

if (-Not (Test-Path -Path $outputDirectory)) {
    New-Item -ItemType Directory -Path $outputDirectory
}

$outputFile = Join-Path -Path $outputDirectory -ChildPath (Get-Item $notebookPath).Basename 

try {
    $conversionResult = jupyter nbconvert --to script $notebookPath --output $outputFile 2>&1
    Write-Host "Conversion output: $conversionResult"
    Write-Host "============================================================"
    
    if (Test-Path -Path ($outputFile + ".py")) {
        Write-Host "Converted $($notebookPath) to $($outputFile)"
    } else {
        Write-Host "Failed to convert $($notebookPath). Check the output above for errors."
    }
} catch {
    Write-Host "Error converting notebook: $_"
}