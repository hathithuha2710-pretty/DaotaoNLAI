$docPath = "C:\Users\USER\Desktop\AI-vibe-code\KhungNLĐTAI\04_Hoc_Lieu_Va_Tham_Khao\SGK Tin học\Chuong-trinh-giao-duc-pho-thong-2018-mon-tin-hoc.doc"
$docxPath = "C:\Users\USER\Desktop\AI-vibe-code\KhungNLĐTAI\06_He_Thong_Ky_Thuat\extracted_data\Chuong-trinh-giao-duc-pho-thong-2018-mon-tin-hoc.docx"

try {
    $word = New-Object -ComObject Word.Application
    $word.Visible = $false
    $word.DisplayAlerts = 0
    Write-Host "Opening doc file: $docPath"
    $doc = $word.Documents.Open($docPath)
    Write-Host "Saving as docx: $docxPath"
    # wdFormatXMLDocument = 12
    $doc.SaveAs2($docxPath, 12)
    $doc.Close()
    $word.Quit()
    Write-Host "Successfully converted doc to docx!"
} catch {
    Write-Host "Error: $($_.Exception.Message)"
    if ($word) { $word.Quit() }
}
