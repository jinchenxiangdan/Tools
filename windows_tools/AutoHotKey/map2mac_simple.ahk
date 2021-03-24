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

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Method portion
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
MapTabPages(key) {
    Send ^%key%
}






;;;;;;;;;;;;;;;;;;;;; 
; editing 
;;;;;;;;;;;;;;;;;;;;; 

!a::Send ^a             ; select all
!x::Send ^x             ; cut
!c::Send ^c             ; copy
!v::Send ^v             ; paste
!z::Send ^z             ; undo
!+z::Send ^+z           ; un-undo
!s::Send ^s             ; save 
!f::Send ^f             ; find 
; mapping line operation 
!Left::Send {Home}      
!+Left::Send +{Home}
!Right::Send {End}
!+Right::Send +{End}
!Up::Send ^{Home}
!+Up::Send ^+{Home}
!Down::Send ^{End}
!+Down::Send ^+{End}

;;;;;;;;;;;;;;;;;;;;;;
; browsing
;;;;;;;;;;;;;;;;;;;;;;

; mapping tab switch
!1::Send ^1
!2::Send ^2
!3::Send ^3
!4::Send ^4
!5::Send ^5
!6::Send ^6
!7::Send ^7
!8::Send ^8
!9::Send ^9

; Ctrl + Tab to right shift tab 
; Ctrl + Shift + Tab to left shift tab 
; !Right::Send ^{Tab}
; !Left::Send ^+{Tab}


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

; mapping window operation 
; !w::Send ^w
!t::Send ^t
!n::Send ^n 
!+n::Send ^+n
; !r::Send ^r



; quit 
return

