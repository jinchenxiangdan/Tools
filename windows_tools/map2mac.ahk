; Author: Shawn Jin
; Purpose: Mapping the shortcut of Map on Windows. So windows OS could be used as MacOS
; Requirment: AutoHotKey
#IfWinActive
SendMode Input   ;  Recommended for new scripts due to its superior speed and reliability.

MoveCursor(key) {
    alt     := GetKeyState("ALT", "P")
    shift   := GetKeyState("SHIFT","P")
    control := GetKeyState("CONTROL","P")
    ; combination key
    controlShift := control && shift
    altShift := alt && shift

    if altShift {
        Send, !+%key%
    }
    else if controlShift {
        Send, ^+%key%
    }
    else if shift {
        Send, +%key%
    }
    else if control {
        Send, ^%key%
    }
    else {
        Send, %key%
    }

}



; 
; editing 
; 
!a::Send ^a
!x::Send ^x
!c::Send ^c
!v::Send ^v
!z::Send ^z
!s::Send ^s 
!f::Send ^f 
; line operation 
!Left::Send {Home}
!Right::Send {End}

; 
; coding
; 

; mapping quick comment
!/::Send ^/
; mapping arrow keys ! The arrow area marco doesn't work well 
!i::Send {Up}
!k::Send {Down}
!j::Send {Left}
!l::Send {Right}

; system
!w::Send ^w
!t::Send ^t
!n::Send ^n 
!r::Send ^r

; quit 
return
