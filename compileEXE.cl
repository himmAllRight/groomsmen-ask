(defun build-main ()
       (load "decryptMessage.cl")
       (sb-ext:save-lisp-and-die "message" :toplevel #'main :executable t))