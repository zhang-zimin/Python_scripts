Sub weishui()
    Dim t As Integer
    Range("C2").Select
    ActiveCell.FormulaR1C1 = "=RC[-1]-R1C2"
    Range("C2").Select
    t = Cells(Cells.Rows.Count, 1).End(xlUp)
    Selection.AutoFill Destination:=Range("C2:C" & t + 1)
    Range("C2:C" & t + 1).Select
    Range("D3").Select
    ActiveCell.FormulaR1C1 = "=MAX(C[-1])"
    Range("D4").Select
    
Dim i As Integer

    For i = 1 To 10000
If Range("d3").Value = Range("c" & i).Value Then
 Range("d" & i) = 0
 End If
Next
    For i = 1 To 10000
If Range("d" & i) = "0" Then

    Range("d" & i + 1).Select
    ActiveCell.FormulaR1C1 = "1"
    Range("D" & i).Resize(2, 1).Select
    Selection.AutoFill Destination:=Range("D" & i & ":d" & t + 1)
    
     Range("E" & i).Select
     ActiveCell.FormulaR1C1 = "=RC[-2]/-R" & i & "C3"
     Selection.AutoFill Destination:=Range("E" & i & ":E" & t + 1)
     Range("D" & i & ":E" & t + 1).Select
End If
Next
End Sub
