from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Incrementador(BoxLayout):
    pass
class Teste(App):
    def build(self):
        return Incrementador()
    
Teste().run()

Public Function GFKEY_MsgBoxKey(PFStr_logModulo As String, PFStr_logNmForm As String, PFStr_Proc As String, Prompt, Optional PFStr_BD As String = "T", Optional Buttons As VbMsgBoxStyle = vbOKOnly, Optional Title = "Keysystems Informática", Optional HelpFile, Optional Context, Optional PFBol_GravaLOG As Boolean = True) As VbMsgBoxResult
    Dim WLStr_Data         As String
    Dim WLStr_Hora         As String
    Dim WLStr_Sql          As String
    Dim WLStr_VBResult()   As String
    '
    ReDim WLStr_VBResult(0) As String
    ReDim Preserve WLStr_VBResult(1) As String
    WLStr_VBResult(1) = "OK"
    ReDim Preserve WLStr_VBResult(2) As String
    WLStr_VBResult(2) = "CANCELAR"
    ReDim Preserve WLStr_VBResult(3) As String
    WLStr_VBResult(3) = "ABORTAR"
    ReDim Preserve WLStr_VBResult(4) As String
    WLStr_VBResult(4) = "TENTAR NOVAMENTE"
    ReDim Preserve WLStr_VBResult(5) As String
    WLStr_VBResult(5) = "IGNORAR"
    ReDim Preserve WLStr_VBResult(6) As String
    WLStr_VBResult(6) = "SIM"
    ReDim Preserve WLStr_VBResult(7) As String
    WLStr_VBResult(7) = "NÃO"
    WLStr_Data = Format(Date, "yyyymmdd")
    WLStr_Hora = Format(time, "hhmmss")
    '
    If PFBol_GravaLOG = True Then
        If Trim(PFStr_BD) = "T" Or Trim(PFStr_BD) = "A" Then
            If Not GFKEY_GravaLog(UCase(PFStr_logModulo), WLStr_Data, WLStr_Hora, WGStr_Usuario, Replace(IIf(Trim(PFStr_Proc) <> Empty, UCase(Trim(PFStr_Proc)) & ": ", "") & UCase(Trim(Prompt)) & " = ???", Chr(10), " "), "A", PFStr_logNmForm) Then
                If UCase(Trim(WGStr_Usuario)) = "KEYADMINISTR" Then
                    MsgBox "Erro de gravação do Log (GFKEY_MsgBoxKey)!" & vbLf & vbLf & _
                           "Código: " & Err.Number & vbLf & _
                           "Descrição: " & Err.Description & vbLf & _
                           IIf(Trim(PFStr_logNmForm) = "", "", "Chamador: " & PFStr_logNmForm & vbLf) & vbLf & _
                           "Log (A): " & Replace(IIf(Trim(PFStr_Proc) <> Empty, UCase(Trim(PFStr_Proc)) & ": ", "") & UCase(Trim(Prompt)) & " = ???", Chr(10), " "), vbCritical + vbOKOnly, "Keysystems Informática"
                Else
                    MsgBox "Atenção!" & Chr(10) & Chr(10) & "Problemas ao gravar LOG de alertas, informe ao suporte imediatamente!", vbExclamation, "Keysystems Informática"
                End If
                Exit Function
            End If
        End If
        If Trim(PFStr_BD) = "T" Or Trim(PFStr_BD) = "B" Then
            If Not GFKEY_GravaLog(UCase(PFStr_logModulo), WLStr_Data, WLStr_Hora, WGStr_Usuario, Replace(UCase(Trim(PFStr_Proc)) & ": " & UCase(Trim(Prompt)) & " = ???", Chr(10), " "), "B", PFStr_logNmForm) Then
                If UCase(Trim(WGStr_Usuario)) = "KEYADMINISTR" Then
                    MsgBox "Erro de gravação do Log (GFKEY_MsgBoxKey)!" & vbLf & vbLf & _
                           "Código: " & Err.Number & vbLf & _
                           "Descrição: " & Err.Description & vbLf & _
                           IIf(Trim(PFStr_logNmForm) = "", "", "Chamador: " & PFStr_logNmForm & vbLf) & vbLf & _
                           "Log (B): " & Replace(UCase(Trim(PFStr_Proc)) & ": " & UCase(Trim(Prompt)) & " = ???", Chr(10), " "), vbCritical + vbOKOnly, "Keysystems Informática"
                Else
                    MsgBox "Atenção!" & Chr(10) & Chr(10) & "Problemas ao gravar LOG de alertas, informe ao suporte imediatamente!", vbExclamation, "Keysystems Informática"
                End If
                Exit Function
            End If
        End If
    End If
    '
    Beep
    GFKEY_MsgBoxKey = MsgBox("Atenção!" & Chr(10) & Chr(10) & Prompt, Buttons, Title, HelpFile, Context)
    '
    If PFBol_GravaLOG = True Then
        WLStr_Sql = "update LOG_MANUTENCAO_" & Left(Format(Date, "yyyymmdd"), 4) & " set log_Histor = replace(log_Histor,'???','" & WLStr_VBResult(GFKEY_MsgBoxKey) & "') "
        WLStr_Sql = WLStr_Sql & "where "
        WLStr_Sql = WLStr_Sql & "log_DataRf = '" & WLStr_Data & "' and log_HoraRf = '" & WLStr_Hora & "' and log_Modulo = '" & PFStr_logModulo & "' and "
        WLStr_Sql = WLStr_Sql & "log_NmForm = '" & PFStr_logNmForm & "' and log_Histor like '%???%'"
        '
        If Trim(PFStr_BD) = "T" Or Trim(PFStr_BD) = "A" Then WGCnx_DBPrim.Execute WLStr_Sql
        If Trim(PFStr_BD) = "T" Or Trim(PFStr_BD) = "B" Then WGCnx_DBSegu.Execute WLStr_Sql
    End If
End Function