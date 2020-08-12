;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Author: Shawn Jin
;         jinchenxiangdan.github.io
; Purpose: Mapping the shortcut of Map on Windows. So windows OS could be used as MacOS
;          Key Map:
;               Alt     -> Command
;               Windows -> option
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Requirment: AutoHotKey (autohotkey.com)
;       Alt         -> !
;       Ctrl        -> ^
;       Shift       -> ^
;       Win Logo    -> #
; For more KeyList: https://www.autohotkey.com/docs/KeyList.htm
;                   http://xahlee.info/mswin/autohotkey_key_notations.html
; Want it lunch when your PC startup? : https://www.autohotkey.com/docs/FAQ.htm#Startup
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
#IfWinActive
SendMode Input   ;  Recommended for new scripts due to its superior speed and reliability.

;;;;;;;;;;;;;;;;;;;;; 
; editing 
;;;;;;;;;;;;;;;;;;;;; 
!a::Send ^a
!x::Send ^x
!c::Send ^c
!v::Send ^v
!z::Send ^z
!s::Send ^s 
!f::Send ^f 
; line operation 
!Left::Send {Home}
!+Left::Send +{Home}
!Right::Send {End}
!+Right::Send +{End}
!Up::Send ^{Home}
!+Up::Send ^+{Home}
!Down::Send ^{End}
!+Down::Send ^+{End}

;;;;;;;;;;;;;;;;;;;;;;
; coding
;;;;;;;;;;;;;;;;;;;;;; 

; mapping quick comment
!/::Send ^/
; mapping arrow keys 
!i::Send {Up}
!k::Send {Down}
!j::Send {Left}
!l::Send {Right}

;;;;;;;;;;;;;;;;;;;;;;
; system
;;;;;;;;;;;;;;;;;;;;;;
!w::Send ^w
!t::Send ^t
!n::Send ^n 
!r::Send ^r
!1::Send ^1
!2::Send ^2
!3::Send ^3
!4::Send ^4
; quit 
return

