$inputFile = Get-ChildItem -Path "04_Hoc_Lieu_Va_Tham_Khao" -Recurse | Where-Object { $_.Extension -eq ".doc" -and $_.Name -like "*mon-tin-hoc*" } | Select-Object -First 1
Write-Host "Opening: $($inputFile.FullName)"

$outDir = (Get-Item "06_He_Thong_Ky_Thuat\extracted_data").FullName
$outFile = [string](Join-Path $outDir ($inputFile.BaseName + ".docx"))

$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0

try {
    $doc = $word.Documents.Open([string]$inputFile.FullName, $false, $true, $false)
    Write-Host "Document opened. Paragraphs count: $($doc.Paragraphs.Count)"
    $doc.SaveAs2($outFile, 16) # 16 = wdFormatDocumentDefault
    $doc.Close(0)
    Write-Host "Successfully saved to: $outFile"
} catch {
    Write-Host "Error: $($_.Exception.Message)"
} finally {
    $word.Quit()
}
