; 3CXDMCC.3CX!App.jss
; Beispielhaftes begonnenes JAWS-Skript fuer die 3CX Windows Desktop App (App-Task: 3CXDMCC.3CX!App)
; Erstellt fuer JAWS 2026 mit KI-Unterstützung (Claude Code)

; ============================================================
; Konstanten
; ============================================================

Const MENU_REL_X = 36
Const MENU_REL_Y = 78


; ============================================================
; Hilfsfunktionen
; ============================================================

String Function GetNavItemLabelByIndex (int nIndex)
  If nIndex == 0 Then Return "Team" EndIf
  If nIndex == 1 Then Return "Kontakte" EndIf
  If nIndex == 2 Then Return "W�hltastatur" EndIf
  If nIndex == 3 Then Return "Rufliste" EndIf
  If nIndex == 4 Then Return "Chat" EndIf
  If nIndex == 5 Then Return "Sprachnachrichten" EndIf
  If nIndex == 6 Then Return "Mehr" EndIf
  If nIndex == 7 Then Return "Einstellungen" EndIf
  Return ""
EndFunction

; Name-Format: "NavigationViewItem 1 von 7"
String Function GetCurrentNavLabel ()
  var String sName, String sIndexStr, int nIndex

  sName = GetObjectName ()

  ; Debug: immer Segment 2 zurueckgeben um Parsing zu pruefen
  If StringStartsWith (sName, "NavigationViewItem") Then
    sIndexStr = StringSegment (sName, " ", 2)
    Return "Seg2=" + sIndexStr
  EndIf

  Return ""
EndFunction

Void Function AnnounceCurrentNavLabel ()
  var String sLabel
  sLabel = GetCurrentNavLabel ()
  If sLabel != "" Then
    StopSpeech ()
    SayString (sLabel)
  EndIf
EndFunction


; ============================================================
; Strg+M - Hamburger-Menue oeffnen
; ============================================================

Script OpenMainMenu ()
  var handle hWnd, int nX, int nY

  hWnd = GetCurrentWindow ()
  nX = GetWindowLeft (hWnd) + MENU_REL_X
  nY = GetWindowTop (hWnd) + MENU_REL_Y

  SayString ("Men�")
  ClickAtPoint (nX, nY)
EndScript


; ============================================================
; SayWindowTypeAndText - ueberschreibt JAWS-Ansage bei Fokus-Wechsel
; ============================================================

Script SayWindowTypeAndText ()
  var String sLabel
  sLabel = GetCurrentNavLabel ()
  If sLabel != "" Then
    SayString (sLabel)
  Else
    PerformDefault ()
  EndIf
EndScript


; ============================================================
; Pfeiltasten und Tab
; ============================================================

Script DownArrow ()
  TypeCurrentScriptKey ()
  ScheduleFunction ("AnnounceCurrentNavLabel", 500)
EndScript

Script UpArrow ()
  TypeCurrentScriptKey ()
  ScheduleFunction ("AnnounceCurrentNavLabel", 500)
EndScript

Script Tab ()
  TypeCurrentScriptKey ()
  ScheduleFunction ("AnnounceCurrentNavLabel", 300)
EndScript

Script ShiftTab ()
  TypeCurrentScriptKey ()
  ScheduleFunction ("AnnounceCurrentNavLabel", 300)
EndScript


String Function GetScriptDescription (String sScript)
  If sScript == "OpenMainMenu" Then Return "Oeffnet das Hauptmenue der 3CX Anwendung" EndIf
  If sScript == "SayWindowTypeAndText" Then Return "Ansage mit korrekten Nav-Item-Labels" EndIf
  Return ""
EndFunction
