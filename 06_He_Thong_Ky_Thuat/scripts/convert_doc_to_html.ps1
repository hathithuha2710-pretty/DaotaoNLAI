$inputFile = Get-ChildItem -Path "04_Hoc_Lieu_Va_Tham_Khao" -Recurse | Where-Object { $_.Extension -eq ".doc" -and $_.Name -like "*mon-tin-hoc*" } | Select-Object -First 1
Write-Host "Opening: $($inputFile.FullName)"

$outDir = (Get-Item "06_He_Thong_Ky_Thuat\extracted_data").FullName
$outFile = [string](Join-Path $outDir "Chuong-trinh-giao-duc-pho-thong-2018-mon-tin-hoc.html")

$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0

try {
    $doc = $word.Documents.Open([string]$inputFile.FullName, $false, $true, $false)
    Write-Host "Opened successfully. Now saving as HTML..."
    # 10 = wdFormatFilteredHTML, 8 = wdFormatHTML
    $doc.SaveAs2($outFile, 10)
    $doc.Close(0)
    Write-Host "HTML saved successfully: $outFile"
} catch {
    Write-Host "Error: $($_.Exception.Message)"
} finally {
    $word.Quit()
}
