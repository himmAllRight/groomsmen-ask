;; Used to build the executable
(defun build-exe (exe-src)
  (sb-ext:save-lisp-and-die exe-src :toplevel #'main :executable t))

(defun main ()
  (intro-message)
  (decrypt-loading)
  (secret-message))

(defun intro-message ()
  (format t "~a~%~%~%" (decode-message '(72 101 108 108 111 33 80 108 101 97 115 
					 101 32 119 97 105 116 32 97 32 109 105 110 
					 117 116 101 32 119 104 105 108 101 32 121 
					 111 117 114 32 115 101 99 114 101 116 32 
					 109 101 115 115 97 103 101 32 105 115 32 
					 100 101 99 114 121 112 116 101 100 33)))
  (sleep 2)
  (format t "Starting decryption...~%")
  (sleep 1))

(defun decrypt-loading ()
  (let* ((messages '((#\Enq 89 111 117 32 107 110 111 119 44 32 105 116 32 114 101 97 108 108 121
			   32 100 111 101 115 110 39 116 32 116 97 107 101 32 116 104 105 115 32 108 111
			   110 103 32 116 111 32 100 101 99 114 121 112 116 46 46)
		    (#\Newline 73 110 32 102 97 99 116 44 32 105 116 32 105 115 32 112 114 111 98
		     97 98 108 121 32 97 108 114 101 97 100 121 32 100 111 110 101 46)
		    (#\Si 69 118 101 114 121 32 109 101 115 115 97 103 101 32 105 115 32 39 100
		     101 99 114 121 112 116 101 100 39)
		    (#\Dc4 73 110 99 108 117 100 105 110 103 32 116 104 105 115 32 111 110 101 46
		     46 46)
		    (#\Nak 65 110 100 32 84 104 105 115 32 111 110 101 46 46 46)
		    (#\Syn 65 110 100 32 84 104 105 115 32 111 110 101 46 46 46)
		    (#\Etb 65 110 100 32 84 104 105 115 32 111 110 101 46 46 46)
		    (#\Can 65 110 100 32 84 104 105 115 32 111 110 101 46 46 46)
		    (#\Em 65 110 100 32 69 118 101 110 32 84 104 105 115 32 111 110 101 46 46 46)))
	(decrypted-messages (decode-pair-list messages)))

      (loop for i from 0 to 100 do
	    (cond ((equal i (caar decrypted-messages))
		   (format t "Decrpyting Message. ~d% Complete2. -- ~a ~%" 
			   i (cdar decrypted-messages))
		   (setf decrypted-messages (cdr decrypted-messages)))
		  (t
		   (format t "Decrpyting Message. ~d% Complete.~%" i)))
	    (sleep 1))))

(defun secret-message ()
  (format t "~%~% ~a" "This is where I will write the secret message!!!"))

(defun encode-message (message)
  (mapcar #'char-code (concatenate 'list message)))

(defun decode-message (num-list)
  (map 'string #'code-char num-list))

(defun encode-pair-list (pair-list)
  (mapcar (lambda (pair) (cons (code-char (car pair)) (encode-message (cdr pair)))) pair-list))

;;(load "decryptMessage.cl")


(defun decode-pair-list (pair-list)
 (mapcar (lambda (pair) (cons (char-code (car pair)) (decode-message (cdr pair)))) pair-list))