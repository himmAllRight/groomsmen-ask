(defun main ()
    (let ((messages '((5 . "You know, it really doesn't take this long to decrypt..") 
		      (10 . "In fact, it is probably already done.") 
		      (15 . "Every message is 'decrypted'") 
		      (20 . "Including this one...") 
		      (21 . "And This one...")
		      (22 . "And This one...")
		      (23 . "And This one...")
		      (24 . "And This one...")
		      (25 . "And Even This one...")
		      )))
      
      (loop for i from 1 to 100 do
	    (cond ((equal i (caar messages))
		   (format t "Decrpyting Message. ~d% Complete2. -- ~a ~%" 
			   i (cdar messages))
		   (setf messages (cdr messages)))
		  (t
		   (format t "Decrpyting Message. ~d% Complete.~%" i)))
	    (sleep 2))))

(defun load-test ()
  (print "loaded"))

(defun build-exe ()
  (sb-ext:save-lisp-and-die "c:\\xtemp\\testing.exe" :toplevel #'main :executable t))